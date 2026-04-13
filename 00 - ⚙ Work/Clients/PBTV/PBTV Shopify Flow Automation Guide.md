---
created: 2026-03-01
updated: 2026-04-13
tags:
  - pbtv
  - shopify
  - automation
  - e-commerce
  - workflows
type: Documentation
subtype: Implementation Guide
---

# PBTV Shopify Flow Automation Guide

Complete Automation Implementation Guide
10 Workflows + 5 Bonus Flows | Exact Sidekick Prompts | Copy-Paste Ready
March 2026 | Prepared by Wes Shields / Synthminds AI

---

## Setup: Installing Shopify Flow

Shopify Flow is free on all paid Shopify plans (Basic, Grow, Advanced, Plus). It takes 60 seconds to install.

- Open the Shopify admin on your phone or computer (admin.shopify.com)
- Go to Apps in the left sidebar
- Search for "Shopify Flow" in the Shopify App Store
- Click Install (free)
- Flow now appears under Apps > Flow in your admin
- For each workflow below: Open Flow > click Sidekick icon (bottom right) > paste the prompt > review > activate

Each workflow below includes the exact Sidekick prompt you can paste, plus the manual trigger/condition/action spec in case you want to build or modify it by hand. Sidekick builds 90% of these perfectly from the prompt; you may need to tweak one or two values.

---

## Flow 1: Low Stock Alert

**Push notification when any plant drops below 3 units**

This is the single most important automation for PBTV. When a plant sells (in-store via Square or online via Shopify), and inventory drops to 3 or fewer, Monica gets an email immediately. The key detail: it only fires ONCE per product (when crossing the threshold), not on every subsequent sale.

**SIDEKICK PROMPT:** "Create a workflow that sends me an email when any product variant's inventory drops to 3 or fewer for the first time. Include the product title, variant title, current quantity, and a link to the product in the admin. Send to plantsbythepool@gmail.com with subject line 'Low Stock Alert' followed by the product title."

- **TRIGGER:** Inventory quantity changed (built-in Shopify trigger)
- **CONDITION:** Product variant inventory quantity IS LESS THAN OR EQUAL TO 3 AND Product variant inventory quantity prior IS GREATER THAN 3
- **ACTION:** Send internal email to plantsbythepool@gmail.com with subject 'LOW STOCK: {{product.title}}' and body containing product title, variant title, current quantity, and admin link

**Why the dual condition matters:** The condition checks BOTH the current quantity (3 or less) AND the prior quantity (was more than 3). This means the email only sends once, when the product first crosses the threshold. Without the prior-quantity check, Monica would get an email on every single sale until the product reaches zero.

**Test it:** Before activating, use Flow's Test Run feature. Select a product with inventory of 4. Simulate a sale (quantity drops to 3). Verify the email preview shows the correct product and quantity. Then activate.

**Variation: Slack notification instead of email**
SIDEKICK PROMPT: "Same as above but instead of email, send a Slack message to the #inventory channel with the product title, current stock, and admin link."
Requires: Slack app installed + connected to Shopify Flow. Free on all Slack plans.

---

## Flow 2: Auto-Hide Sold-Out Products

**Automatically remove sold-out plants from the online store**

