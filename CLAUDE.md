# SynthBrain

Knowledge base for **Synthminds LLC** -- AI, content creation, product development, and education. Powered by **Mem.ai** as the central knowledge vault for all projects and processes.

## Repository Structure

```
00 - ⚙ Work/              → Client projects (Verizon, YU, ANVL, etc.)
01 - 🎥 Commercial Hub/    → YouTube, Synaptic Labs, content workflows
02 - 🧙 Learning Lab/      → Courses (CS50, Uplimit, YU), course construction
03 - 🔬 R&D/               → AI research, math/comp sci, tech docs
04 - 🤖 Prompts/           → AI prompt engineering library
05 - 🌐 Organization/      → Team coordination, partnerships, tasks
🛠 The Workshop/            → Tools docs, programming languages, Synthsidian
🛰️ Mission Control/        → Strategic projects, roadmaps, templates
```

## Conventions

- **Content format:** Markdown with YAML frontmatter (`created`, `updated`, `tags`, `type`, `subtype`)
- **File naming:** Emoji prefixes on folders match the organizational system
- **Attachments:** Store in `_attachments/` subdirectories within each section
- **Templates:** Located in `🛰️ Mission Control/Templates/`

## Knowledge Vault

**Mem.ai** is the central knowledge vault for Synthminds. Use the Mem.ai MCP server (already connected) for:
- Storing and retrieving project documentation, meeting notes, and decisions
- Searching across all organizational knowledge
- Creating and updating notes programmatically
- Building the persistent knowledge graph for all Synthminds projects

## MCP Servers

This project has 37 MCP server connections across two surfaces:

- **Web UI (21 servers):** GitHub, Vercel, Cloudflare, Figma, Canva, Sentry, Notion, Slack, Gmail, Google Calendar, Granola, Gamma, Eraser, Exa, Hugging Face, 2x Mermaid, Domain Checker, Tax Tool, SFDR, Job Search
- **CLI via `.mcp.json` (16 servers):** Playwright, Memory, Context7, 21st.dev Magic, Google Stitch, Nano Banana (mcp-image), Chrome DevTools, Mem.ai, Shopify, Square POS, ShipStation, Etsy, Klaviyo, Instagram DM, Calendly, Stripe

Full reference: `🛠 The Workshop/Tools Documentation/Claude Code MCP Server Reference.md`

### Required Environment Variables (for CLI servers)

```bash
# Design & Dev tools
export TWENTY_FIRST_API_KEY="your-21st-dev-key"
export GEMINI_API_KEY="your-gemini-api-key"
export MEM_API_KEY="your-mem-ai-api-key"
# Google Stitch: run `npx @_davideast/stitch-mcp init` for OAuth setup

# PBTV / E-commerce stack
export SHOPIFY_ACCESS_TOKEN="shpat_xxxxx"
export SHOPIFY_STORE_DOMAIN="your-store.myshopify.com"
export SQUARE_ACCESS_TOKEN="EAAAxxxxxxx"
export SHIPSTATION_API_KEY="your-key"
export SHIPSTATION_API_SECRET="your-secret"
export ETSY_API_KEY="your-etsy-key"
export KLAVIYO_API_KEY="pk_xxxxxxxx"
export INSTAGRAM_ACCESS_TOKEN="your-meta-graph-token"
export CALENDLY_API_KEY="your-calendly-pat"
export STRIPE_SECRET_KEY="sk_test_xxxxx"
```

## Skills

- **UI/UX Pro Max** installed at `.claude/skills/ui-ux-pro-max/` -- auto-generates design systems with 67 UI styles, 161 palettes, 57 font pairings

## Working With This Repo

- This is a documentation/knowledge repo, not a code project. No build system or CI/CD.
- Git is used for backup (`vault backup: YYYY-MM-DD HH:MM:SS` commit format)
- When creating new documentation, follow existing frontmatter patterns
- Use Mem.ai as the primary knowledge store; this repo serves as the versioned backup
