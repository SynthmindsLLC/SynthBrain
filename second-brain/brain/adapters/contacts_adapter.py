"""Contacts adapter — vCard (.vcf) -> Person entities.

vCard is the universal contacts export: iPhone, Google Contacts, and Outlook all
emit it, so this one adapter covers every place Wes's contacts might live. Each
VCARD becomes a Person node carrying the ground-truth attributes (full name,
org, title, email, phone, notes) that the dossier reads from.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import vobject

from ..core.entities import Entity
from .entity_base import EntityAdapter


def _val(component, attr):
    try:
        return getattr(component, attr).value
    except AttributeError:
        return None


class ContactsAdapter(EntityAdapter):
    name = "contacts"

    def __init__(self, source: str) -> None:
        self.source = Path(source)

    def fetch(self) -> Iterable[Entity]:
        if not self.source.exists():
            raise FileNotFoundError(
                f"vCard file not found: {self.source}. Export contacts as .vcf "
                "(iPhone: Contacts > Export; Google: Contacts > Export > vCard)."
            )
        raw = self.source.read_text(encoding="utf-8", errors="replace")
        for card in vobject.readComponents(raw):
            full_name = _val(card, "fn")
            if not full_name:
                continue

            attrs: dict = {}
            # Structured name -> given/family, useful for alias generation.
            n = _val(card, "n")
            given = getattr(n, "given", "") if n else ""
            if n:
                attrs["family_name"] = getattr(n, "family", "")
                attrs["given_name"] = given

            org = _val(card, "org")
            if org:
                attrs["org"] = org[0] if isinstance(org, list) else org
            if _val(card, "title"):
                attrs["title"] = _val(card, "title")
            # Emails / phones can repeat.
            emails = [e.value for e in card.contents.get("email", [])]
            phones = [t.value for t in card.contents.get("tel", [])]
            if emails:
                attrs["emails"] = emails
            if phones:
                attrs["phones"] = phones
            if _val(card, "note"):
                attrs["note"] = _val(card, "note")
            if _val(card, "bday"):
                attrs["birthday"] = _val(card, "bday")

            aliases = [full_name]
            if given:
                aliases.append(given)          # "Jeff" resolves to "Jeff Torres"
            aliases += emails                  # email is a strong resolution key

            yield Entity(
                kind="person",
                name=full_name,
                aliases=aliases,
                attributes=attrs,
                source_refs=[f"contacts:{self.source.name}"],
            )