When a plant's inventory hits zero, it should disappear from PBTV.shop immediately. This prevents the "stale sold-out listings" problem. The product stays in Shopify's catalog (for when it's restocked), but is unpublished from the online storefront.

**SIDEKICK PROMPT:** "Create a workflow that unpublishes a product from the online store when its total inventory quantity reaches zero. When inventory is restocked above zero, automatically republish the product to the online store."

- **TRIGGER:** Inventory quantity changed
- **CONDITION:** BRANCH 1: Product variant inventory quantity IS EQUAL TO 0 → Action A. BRANCH 2 (Otherwise): Product variant inventory quantity IS GREATER THAN 0 AND product is not active on online store → Action B.
- **ACTION:** Action A: Remove product from Online Store sales channel. Action B: Publish product to Online Store sales channel.

**Alternative approach:** Instead of unpublishing, tag the product as "sold-out" and use your Shopify theme to display a "Notify Me" button for tagged products. This keeps the product visible but non-purchasable, and pairs with the waitlist workflow (Flow 3).

---

## Flow 3: Waitlist Capture for Sold-Out Items

**Convert sold-out products into demand signals**

This workflow pairs with the Back in Stock app (free Shopify app) to capture email addresses from customers who want a plant that's currently sold out.

**SIDEKICK PROMPT:** "Create a workflow that adds a tag 'waitlist-active' to any product when its inventory reaches zero. Remove the tag when inventory is restocked above zero."

- **TRIGGER:** Inventory quantity changed
- **CONDITION:** Product variant inventory quantity EQUALS 0
- **ACTION:** Add tag 'waitlist-active' to product. (Otherwise branch: if quantity > 0, remove tag 'waitlist-active')

**Companion setup:** Install the free "Back in Stock: Restock Alerts" app. Configure it to display a "Notify Me When Available" button on any product tagged "waitlist-active." When inventory is restocked and the tag is removed, the app auto-sends restock emails.

**Data insight:** The Back in Stock app dashboard shows which products have the most waitlist signups. If 47 people are waiting for Monstera Albo, that's a clear signal to source more.

---

## Flow 4: Abandoned Cart Recovery

**Auto-email customers who leave plants in their cart**

Industry average recovery rate: 5-15% of abandoned carts.

### Option A: Built-in (No Flow needed)
- Go to Settings > Checkout > Abandoned checkouts
- Enable "Automatically send abandoned checkout emails"
- Set timing: 1 hour after abandonment (recommended)
- Customize the email template with PBTV branding

### Option B: Advanced Multi-Step via Klaviyo + Flow

**SIDEKICK PROMPT:** "Create a workflow that triggers when a checkout is abandoned. Wait 1 hour, then check if the order was completed. If not, trigger a Klaviyo event called 'cart_abandoned' with the checkout details."

- **TRIGGER:** Checkout abandoned
- **CONDITION:** Wait 1 hour → Check if order was completed (order exists for this checkout = false)
- **ACTION:** Trigger Klaviyo event 'pbtv_cart_abandoned' with checkout URL, line items, total price

**Klaviyo handles:**
- Email 1 (immediate after Flow trigger): "You left some plants behind!" with cart contents
- Email 2 (24 hours later): "Still thinking about it? Here's 10% off" with discount code
- Email 3 (48 hours later): "Last chance -- these plants are selling fast" with urgency

---

## Flow 5: New Customer Welcome Series

**Turn first-time buyers into Plant Fam members**

**SIDEKICK PROMPT:** "Create a workflow that triggers when a customer places their first order. Tag the customer as 'first-purchase'. Then trigger a Klaviyo event called 'new_customer_welcome' with the customer's first name and email."

- **TRIGGER:** Order created
- **CONDITION:** Customer orders count EQUALS 1
- **ACTION:** 1) Add tag 'first-purchase' to customer. 2) Trigger Klaviyo event 'new_customer_welcome'

**Klaviyo welcome series (3 emails):**
- Email 1 (immediate): "Welcome to the Plant Fam!" Thank you, shipping timeline
- Email 2 (Day 3): Plant care tips for the species they purchased. Link to PBTV.app
- Email 3 (Day 7): Invite to follow @plantsbythevillage on IG + join PBTV.app + 10% off second order

---

## Flow 6: VIP Customer Auto-Tagging

**Identify and reward your best customers automatically**

**SIDEKICK PROMPT:** "Create a workflow that tags a customer as 'VIP' when their total lifetime spending exceeds $200. Only tag them if they don't already have the VIP tag."

