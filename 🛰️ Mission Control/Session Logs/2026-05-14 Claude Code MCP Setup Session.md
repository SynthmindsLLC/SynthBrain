---
created: 2026-05-14
updated: 2026-05-14
tags:
  - claude-code
  - mcp
  - skills
  - infrastructure
  - setup
type: Documentation
subtype: Session Log
---

# Claude Code MCP & Skills Setup Session

**Date:** May 14, 2026
**Session:** `session_01R2ZMequazSWYDv6k9VCav8`
**Branch:** `claude/setup-mcp-servers-08CN6`
**PR:** [#1](https://github.com/SynthmindsLLC/SynthBrain/pull/1)

---

## Objective

Fully outfit Claude Code with MCP server connections and skills for website creation, software engineering, marketing, and operations -- including a dedicated PBTV (Plants by the Village) e-commerce stack.

---

## What Was Built

### Phase 1: Core MCP Servers & Config

**8 CLI MCP servers** added via `.mcp.json`:

| Server | Package | Purpose |
|--------|---------|---------|
| Playwright | `@playwright/mcp@latest` | Browser automation & testing |
| Memory | `@modelcontextprotocol/server-memory` | Persistent knowledge graph across sessions |
| Context7 | `@upstash/context7-mcp@latest` | Live library documentation fetching |
| 21st.dev Magic | `@21st-dev/magic@latest` | React/TS component generation from natural language |
| Google Stitch | `@_davideast/stitch-mcp` | Gemini-powered UI design generation |
| Nano Banana | `mcp-image` | Image generation via Gemini Flash/Pro |
| Chrome DevTools | `@anthropic/chrome-devtools-mcp` | Live Chrome tab interaction |
| Mem.ai | `mcp-mem` (Python/uvx) | Knowledge vault -- notes and collections |

**Project files created:**
- **`CLAUDE.md`** -- Project instructions with Mem.ai as central knowledge vault, all 37 servers documented, env vars listed
- **`🛠 The Workshop/Tools Documentation/Claude Code MCP Server Reference.md`** -- Comprehensive 400+ line reference doc cataloging all servers with tools, use cases, workflow recipes, and configuration reference

**UI/UX Pro Max Skill** installed at `.claude/skills/ui-ux-pro-max/` -- 67 UI styles, 161 color palettes, 57 font pairings, 161 industry rules across 15 tech stacks.

### Phase 2: PBTV E-commerce Stack

**8 additional CLI MCP servers** for the Plants by the Village business:

| Server | Package | Type |
|--------|---------|------|
| Shopify | `shopify-mcp` | Community |
| Square POS | `square-mcp-server` | **Official (Block)** |
| ShipStation | `@iflow-mcp/shipstation-mcp-shipstation-api` | Community |
| Etsy | `@iflow-mcp/dynamicendpoints-etsy-mcp` | Community |
| Klaviyo | `klaviyo-mcp` | Community |
| Instagram DM | `mcp-instagram-dm` | Community |
| Calendly | `calendly-cli` | Community (40 tools) |
| Stripe | `@stripe/mcp` | **Official (Stripe)** |

**4 services without MCP servers** (workarounds documented):
- Palmstreet -- use Playwright browser automation
- Circle.so -- REST API available for custom MCP wrapper
- Tidio -- REST API available for custom MCP wrapper
- Later/Planoly -- use Instagram native Content Publishing API

**PBTV Shopify Flow Automation Guide** saved to `00 - ⚙ Work/Clients/PBTV/`:
- 10 core workflows with exact Shopify Sidekick prompts
- 5 bonus flows
- 4-week activation schedule
- Tech stack cost breakdown

### Phase 3: Skills Installation

**187 skills** installed from 7 major collections via `npx skills add`:

| Collection | Skills | Highlights |
|-----------|--------|-----------|
| `anthropics/skills` | 13 | PDF, DOCX, PPTX, XLSX, frontend-design, mcp-builder |
| `vercel-labs/agent-skills` | 7 | React best practices, web design, Vercel deploy |
| `coreyhaines31/marketingskills` | 45 | Copywriting, SEO audit, paid ads, CRO, launch strategy |
| `aaron-he-zhu/seo-geo-claude-skills` | 20 | SEO/GEO keyword research, rank tracking, schema markup |
| `trailofbits/skills` | 35+ | Semgrep, CodeQL, supply chain, smart contract security |
| `alirezarezvani/claude-skills` | 235 | Engineering, debugging, finance, RevOps, stress testing |
| `tfriedel/claude-office-skills` | 4 | PPTX, DOCX, XLSX, PDF creation |

Plus `find-skills` installed globally for discovering more skills.

### Phase 4: Skill Codex Dashboard

**`skill-codex.html`** -- Self-contained RPG-style dashboard:
- Skill cards with rarity system (Legendary/Epic/Rare/Uncommon/Common)
- XP progression bar with level system
- D3.js force-directed graph showing skill relationships by category
- MCP Arsenal view with all 37 servers
- Sidebar filtering, search, and detail modals
- Dark theme with retro scanline aesthetic

**Supporting data:**
- `.agents/skills-catalog.json` -- 188 skills cataloged with metadata
- `.agents/build-catalog.py` -- Regeneration script

---

## Final Totals

| Category | Count |
|----------|-------|
| MCP Servers (Web UI) | 21 |
| MCP Servers (CLI) | 16 |
| **Total MCP Servers** | **37** |
| Skills (installed) | 188 |
| Commits | 7 |

---

## Files Created/Modified

| File | Action |
|------|--------|
| `.mcp.json` | Created -- 16 CLI MCP server configs |
| `CLAUDE.md` | Created -- Project instructions |
| `🛠 The Workshop/Tools Documentation/Claude Code MCP Server Reference.md` | Created -- Full server catalog |
| `00 - ⚙ Work/Clients/PBTV/PBTV Shopify Flow Automation Guide.md` | Created -- 10 workflows + 5 bonus |
| `.claude/skills/ui-ux-pro-max/` | Created -- Design skill (SKILL.md + data + scripts) |
| `.agents/skills/` | Created -- 187 skill directories |
| `.agents/skills-catalog.json` | Created -- Skills metadata catalog |
| `.agents/build-catalog.py` | Created -- Catalog regeneration script |
| `skill-codex.html` | Created -- RPG dashboard |
| `skills-lock.json` | Created -- Skills lockfile |

---

## Environment Variables Required

```bash
# Design & Dev
export TWENTY_FIRST_API_KEY="your-21st-dev-key"
export GEMINI_API_KEY="your-gemini-api-key"
export MEM_API_KEY="your-mem-ai-api-key"

# PBTV / E-commerce
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

**Google Stitch** requires interactive OAuth: `npx @_davideast/stitch-mcp init`

---

## Outstanding Items

1. **Mem.ai push** -- PBTV Shopify Flow doc needs to be pushed to Mem.ai (MCP server didn't connect in web environment; use curl or local CLI)
2. **Merge PR #1** -- All changes are on `claude/setup-mcp-servers-08CN6`, ready to merge
3. **vibecode-cli** -- Investigated but is a cloud deployment platform, not a skills tool; evaluate separately if needed

---

## Key Insights from Research

- **Skills > MCP for token efficiency** (~50 tokens header vs 5.7K+ per MCP server)
- **`npx skills find`** discovers new skills interactively
- **Pre-define subagents** in `.claude/agents/` for consistent results
- **Keep CLAUDE.md under 500 lines** -- every session loads it
- **Browse skills at skills.sh** -- leaderboard of top 200 skills
