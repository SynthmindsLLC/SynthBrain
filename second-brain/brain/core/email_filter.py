"""Email triage — decide which messages reach the brain.

Default: KEEP personal + work + transactional-receipts; DROP marketing,
newsletters, and bulk notifications. The brain's dossier value is in
correspondence between humans, not in retailer broadcasts.

Stages (cheap -> expensive, short-circuit on any hard signal):
  1. RFC-8058 List-Unsubscribe header  -> drop (bulk-mail signal)
  2. Hard-block From/Subject patterns  -> drop (noreply, ESP domains, etc.)
  3. Sender allowlist                   -> keep (Google Contacts, iCloud
                                          Contacts, the brain's Person.aliases)
  4. Domain allowlist                   -> keep (owner's own domains)
  5. LLM tiebreaker                     -> keep/drop with a label
                                          (only when ANTHROPIC_API_KEY set)
  6. Default                            -> drop (unknown sender, no signal)

Output is an EmailVerdict so adapters can record WHY a message was dropped
(useful for auditing the filter, especially in the first couple weeks).
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable

ADAPTER_NAME = "email-filter"

# --- hard rules -------------------------------------------------------------

# From-address local parts that always read as automated bulk mail.
HARD_BLOCK_LOCAL_PARTS = frozenset({
    "noreply", "no-reply", "donotreply", "do-not-reply",
    "notifications", "notification", "newsletter", "news",
    "marketing", "promo", "promotions", "offers", "deals",
    "support-noreply", "bounces", "mailer-daemon", "postmaster",
    "info", "hello", "team", "updates", "alerts",
})

# ESP / bulk-mail sender domains. Any From: domain ending in one of these
# is bulk by definition.
HARD_BLOCK_DOMAINS = frozenset({
    "mailchimp.com", "mcsignup.com", "mc.us", "list-manage.com",
    "sendgrid.net", "sendgrid.com",
    "customeriomail.com", "customer.io",
    "klaviyomail.com", "klaviyo.com",
    "mailgun.org", "mailgun.com",
    "postmarkapp.com",
    "mandrillapp.com",
    "convertkit.com", "convertkit-mail2.com",
    "substack.com",
    "rsgsv.net", "intuit.com",
    "ebay.com", "amazon.com", "amazonses.com",
    "shopify.com", "shopifyemail.com",
    "constantcontact.com", "ccsend.com",
    "salesforce.com", "exct.net", "exacttarget.com",
    "hubspotmail.com", "hubspotemail.net",
    "marketo.org",
})

# Subject patterns that strongly indicate bulk/marketing.
SUBJECT_BLOCK_RE = re.compile(
    r"\b(unsubscribe|view in browser|view online|"
    r"newsletter|weekly digest|monthly digest|daily digest|"
    r"% off|sale ends|limited time|early access|"
    r"survey results|webinar|"
    r"sponsored|\[ad\]|\[adv\]|\[promo\])\b",
    re.IGNORECASE,
)

# Body-side bulk markers (looked at only if header doesn't expose
# List-Unsubscribe explicitly).
BODY_UNSUBSCRIBE_RE = re.compile(
    r"\b(click here to unsubscribe|to stop receiving|"
    r"manage your preferences|update your subscription|"
    r"you are receiving this email because|"
    r"this email was sent to)\b",
    re.IGNORECASE,
)

# Transactional receipts we DO want to keep — they're personal/work signal
# (purchase history, work-tool notifications you actually act on).
TRANSACTIONAL_HINTS_RE = re.compile(
    r"\b(receipt|invoice|order #|order confirmation|"
    r"shipping|delivered|tracking|"
    r"booking confirmation|reservation|"
    r"payment received|paid|refund issued|"
    r"signed contract|docusign|hellosign)\b",
    re.IGNORECASE,
)


class Decision(str, Enum):
    KEEP = "keep"
    DROP = "drop"


@dataclass
class EmailMeta:
    """The minimum an adapter passes in. Body is markdown / plain-text only;
    HTML should be stripped before classification."""
    from_addr: str = ""
    from_name: str = ""
    to_addrs: list[str] = field(default_factory=list)
    subject: str = ""
    body: str = ""
    headers: dict[str, str] = field(default_factory=dict)


@dataclass
class EmailVerdict:
    decision: Decision
    label: str = ""        # personal | work | transactional | marketing | newsletter | unknown
    reason: str = ""       # short, debuggable
    stage: str = ""        # which stage produced the decision


def classify_email(
    meta: EmailMeta,
    *,
    allowlist: Iterable[str] = (),
    own_domains: Iterable[str] = (),
    llm_tiebreaker: bool = True,
) -> EmailVerdict:
    """Run the cheap-to-expensive cascade. `allowlist` is a set of email
    addresses (lowercase) treated as personal/work by definition (your
    Contacts merged with the brain's Person aliases). `own_domains` are
    the domains you control or work under (auto-keep for senders/receivers
    matching them)."""
    from_lower = meta.from_addr.lower().strip()
    local, _, domain = from_lower.partition("@")
    allow = {a.lower().strip() for a in allowlist}
    own = {d.lower().lstrip("@") for d in own_domains}

    # Stage 1 — RFC-8058 List-Unsubscribe header
    lu = _header(meta.headers, "list-unsubscribe")
    if lu:
        return EmailVerdict(Decision.DROP, label="marketing",
                            reason="List-Unsubscribe header present",
                            stage="list-unsubscribe")

    # Stage 2 — hard-block patterns (from local part + domain + subject)
    if local in HARD_BLOCK_LOCAL_PARTS:
        return EmailVerdict(Decision.DROP, label="newsletter",
                            reason=f"from local-part {local!r} is bulk",
                            stage="hard-block-local")
    if any(domain == d or domain.endswith("." + d) for d in HARD_BLOCK_DOMAINS):
        return EmailVerdict(Decision.DROP, label="marketing",
                            reason=f"ESP domain {domain}",
                            stage="hard-block-domain")
    if meta.subject and SUBJECT_BLOCK_RE.search(meta.subject):
        # Even with a real human From, an "Unsubscribe in subject" is bulk.
        return EmailVerdict(Decision.DROP, label="marketing",
                            reason="bulk pattern in subject",
                            stage="hard-block-subject")
    if BODY_UNSUBSCRIBE_RE.search(meta.body[:2000]):
        return EmailVerdict(Decision.DROP, label="marketing",
                            reason="unsubscribe boilerplate in body",
                            stage="hard-block-body")

    # Stage 3 — sender allowlist
    if from_lower in allow:
        return EmailVerdict(Decision.KEEP, label="personal",
                            reason="sender in contacts/known persons",
                            stage="allowlist")

    # Stage 4 — own domains (yours and recipients you correspond with often)
    if domain and any(domain == d or domain.endswith("." + d) for d in own):
        return EmailVerdict(Decision.KEEP, label="work",
                            reason=f"from your domain {domain}",
                            stage="own-domain")
    for to in meta.to_addrs:
        _, _, tod = to.lower().partition("@")
        if tod and any(tod == d or tod.endswith("." + d) for d in own):
            # to your own address from someone else — likely real
            break
    else:
        tod = ""

    # Stage 5 — transactional-keep heuristic
    if TRANSACTIONAL_HINTS_RE.search(meta.subject + " " + meta.body[:500]):
        return EmailVerdict(Decision.KEEP, label="transactional",
                            reason="receipt/order/booking pattern",
                            stage="transactional")

    # Stage 6 — LLM tiebreaker (only when we have a key + opted in)
    if llm_tiebreaker and os.environ.get("ANTHROPIC_API_KEY"):
        try:
            label = _llm_label(meta)
            decision = Decision.KEEP if label in ("personal", "work", "transactional") else Decision.DROP
            return EmailVerdict(decision, label=label,
                                reason="LLM tiebreaker",
                                stage="llm")
        except Exception:
            pass  # fall through to default

    # Stage 7 — default: drop. We refuse to keep unknown-sender bulk-looking mail.
    return EmailVerdict(Decision.DROP, label="unknown",
                        reason="no signal that this is personal/work",
                        stage="default")


def build_allowlist_from_store(store) -> set[str]:
    """Walk the brain's EntityStore and harvest every email address attached
    to a Person entity. These addresses bypass the filter."""
    out: set[str] = set()
    for e in store.all_entities("person"):
        for em in e.attributes.get("emails") or []:
            if isinstance(em, str) and "@" in em:
                out.add(em.lower().strip())
        for alias in e.aliases:
            if "@" in alias:
                out.add(alias.lower().strip())
    return out


# --- helpers ----------------------------------------------------------------

def _header(headers: dict[str, str], name: str) -> str:
    name_l = name.lower()
    for k, v in headers.items():
        if k.lower() == name_l:
            return v or ""
    return ""


_LLM_PROMPT = """\
Classify this email into exactly one label:
- "personal": from / to an individual person, not bulk
- "work": professional correspondence
- "transactional": receipt, invoice, booking, shipping notification
- "marketing": promotional content from a company
- "newsletter": content broadcast (digest, briefing)

Reply with ONLY one lowercase word: personal, work, transactional, marketing, newsletter.

From: {sender}
Subject: {subject}

Body excerpt:
\"\"\"
{body}
\"\"\"
"""


def _llm_label(meta: EmailMeta) -> str:
    from .synthesize import _post_anthropic, _extract_text, DEFAULT_MODEL

    prompt = _LLM_PROMPT.format(
        sender=f"{meta.from_name} <{meta.from_addr}>" if meta.from_name else meta.from_addr,
        subject=meta.subject[:200],
        body=(meta.body or "")[:1500],
    )
    payload = _post_anthropic({
        "model": DEFAULT_MODEL,
        "max_tokens": 6,
        "messages": [{"role": "user", "content": prompt}],
    })
    raw = _extract_text(payload).strip().lower().strip(".,'\"")
    valid = {"personal", "work", "transactional", "marketing", "newsletter"}
    if raw in valid:
        return raw
    for tok in raw.split():
        tok = tok.strip(".,'\"")
        if tok in valid:
            return tok
    return "unknown"