- **TRIGGER:** Order created
- **CONDITION:** Customer total spent IS GREATER THAN $200 AND Customer tags DOES NOT CONTAIN 'VIP'
- **ACTION:** 1) Add tag 'VIP'. 2) Send internal email. 3) Trigger Klaviyo event 'customer_vip_upgrade'.

**VIP perks:** Early access to rare drops (24-48 hour head start), free shipping, exclusive PBTV.app content, birthday discount.

**Threshold guidance:** Start at $200. Create multiple tiers: Bronze ($100), Silver ($200), Gold ($500).

---

## Flow 7: Post-Purchase Care Email

**Send species-specific care guides after delivery**

Reduces "my plant is dying" support tickets by 50-70%.

**SIDEKICK PROMPT:** "Create a workflow that triggers when an order is fulfilled. Wait 3 days (to allow for delivery). Then send an internal email with the order line items to plantsbythepool@gmail.com. Also trigger a Klaviyo event called 'post_purchase_care' with the order line items and customer email."

- **TRIGGER:** Order fulfilled
- **CONDITION:** Wait 3 days
- **ACTION:** Trigger Klaviyo event 'post_purchase_care' with customer email, first name, and order line item titles

**Klaviyo handles personalization:** Conditional splits based on product title. If order contains "Monstera" → Monstera care email. If "Calathea" → Calathea care email. Default: general tropical plant care.

**Advanced:** Create care guide content on PBTV.app and link to it: "For more detailed care guides, visit PBTV.app -- your first 7 days are free."

---

## Flow 8: High-Risk Order Flag

**Prevent fraud on rare plant orders**

Rare plants at $65-250+ are high-value targets for fraudulent orders.

**SIDEKICK PROMPT:** "Create a workflow that triggers when Shopify's risk analysis is complete. If the order risk level is high, add a tag 'high-risk-hold' to the order, put the order on hold, and send me an email at plantsbythepool@gmail.com with the order details and risk reason."

- **TRIGGER:** Order risk analyzed
- **CONDITION:** Order risk level IS HIGH
- **ACTION:** 1) Add tag 'high-risk-hold'. 2) Put fulfillment on hold. 3) Send internal email with order details.

**Monica's action:** Review in Shopify app, release hold (legitimate) or cancel and refund (fraud). Takes 30 seconds.

---

## Flow 9: Auto-Request Product Reviews

**Build social proof on every product page**

14 days after delivery (enough time for customer to assess plant health).

**SIDEKICK PROMPT:** "Create a workflow that triggers when an order is fulfilled. Wait 14 days. Then trigger a Klaviyo event called 'review_request' with the customer email, first name, and the first line item's product title and product URL."

- **TRIGGER:** Order fulfilled
- **CONDITION:** Wait 14 days
- **ACTION:** Trigger Klaviyo event 'review_request'

**Klaviyo email:** "How's your [Plant Name] doing? Leave a review and get 5% off your next order."

**Alternative:** Use Judge.me's built-in review request feature (free plan, unlimited requests).

---

## Flow 10: Daily Sales Summary Email

**One-glance daily health check at 8pm**

**SIDEKICK PROMPT:** "Create a scheduled workflow that runs every day at 8:00 PM Eastern time. Get all orders created today. Count them. Sum their totals. Also get all products with zero inventory. Count those. Send me an email at plantsbythepool@gmail.com with subject 'PBTV Daily Summary' containing: number of orders today, total revenue, number of unfulfilled orders, and number of out-of-stock products with their titles."

- **TRIGGER:** Scheduled time: Every day at 8:00 PM ET
- **CONDITION:** Get order data (created today) + Get product data (inventory = 0)
- **ACTION:** Count orders, sum totals, count out-of-stock, send email

**Note:** Uses advanced Flow features (Scheduled Time, Get Data, Count, Sum, For Each). Sidekick generates the basic structure; you may need to refine Get Data filters manually.

---

## Bonus Flows

