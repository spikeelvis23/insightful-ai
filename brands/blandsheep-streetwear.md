# BlandSheep — Streetwear Brand

> Note: this is the **streetwear** BlandSheep (cyberpunk aesthetic, Shopify + Supabase).
> There is a second, unrelated-in-tech-stack "BlandSheep" concept inside the House of Uganda
> food ecosystem (an East African street food / food truck brand). Same name, different
> aesthetic and different build. See `house-of-uganda-ecosystem.md` for that one, and flag
> to Spike which one an agent is working on before it starts.

## Purpose & design language
- Streetwear brand website, cyberpunk / underground aesthetic
- Design vision blends VICE magazine editorial sensibility with hacker OS interfaces and streetwear mythology
- Color palette: dark background `#020304`, neon green `#00ff41`, cyan `#00ffff`
- Typography: Bebas Neue + Share Tech Mono
- Visual motifs: scanline overlays, glitch effects, terminal-style HUD bars, corner bracket decorations
- Design should feel like a living system, not a static page — motion, drift, and glitch are core to the aesthetic, not decorative
- Preference for organic, non-rigid layouts — scattered card positions and natural variation over structured grids

## Architecture & tools
- Hybrid Shopify + Supabase architecture:
  - **Shopify Storefront API** — products, inventory, variants, checkout, payments
  - **Supabase** — user auth, profiles, order history, wishlists
  - Shopify and Supabase connected via shared email
  - This split is intentional — commerce infra and user-data infra should stay separate
- **Replit** is the primary dev environment; file structure already established (`server.js`, admin pages)
- Dev mode mock fallbacks matter — build/test before live API connections exist

## Current state (as of last check-in)
- Two self-contained HTML/CSS/JS deliverables built and ready:
  - **`index.html`** — cinematic 3D scroll entry experience. Scattered card placement, unique tilt angles, per-card parallax speeds, wobble frequencies, organic drift. Six nav cards (SHOP, ARCHIVE, STORIES, DISPATCH, COMMUNITY, ABOUT) plus a final "ENTER THE SYSTEM" button, all clickable with zoom transitions.
  - **`home.html`** — full homepage: boot loader sequence, hero with particle canvas, product grid with Shopify API integration + mock product fallback for dev mode, ticker marquee, drop banner, editorial cards, manifesto strip, dispatch newsletter form, footer.

## On the horizon
- Core pages still to build: shop, archive, stories, dispatch, community, about
- Account flows and admin interface
- Backend integration — connecting Shopify Storefront API and Supabase in production
- Third-party service setup still pending

## Ways of working on this brand
- Deliverables are self-contained files ready to drop into Replit — no complex build steps at this stage
- Iterative refinement: review outputs, request targeted adjustments rather than full rebuilds
- Master prompts (general + Replit-specific) already exist covering env vars, `server.js` patterns, API routes, Supabase schemas, Shopify GraphQL queries, and frontend fetch patterns — treat these as canonical reference for future sessions if Spike supplies them
