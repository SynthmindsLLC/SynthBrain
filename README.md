# SynthBrain

Knowledge base for **Synthminds LLC** — AI, content creation, product development, and education. **Mem.ai** is the central knowledge vault for all projects and processes; this repo is transitioning into the **Mem.ai connector codebase** (per [`CLAUDE.md`](./CLAUDE.md)).

## Quick links

- [`CLAUDE.md`](./CLAUDE.md) — agentic coding rules + project overlay (migration plan, conventions, decisions).
- [`.mcp.json`](./.mcp.json) — 16 CLI MCP server configurations.
- [`🛠 The Workshop/Tools Documentation/Claude Code MCP Server Reference.md`](./🛠%20The%20Workshop/Tools%20Documentation/Claude%20Code%20MCP%20Server%20Reference.md) — full catalog of all 37 MCP servers, tools, and workflow recipes.
- [`🛰️ Mission Control/Session Logs/`](./🛰️%20Mission%20Control/Session%20Logs/) — Claude Code session logs.
- [`skill-codex.html`](./skill-codex.html) — RPG-style dashboard for the 187 installed skills.

## Repository Structure

```
00 - ⚙ Work/              → Client projects (Verizon, YU, ANVL, PBTV, etc.)
01 - 🎥 Commercial Hub/    → YouTube, Synaptic Labs, content workflows
02 - 🧙 Learning Lab/      → Courses (CS50, Uplimit, YU), course construction
03 - 🔬 R&D/               → AI research, math/comp sci, tech docs
04 - 🤖 Prompts/           → AI prompt engineering library
05 - 🌐 Organization/      → Team coordination, partnerships, tasks
🛠 The Workshop/            → Tools docs, programming languages, Synthsidian
🛰️ Mission Control/        → Strategic projects, roadmaps, templates, session logs
.agents/skills/             → 187 installed skills (catalog: .agents/skills-catalog.json)
.claude/skills/             → Local Claude skills (e.g. ui-ux-pro-max)
```

## Conventions

- **Content format:** Markdown with YAML frontmatter (`created`, `updated`, `tags`, `type`, `subtype`).
- **File naming:** Emoji prefixes on folders match the organizational system.
- **Attachments:** Store in `_attachments/` subdirectories within each section.
- **Templates:** Located in `🛰️ Mission Control/Templates/`.

## Knowledge Vault — Mem.ai

**Mem.ai** is the canonical knowledge store. Use the Mem.ai MCP server (already connected) for:

- Storing and retrieving project documentation, meeting notes, and decisions.
- Searching across all organizational knowledge.
- Creating and updating notes programmatically.
- Building the persistent knowledge graph for all Synthminds projects.

Vault content in this repo is being migrated to Mem.ai per the phased plan in [`CLAUDE.md`](./CLAUDE.md). Until that's done, **Mem.ai is the source of truth for active knowledge work**; this repo holds the legacy vault and the connector code.

## MCP Servers

37 MCP server connections across two surfaces:

- **Web UI (21 servers):** GitHub, Vercel, Cloudflare, Figma, Canva, Sentry, Notion, Slack, Gmail, Google Calendar, Granola, Gamma, Eraser, Exa, Hugging Face, 2× Mermaid, Domain Checker, Tax Tool, SFDR, Job Search.
- **CLI via `.mcp.json` (16 servers):** Playwright, Memory, Context7, 21st.dev Magic, Google Stitch, Nano Banana (mcp-image), Chrome DevTools, Mem.ai, Shopify, Square POS, ShipStation, Etsy, Klaviyo, Instagram DM, Calendly, Stripe.

Full reference (including required env vars, OAuth steps, and workflow recipes): [`🛠 The Workshop/Tools Documentation/Claude Code MCP Server Reference.md`](./🛠%20The%20Workshop/Tools%20Documentation/Claude%20Code%20MCP%20Server%20Reference.md).

## Skills

187 skills installed under `.agents/skills/` from 7 collections (Anthropic, Vercel Labs, Marketing, SEO/GEO, Trail of Bits, Alireza Rezvani, Office). Plus the **UI/UX Pro Max** design intelligence skill at `.claude/skills/ui-ux-pro-max/` (67 styles, 161 palettes, 57 font pairings, 13 stacks). Browse interactively via [`skill-codex.html`](./skill-codex.html).

## Working with this repo

- This repo is in transition: legacy Obsidian vault → Mem.ai-backed connector codebase. See the migration plan in [`CLAUDE.md`](./CLAUDE.md).
- Vault commits historically used the format `vault backup: YYYY-MM-DD HH:MM:SS`. Going forward, follow **Conventional Commits** (per the global rules in [`CLAUDE.md`](./CLAUDE.md)).
- New documentation: follow existing frontmatter patterns; prefer creating in Mem.ai if it's active knowledge work.
- Active migration branch: `claude/integrate-mem-ai-1ZuZJ`.
