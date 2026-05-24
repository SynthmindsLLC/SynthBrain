---
created: 2026-04-13
updated: 2026-04-13
tags:
  - tools
  - claude-code
  - mcp
  - infrastructure
type: Documentation
subtype: Reference
---

# Claude Code MCP Server Reference

Synthminds runs **39 MCP servers** across two surfaces -- the Claude Code web UI (21 OAuth-managed servers) and the CLI via `.mcp.json` (18 local servers). This document catalogs every server, its tools, and how they fit into our workflows.

**Mem.ai** is the central knowledge vault. Use it for storing and retrieving all project documentation, meeting notes, and decisions.

---

## Quick Reference

| # | Server | Category | Interface | Key Capabilities |
|---|--------|----------|-----------|-----------------|
| 1 | GitHub | Engineering | Web UI | Repos, PRs, issues, code search, security scanning |
| 2 | Vercel | Web/Deploy | Web UI | Deploy, projects, build/runtime logs, domain checking |
| 3 | Cloudflare | Web/Infra | Web UI | Workers, D1, KV, R2, Hyperdrive |
| 4 | Figma | Design | Web UI | Design context, screenshots, code connect, variables |
| 5 | Canva | Design | Web UI | Generate/edit designs, export, brand kits |
| 6 | Sentry | Engineering | Web UI | Error monitoring, replays, Seer AI analysis |
| 7 | Notion | Operations | Web UI | Pages, databases, views, teams |
| 8 | Slack | Operations | Web UI | Messaging, channels, search, canvases |
| 9 | Gmail | Operations | Web UI | Email read/draft/search, labels |
| 10 | Google Calendar | Operations | Web UI | Events, scheduling, free time |
| 11 | Granola | Operations | Web UI | Meeting transcripts and notes |
| 12 | Gamma | Marketing | Web UI | Presentations, documents, webpages |
| 13 | Eraser | Marketing | Web UI | Diagrams, docs, tables, boards |
| 14 | Exa | Engineering | Web UI | Web search and page fetching |
| 15 | Hugging Face | Engineering | Web UI | ML models, papers, docs, spaces |
| 16 | Mermaid | Marketing | Web UI | Diagram rendering and validation |
| 17 | Domain Checker | Web | Web UI | Domain availability and suggestions |
| 18 | Tax Tool | Specialized | Web UI | Tax calculations and PDFs |
| 19 | SFDR | Specialized | Web UI | Securities fund compliance |
| 20 | Job Search | Specialized | Web UI | Job searching |
| 21 | Playwright | Engineering | CLI | Browser automation, testing, screenshots |
| 22 | Memory | Engineering | CLI | Persistent knowledge graph |
| 23 | Context7 | Engineering | CLI | Up-to-date library documentation |
| 24 | 21st.dev Magic | Design | CLI | React/TS component generation, logo search |
| 25 | Google Stitch | Design | CLI | Gemini UI design generation, screen-to-code |
| 26 | Nano Banana | Design | CLI | Image generation via Gemini Flash/Pro |
| 27 | Chrome DevTools | Engineering | CLI | Live Chrome tab interaction |
| 28 | Mem.ai | Operations | CLI | Knowledge vault -- notes and collections |
| 29 | Mermaid (2nd) | Marketing | Web UI | Diagram validation (overlaps with #16) |
| 30 | Shopify | E-commerce | CLI | Products, orders, inventory, customers (GraphQL Admin API) |
| 31 | Square POS | E-commerce | CLI | In-store transactions, payments, catalog, inventory (Official) |
| 32 | ShipStation | E-commerce | CLI | Shipping labels, tracking, multi-channel orders |
| 33 | Etsy | E-commerce | CLI | Listings, orders, shops, reviews, shipping |
| 34 | Klaviyo | E-commerce | CLI | Email campaigns, automations, segments, SMS |
| 35 | Instagram DM | E-commerce | CLI | Read inbox, send messages, conversations |
| 36 | Calendly | E-commerce | CLI | Events, scheduling, availability, webhooks (40 tools) |
| 37 | Stripe | E-commerce | CLI | Payments, subscriptions, invoices, refunds (Official) |
| 38 | Google Drive | Ingestion | CLI | Drive, Docs, Sheets, Slides, Calendar (60+ tools) |
| 39 | Filesystem | Ingestion | CLI | Local file reading, directory listing, search |

---

## Website Creation & Design

### Figma
- **Interface:** Web UI (OAuth)
- **Tools:** `use_figma`, `get_design_context`, `get_screenshot`, `get_metadata`, `get_figjam`, `get_variable_defs`, `search_design_system`, `create_design_system_rules`, `add_code_connect_map`, `get_code_connect_map`, `get_code_connect_suggestions`, `get_context_for_code_connect`, `send_code_connect_mappings`, `generate_diagram`, `create_new_file`, `whoami`
- **Use Cases:** Extract design specs from Figma files for code implementation, screenshot components for review, map Figma components to codebase components via Code Connect, search design tokens and variables, generate diagrams in FigJam
- **Tip:** Use `get_code_connect_suggestions` before implementing a new component to check if a Figma mapping already exists. Pair with Vercel for a design-to-deploy pipeline.

### Canva
- **Interface:** Web UI (OAuth)
- **Tools:** `generate-design`, `generate-design-structured`, `get-design`, `get-design-content`, `get-design-pages`, `get-design-thumbnail`, `get-assets`, `get-export-formats`, `get-presenter-notes`, `export-design`, `import-design-from-url`, `create-design-from-candidate`, `start-editing-transaction`, `perform-editing-operations`, `commit-editing-transaction`, `cancel-editing-transaction`, `resize-design`, `merge-designs`, `upload-asset-from-url`, `list-brand-kits`, `create-folder`, `list-folder-items`, `move-item-to-folder`, `search-designs`, `search-folders`, `comment-on-design`, `list-comments`, `list-replies`, `reply-to-comment`, `request-outline-review`, `resolve-shortlink`
- **Use Cases:** Generate marketing assets from prompts, create social media graphics, build presentation decks, maintain brand consistency via brand kits, bulk export designs
- **Tip:** Use `list-brand-kits` first to ensure generated designs match Synthminds branding.

### Vercel
- **Interface:** Web UI (OAuth)
- **Tools:** `deploy_to_vercel`, `list_projects`, `get_project`, `list_deployments`, `get_deployment`, `get_deployment_build_logs`, `get_runtime_logs`, `list_teams`, `check_domain_availability_and_price`, `get_access_to_vercel_url`, `web_fetch_vercel_url`, `search_vercel_documentation`, `list_toolbar_threads`, `get_toolbar_thread`, `reply_to_toolbar_thread`, `edit_toolbar_message`, `add_toolbar_reaction`, `change_toolbar_thread_resolve_status`
- **Use Cases:** Deploy websites, check build/runtime logs for debugging, check domain availability, manage toolbar feedback threads
- **Tip:** After deploying, use Playwright to run automated browser tests against the live URL.

### Cloudflare
- **Interface:** Web UI (OAuth)
- **Tools:** `accounts_list`, `set_active_account`, `workers_list`, `workers_get_worker`, `workers_get_worker_code`, `d1_databases_list`, `d1_database_create`, `d1_database_get`, `d1_database_delete`, `d1_database_query`, `kv_namespaces_list`, `kv_namespace_create`, `kv_namespace_get`, `kv_namespace_update`, `kv_namespace_delete`, `r2_buckets_list`, `r2_bucket_create`, `r2_bucket_get`, `r2_bucket_delete`, `hyperdrive_configs_list`, `hyperdrive_config_get`, `hyperdrive_config_edit`, `hyperdrive_config_delete`, `search_cloudflare_documentation`, `migrate_pages_to_workers_guide`
- **Use Cases:** Manage Workers for serverless functions, D1 for SQL databases, KV for key-value storage, R2 for object storage, Hyperdrive for database connection pooling
- **Tip:** Use D1 for lightweight databases and R2 for file/image storage. Pair with Vercel for frontend + Cloudflare for backend infrastructure.

### Domain Checker
- **Interface:** Web UI
- **Tools:** `domains_check_availability`, `domains_suggest`
- **Use Cases:** Check if a domain is available before launching a project, get domain name suggestions

### 21st.dev Magic
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@21st-dev/magic@latest`
- **Env var:** `TWENTY_FIRST_API_KEY`
- **Tools:** `21st_magic_component_builder`, `21st_magic_component_inspiration`, `21st_magic_component_refiner`, `logo_search`
- **Use Cases:** Generate production-ready React/TypeScript UI components from natural language descriptions, browse component inspiration from the 21st.dev library, refine existing components, search for company logos in JSX/TSX/SVG format
- **Tip:** Describe the component you need in plain English and 21st.dev generates production code. Use `logo_search` for instant branded logos.

### Google Stitch
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@_davideast/stitch-mcp`
- **Auth:** Google Cloud OAuth -- run `npx @_davideast/stitch-mcp init` first
- **Tools:** `build_site` (maps screens to routes, returns design HTML), `get_screen_code` (retrieves screen HTML), `get_screen_image` (screenshots as base64), plus upstream Stitch proxy tools
- **Use Cases:** Generate UI designs from text prompts using Gemini 2.5 Pro, extract clean HTML/CSS from generated screens, create multi-page site layouts
- **Tip:** Use Stitch for initial design generation, then 21st.dev for component refinement.

### Nano Banana (mcp-image)
- **Interface:** CLI (`.mcp.json`)
- **Package:** `mcp-image`
- **Env var:** `GEMINI_API_KEY` (free from Google AI Studio)
- **Tools:** `generate_image`
- **Quality presets:** `fast` (Gemini 3.1 Flash -- quick iterations), `balanced` (Flash + Thinking), `quality` (Gemini 3 Pro -- maximum fidelity)
- **Use Cases:** Generate hero images, product mockups, social media graphics, blog illustrations, icons
- **Tip:** Use `fast` for prototyping, `quality` for final assets. Pair with Canva for post-processing.

---

## Software Engineering

### GitHub
- **Interface:** Web UI (OAuth)
- **Tools:** `get_me`, `create_repository`, `fork_repository`, `create_branch`, `list_branches`, `list_tags`, `get_tag`, `list_commits`, `get_commit`, `get_file_contents`, `create_or_update_file`, `delete_file`, `push_files`, `search_code`, `search_repositories`, `search_users`, `list_issues`, `issue_read`, `issue_write`, `list_issue_types`, `sub_issue_write`, `add_issue_comment`, `search_issues`, `get_label`, `list_pull_requests`, `pull_request_read`, `create_pull_request`, `update_pull_request`, `update_pull_request_branch`, `merge_pull_request`, `search_pull_requests`, `pull_request_review_write`, `add_comment_to_pending_review`, `add_reply_to_pull_request_comment`, `resolve_review_thread`, `unresolve_review_thread`, `enable_pr_auto_merge`, `disable_pr_auto_merge`, `request_copilot_review`, `subscribe_pr_activity`, `unsubscribe_pr_activity`, `list_releases`, `get_latest_release`, `get_release_by_tag`, `get_teams`, `get_team_members`, `run_secret_scanning`
- **Use Cases:** Full repository management, PR workflows, issue tracking, code search, security scanning, release management

### Sentry
- **Interface:** Web UI (OAuth)
- **Tools:** `whoami`, `find_organizations`, `find_projects`, `find_teams`, `find_releases`, `search_issues`, `search_issue_events`, `search_events`, `get_issue_tag_values`, `get_event_attachment`, `get_replay_details`, `get_profile_details`, `get_sentry_resource`, `analyze_issue_with_seer`
- **Use Cases:** Monitor production errors, investigate issue details, watch session replays, use Seer AI for root cause analysis
- **Tip:** After deploying via Vercel, check Sentry for any new errors. Use `analyze_issue_with_seer` for AI-powered debugging.

### Exa
- **Interface:** Web UI (OAuth)
- **Tools:** `web_search_exa`, `web_fetch_exa`
- **Use Cases:** Research libraries, find documentation, fetch web page content for analysis

### Hugging Face
- **Interface:** Web UI (OAuth)
- **Tools:** `hf_whoami`, `hf_hub_query`, `hf_doc_search`, `hf_doc_fetch`, `hub_repo_search`, `hub_repo_details`, `paper_search`, `space_search`, `dynamic_space`
- **Use Cases:** Find ML models, search research papers, browse model documentation, explore Hugging Face Spaces
- **Tip:** Use `paper_search` for AI research and `hub_repo_search` to find pre-trained models.

### Playwright
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@playwright/mcp@latest`
- **Tools:** `browser_navigate`, `browser_click`, `browser_fill_form`, `browser_type`, `browser_press_key`, `browser_select_option`, `browser_hover`, `browser_drag`, `browser_take_screenshot`, `browser_snapshot`, `browser_evaluate`, `browser_run_code`, `browser_file_upload`, `browser_handle_dialog`, `browser_tabs`, `browser_close`, `browser_navigate_back`, `browser_resize`, `browser_console_messages`, `browser_network_requests`, `browser_wait_for`
- **Use Cases:** Automated browser testing, visual regression testing, form submission testing, accessibility audits, screenshot comparisons against Figma designs, end-to-end user flow verification
- **Tip:** After Vercel deploys, use Playwright to navigate the live URL and verify the site works. Compare screenshots against Figma designs.

### Memory
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@modelcontextprotocol/server-memory`
- **Tools:** `create_entities`, `add_observations`, `create_relations`, `delete_entities`, `delete_observations`, `delete_relations`, `open_nodes`, `read_graph`, `search_nodes`
- **Use Cases:** Persistent knowledge graph that survives across sessions. Store project context, user preferences, codebase patterns, architectural decisions, client details.
- **Tip:** Create entities for each project and add observations as you learn things. This is Claude's "working memory" -- complements Mem.ai (the long-term vault).

### Context7
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@upstash/context7-mcp@latest`
- **Tools:** `resolve-library-id`, `query-docs`
- **Use Cases:** Fetch current documentation for any library, framework, or SDK. Prevents hallucinated or deprecated API calls.
- **Tip:** Use this whenever working with any library -- even well-known ones like React, Next.js, Tailwind. Training data may not reflect recent changes.

### Chrome DevTools
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@anthropic/chrome-devtools-mcp`
- **Use Cases:** Open Chrome tabs, take screenshots, click elements, inspect the DOM in a live browser
- **Tip:** Use for debugging live pages when Playwright is overkill. Great for quick visual checks.

---

## Marketing & Content

### Gamma
- **Interface:** Web UI (OAuth)
- **Tools:** `generate`, `get_generation_status`, `get_themes`, `get_folders`, `read_gamma`
- **Use Cases:** Generate AI-powered presentations, documents, webpages, and social posts with themes. Read existing Gamma content.
- **Note:** Cannot edit existing Gammas -- only generate new ones. Edits must be done in the Gamma editor.

### Eraser
- **Interface:** Web UI (OAuth)
- **Tools:** `diagram_create`, `diagram_get_dsl`, `doc_create`, `doc_get`, `doc_update`, `table_create`, `table_list_rows`, `table_sync_rows`, `board_list_items`, `context_explore`, `context_get`, `image_get_data`, `image_get_url`
- **Use Cases:** Create architecture diagrams, technical docs, project boards, data tables. Get diagram DSL for version control.

### Mermaid (x2)
- **Interface:** Web UI
- **Tools:** `validate_and_render_mermaid_diagram`, `get_mermaid_syntax_document`, `search_mermaid_icons`, `get_diagram_summary`, `get_diagram_title`, `list_tools`
- **Use Cases:** Render and validate Mermaid diagrams, search for icons, get syntax help
- **Note:** Two Mermaid servers are connected (57ae and f2c6). Both can validate diagrams. You may only need one.

---

## Operations & Communication

### Slack
- **Interface:** Web UI (OAuth)
- **Tools:** `slack_send_message`, `slack_send_message_draft`, `slack_schedule_message`, `slack_read_channel`, `slack_read_thread`, `slack_read_user_profile`, `slack_search_channels`, `slack_search_public`, `slack_search_public_and_private`, `slack_search_users`, `slack_create_canvas`, `slack_read_canvas`, `slack_update_canvas`
- **Use Cases:** Send team updates, read channel history, search conversations, create/update Slack canvases for documentation

### Gmail
- **Interface:** Web UI (OAuth)
- **Tools:** `gmail_get_profile`, `gmail_search_messages`, `gmail_read_message`, `gmail_read_thread`, `gmail_create_draft`, `gmail_list_drafts`, `gmail_list_labels`
- **Use Cases:** Search emails, read threads, draft responses, manage labels

### Google Calendar
- **Interface:** Web UI (OAuth)
- **Tools:** `gcal_list_calendars`, `gcal_list_events`, `gcal_get_event`, `gcal_create_event`, `gcal_update_event`, `gcal_delete_event`, `gcal_find_meeting_times`, `gcal_find_my_free_time`, `gcal_respond_to_event`
- **Use Cases:** View schedule, create events, find free time for meetings, manage RSVPs

### Granola
- **Interface:** Web UI (OAuth)
- **Tools:** `get_meetings`, `list_meetings`, `list_meeting_folders`, `get_meeting_transcript`, `query_granola_meetings`
- **Use Cases:** Pull meeting transcripts, search across meeting history, extract action items from meetings

### Notion
- **Interface:** Web UI (OAuth)
- **Tools:** `notion-search`, `notion-fetch`, `notion-create-pages`, `notion-update-page`, `notion-duplicate-page`, `notion-move-pages`, `notion-create-database`, `notion-create-view`, `notion-update-view`, `notion-update-data-source`, `notion-create-comment`, `notion-get-comments`, `notion-get-teams`, `notion-get-users`
- **Use Cases:** Search across Notion workspace, create/update pages and databases, manage views, add comments

### Mem.ai
- **Interface:** CLI (`.mcp.json`)
- **Package:** `mcp-mem` (Python/uvx)
- **Env var:** `MEM_API_KEY`
- **Tools:** `mem_it` (auto-organize content), `create_note`, `read_note`, `delete_note`, `create_collection`, `delete_collection`
- **Use Cases:** Central knowledge vault for all Synthminds projects. Store meeting notes, project documentation, decisions, research findings. Search across all organizational knowledge.
- **Tip:** Use `mem_it` to quickly save content with AI-powered organization. Use collections to group related notes by project.

---

## Specialized

### Tax Tool
- **Interface:** Web UI
- **Tools:** `calculate_tax`, `check_tax`, `generate_tax_pdf_tool`, `get_tax_pdf_tool`, `tax_jurisdictions`, `tax_namespaces`, `tax_namespace_schema`, `tax_years`, `tax_simple_return`, `generate_uuid_v5`

### SFDR
- **Interface:** Web UI
- **Tools:** `sfdr20_check`, `sfdr20_check_by_isin`, `sfdr20_check_by_query`, `sfdr20_assess_fund_name`, `interpret_sfdr20_result`, `search_securities`

### Job Search
- **Interface:** Web UI
- **Tools:** `search_jobs`

---

## E-commerce & PBTV Stack

### Shopify
- **Interface:** CLI (`.mcp.json`)
- **Package:** `shopify-mcp`
- **Env vars:** `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_STORE_DOMAIN`
- **Use Cases:** Manage PBTV.shop -- products, orders, inventory, customers via GraphQL Admin API. Create products, update inventory counts, fulfill orders, search customers, manage collections.
- **Tip:** Pair with Shopify Flow automations (see PBTV Shopify Flow Automation Guide). Use for bulk product updates and inventory management that Flow can't handle.

### Square POS (Official)
- **Interface:** CLI (`.mcp.json`)
- **Package:** `square-mcp-server` (published by Block)
- **Env var:** `SQUARE_ACCESS_TOKEN`
- **Use Cases:** In-store transactions, payment processing, catalog management, inventory tracking, customer profiles, location management. Square is the source of truth for the in-store catalog.
- **Tip:** Inventory syncs between Square and Shopify via Thrive/DPL. Use this MCP to check real-time in-store inventory and daily sales.

### ShipStation
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@iflow-mcp/shipstation-mcp-shipstation-api`
- **Env vars:** `SHIPSTATION_API_KEY`, `SHIPSTATION_API_SECRET`
- **Use Cases:** Auto-import orders from Shopify + Palmstreet, print shipping labels, track shipments, manage multi-channel orders. Push tracking numbers back to Shopify/Etsy.

### Etsy
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@iflow-mcp/dynamicendpoints-etsy-mcp`
- **Env var:** `ETSY_API_KEY`
- **Use Cases:** Manage Etsy listings, view orders, respond to reviews, handle shipping profiles. Sync inventory with Shopify via DPL integration.
- **Tip:** Also consider `listing-doctor-mcp` for Etsy SEO optimization with 100-point listing scoring.

### Klaviyo
- **Interface:** CLI (`.mcp.json`)
- **Package:** `klaviyo-mcp`
- **Env var:** `KLAVIYO_API_KEY`
- **Use Cases:** Email/SMS marketing -- manage campaigns, automations, segments, profiles, flows, metrics, templates. Powers PBTV's abandoned cart recovery, welcome series, VIP tagging, care emails, and review requests.
- **Tip:** Shopify Flow triggers Klaviyo events; Klaviyo handles the multi-step email sequences. Use this MCP to check campaign performance and manage segments.

### Instagram DM
- **Interface:** CLI (`.mcp.json`)
- **Package:** `mcp-instagram-dm`
- **Env var:** `INSTAGRAM_ACCESS_TOKEN` (Meta Graph API token)
- **Use Cases:** Read DM inbox, send messages, search conversations. Manage @plantsbythevillage customer interactions.
- **Note:** Requires a Facebook developer app with Instagram Graph API access. Posts/Reels/Stories are managed through Later or the Instagram app directly.

### Calendly
- **Interface:** CLI (`.mcp.json`)
- **Package:** `calendly-cli` (40 tools)
- **Env var:** `CALENDLY_API_KEY` (Personal Access Token)
- **Use Cases:** Manage consultation bookings, view upcoming events, check availability, manage event types, handle invitees, set up webhooks, configure routing forms.

### Stripe (Official)
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@stripe/mcp` (published by Stripe)
- **Env var:** `STRIPE_SECRET_KEY`
- **Use Cases:** Payment processing layer -- customers, products, prices, invoices, subscriptions, charges, payment intents, refunds, balance, payouts. Stripe is the payment backend for Shopify and potentially Circle/PBTV.app.

### Services Without MCP Servers

| Service | Status | Workaround |
|---------|--------|-----------|
| **Palmstreet** | No public API | Use Playwright for browser automation during live sales |
| **Circle.so** | REST API available | Custom MCP wrapper possible; manage PBTV.app community via API |
| **Tidio** | REST API available | Custom MCP wrapper possible; manage chatbot via API |
| **Later/Planoly** | No public API | Use Instagram native Content Publishing API for scheduling |

---

## Document Ingestion

### Google Drive (60+ tools)
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@piotr-agier/google-drive-mcp`
- **Env var:** `GOOGLE_DRIVE_OAUTH_CREDENTIALS` (path to OAuth keys JSON)
- **Tools:** `search`, `listFolder`, `listSharedDrives`, `readGoogleDoc` (markdown output), `readGoogleDocPaginated`, `getGoogleSheetContent`, `getGoogleSlidesContent`, `downloadFile`, `uploadFile`, `listComments`, plus full CRUD for Docs, Sheets, Slides, Calendar
- **Use Cases:** Ingest documents from Google Drive and Shared Drives into Mem.ai. Read Google Docs as markdown, extract Sheet data, pull Slides content.
- **Setup:** Create Google Cloud project, enable Drive + Docs + Sheets + Slides + Calendar APIs, create Desktop OAuth Client, place JSON at `~/.config/google-drive-mcp/gcp-oauth.keys.json`

### Local Filesystem
- **Interface:** CLI (`.mcp.json`)
- **Package:** `@modelcontextprotocol/server-filesystem`
- **Tools:** `read_text_file`, `read_media_file`, `read_multiple_files`, `list_directory`, `list_directory_with_sizes`, `directory_tree`, `search_files`, `get_file_info`, `write_file`, `edit_file`, `create_directory`, `move_file`, `list_allowed_directories`
- **Use Cases:** Ingest local markdown, text, and document files into Mem.ai. Scan directories for new content.
- **Note:** Restricted to explicitly allowed directories (configured in `.mcp.json` args). Claude Code already has built-in file reading, so this MCP is most useful for agent-driven batch ingestion.

### Ingestion Pipeline Reference

Full ingestion schema, tagging taxonomy, classification rules, and pipeline specs: [`🛰️ Mission Control/SynthBrain Ingestion & Tagging Schema.md`](../🛰️%20Mission%20Control/SynthBrain%20Ingestion%20%26%20Tagging%20Schema.md)

### Future Ingestion Sources

| Source | MCP Server | When |
|--------|-----------|------|
| Microsoft 365 | `@softeria/ms-365-mcp-server` (200+ tools) | When M365/OneDrive/SharePoint access is needed |
| Box | `box-mcp-server` | When Box integration is needed |

---

## Workflow Recipes

### Design-to-Deploy Pipeline
1. **Figma** `get_design_context` -- Extract design specs
2. **21st.dev** `21st_magic_component_builder` -- Generate React components
3. **Playwright** `browser_navigate` + `browser_take_screenshot` -- Test locally
4. **Vercel** `deploy_to_vercel` -- Deploy to production
5. **Playwright** `browser_navigate` -- Test the live deployment
6. **Sentry** `search_issues` -- Monitor for errors

### Meeting-to-Action Pipeline
1. **Granola** `get_meeting_transcript` -- Pull meeting transcript
2. **Claude** -- Extract action items and decisions
3. **Mem.ai** `create_note` -- Store decisions in knowledge vault
4. **Notion** `notion-create-pages` -- Create task pages
5. **Slack** `slack_send_message` -- Notify team
6. **Google Calendar** `gcal_create_event` -- Schedule follow-ups

### Content Creation Pipeline
1. **Exa** `web_search_exa` -- Research topic
2. **Claude** -- Draft content
3. **Nano Banana** `generate_image` -- Generate visuals
4. **Gamma** `generate` -- Create presentation
5. **Canva** `generate-design` -- Design social media assets
6. **Eraser** `diagram_create` -- Create technical diagrams

### Website from Scratch Pipeline
1. **Google Stitch** `build_site` -- Generate initial UI design via Gemini
2. **Figma** `get_design_context` -- Refine with Figma designs
3. **21st.dev** `21st_magic_component_builder` -- Generate components
4. **Context7** `query-docs` -- Get current framework docs
5. **Playwright** `browser_take_screenshot` -- Visual testing
6. **Vercel** `deploy_to_vercel` -- Ship it
7. **Cloudflare** `d1_database_create` -- Set up backend DB

### PBTV Order-to-Delivery Pipeline
1. **Shopify** -- New order comes in on PBTV.shop
2. **ShipStation** -- Auto-imports order, buy shipping label
3. **Klaviyo** -- Sends order confirmation + shipping notification
4. **Shopify** -- Mark as fulfilled with tracking number
5. **Klaviyo** -- 3 days post-delivery: send species-specific care guide
6. **Klaviyo** -- 14 days post-delivery: request product review

### PBTV Inventory Management Pipeline
1. **Square** -- Check in-store inventory (source of truth)
2. **Shopify** -- Sync online inventory (via Thrive/DPL)
3. **Etsy** -- Sync Etsy listings (via DPL Etsy Integration)
4. **Shopify Flow** -- Auto-alert at 3 units, auto-hide at 0
5. **Klaviyo** -- Waitlist notification when restocked

---

## Configuration Reference

### Web UI vs CLI

| Aspect | Web UI | CLI (`.mcp.json`) |
|--------|--------|-------------------|
| **Auth** | OAuth managed automatically | API keys via env vars |
| **Location** | Claude Code web settings | `.mcp.json` at repo root |
| **Best for** | SaaS integrations (Slack, Gmail, GitHub, etc.) | Local tools (Playwright, Memory, etc.) |
| **Token cost** | Same | Same |

### CLI `.mcp.json` Format

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@scope/package@latest"],
      "env": {
        "API_KEY": "${ENV_VAR_NAME}"
      }
    }
  }
}
```

### Required Environment Variables

| Variable | Server | How to get it |
|----------|--------|--------------|
| `TWENTY_FIRST_API_KEY` | 21st.dev Magic | https://21st.dev/magic/console |
| `GEMINI_API_KEY` | Nano Banana + Stitch | https://aistudio.google.com/app/apikey (free) |
| `MEM_API_KEY` | Mem.ai | Mem.ai account settings |
| Google Cloud OAuth | Google Stitch | Run `npx @_davideast/stitch-mcp init` |
| `SHOPIFY_ACCESS_TOKEN` | Shopify | Shopify Admin > Settings > Apps > Develop apps |
| `SHOPIFY_STORE_DOMAIN` | Shopify | e.g. `pbtv-shop.myshopify.com` |
| `SQUARE_ACCESS_TOKEN` | Square POS | Square Developer Dashboard |
| `SHIPSTATION_API_KEY` | ShipStation | ShipStation > Settings > API Keys |
| `SHIPSTATION_API_SECRET` | ShipStation | Same as above |
| `ETSY_API_KEY` | Etsy | Etsy Developer Portal |
| `KLAVIYO_API_KEY` | Klaviyo | Klaviyo > Account > Settings > API Keys (private key) |
| `INSTAGRAM_ACCESS_TOKEN` | Instagram DM | Meta Developer Portal (Graph API token) |
| `CALENDLY_API_KEY` | Calendly | Calendly > Integrations > Personal Access Tokens |
| `STRIPE_SECRET_KEY` | Stripe | Stripe Dashboard > Developers > API Keys |
| `GOOGLE_DRIVE_OAUTH_CREDENTIALS` | Google Drive | Path to OAuth JSON (see schema doc for setup) |

### Skills vs MCP Servers

Per the "Claude Code: Zero to Advance" guide, skills are more token-efficient than MCP servers:
- **MCP:** All endpoints loaded into context (~5.7K+ tokens per server)
- **Skills:** Only header in context (~50 tokens), full skill loaded on demand

If a tool has both a Skill and an MCP option, prefer the Skill. Browse available skills at **skills.sh**.

---

## Future Additions

These servers are worth adding when the need arises:

| Server | What It Does | When to Add |
|--------|-------------|-------------|
| **Supabase** | Database, auth, realtime, edge functions | When building a web app with Supabase backend |
| **Linear** | Project management, sprints, roadmaps | When GitHub Issues isn't enough |
| **Neon** | Serverless PostgreSQL with branching | When you need raw Postgres without Supabase |
| **Upstash** | Redis caching, Kafka queues | When apps need caching or message queues |
| **Circle.so** (custom) | Community, courses, events, members | When PBTV.app needs API automation |
| **Tidio** (custom) | Chat conversations, contacts | When chatbot needs programmatic management |