### Bonus A: Auto-Tag Pet-Safe Products
**SIDEKICK PROMPT:** "Create a workflow that adds the tag 'pet-safe' to any product when its title or description contains the words 'pet safe', 'pet friendly', 'non-toxic', or 'cat safe'."

### Bonus B: Auto-Tag Rare Plants by Price
**SIDEKICK PROMPT:** "Create a workflow that triggers when a product is created or updated. If the product price is $50 or more, add the tag 'rare-collection'. If under $50, add the tag 'everyday-collection'. Remove the opposite tag if present."

### Bonus C: Notify Team of Large Orders
**SIDEKICK PROMPT:** "Create a workflow that sends me an email when any single order exceeds $100 in total value. Include the order number, customer name, line items, and total in the email."

### Bonus D: Auto-Cancel Unpaid Orders
**SIDEKICK PROMPT:** "Create a workflow that triggers when an order is created with pending payment. Wait 24 hours. If the payment is still pending, cancel the order and restock the inventory."

### Bonus E: Tag Palmstreet Pre-Reserve
**SIDEKICK PROMPT:** "Create a workflow that adds a tag 'palmstreet-reserved' to any product when I manually add that tag, and simultaneously reduces the online store inventory by the number I specify in a metafield called 'palmstreet_reserve_qty'. When I remove the tag, restore the inventory."

---

## Testing & Activation Checklist

Before activating any workflow:
- [ ] Open the workflow in Flow editor. Click Test Run.
- [ ] Select a sample product/order matching trigger conditions.
- [ ] Watch execution path light up step by step.
- [ ] Check email preview shows correct data.
- [ ] Confirm no real actions during test (test mode is safe).
- [ ] Click "Turn on workflow."
- [ ] Trigger for real with a test purchase or manual inventory adjustment.
- [ ] Check email/Slack for notification. Verify data is correct.
- [ ] Monitor Run History tab for the first week.

## Recommended Activation Order

| Week | Flows | Why |
|------|-------|-----|
| Week 1 | Flow 1 (Low Stock) + Flow 8 (High-Risk) + Flow 10 (Daily Summary) | Notifications only -- no data modifications. Safe to test. |
| Week 2 | Flow 2 (Auto-Hide) + Flow 3 (Waitlist) + Bonus B (Price Tags) | Product visibility changes. Monitor for a few days. |
| Week 3 | Flow 4 (Abandoned Cart) + Flow 5 (Welcome) + Flow 6 (VIP) | Customer-facing emails begin. Review templates carefully. |
| Week 4 | Flow 7 (Care Email) + Flow 9 (Reviews) + all Bonus flows | Full automation stack is live. Monitor Run History. |

**Total setup time:** ~2-3 hours using Sidekick prompts.
**Once activated:** 15 automations run 24/7, eliminating ~15-20 hours/week of manual work.
**Total cost:** $0 (Shopify Flow is free on all plans).

---

## PBTV Tech Stack Reference

| Layer | Tool | Monthly Cost | Role |
|-------|------|-------------|------|
| E-Commerce Platform | Shopify Basic | $39/mo | PBTV.shop storefront, product catalog, checkout |
| In-Store POS | Square POS | $0 (free tier) | In-store transactions. Keeps current hardware. |
| POS-Shopify Sync | Thrive by Square (or DPL Square) | $20-50/mo | Real-time bi-directional inventory sync |
| Etsy Sync | DPL Etsy Integration (or Shuttle) | $20-30/mo | Product/inventory/order sync between Shopify and Etsy |
| Shipping Hub | ShipStation | $10-25/mo | Auto-import orders, print labels, push tracking |
| AI Chatbot | Tidio (Phase 1) | $0-29/mo | 24/7 customer support on PBTV.shop |
| Email Marketing | Shopify Email or Klaviyo | $0-20/mo | Abandoned cart, new drops, care tips, promos |
