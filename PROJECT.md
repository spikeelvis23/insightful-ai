# Spike's Website Build Project

This is the master file for a multi-brand website build. Read this first, then open the
specific `brands/<name>.md` file for whichever brand you're actually building.

## What's in this workspace

| Brand / Venture | File | What it is | Build status |
|---|---|---|---|
| BlandSheep (streetwear) | `brands/blandsheep-streetwear.md` | Cyberpunk streetwear e-commerce site, Shopify + Supabase | 2 of ~8 pages built |
| House of Uganda ecosystem | `brands/house-of-uganda-ecosystem.md` | 5 linked culinary brands (House of Uganda Bible, Sauce House, Culinary Bible, African Flame, BlandSheep food truck) | Book I done, several modules built, more scaffolded |
| DIASPORA | `brands/diaspora.md` | African diaspora media platform (Spiral Media) | Iterative build, agent/dashboard tooling in progress |
| FREQUENCY | `brands/frequency.md` | AI hip-hop curation tool (Spiral Media, shares system with DIASPORA) | Early build |
| BSC (Bland Sheep Crew) | `brands/bsc.md` | Streetwear/mascot brand + music side project | Creative direction + script done, site not started |

## Known naming overlap — flag before starting work

There are **two unrelated "BlandSheep" concepts**:
1. The **streetwear** brand (cyberpunk, Shopify + Supabase, Replit) — `brands/blandsheep-streetwear.md`
2. A **street food / food truck** concept inside the House of Uganda ecosystem (Soho-bougie aesthetic, espresso/ivory/brass) — covered inside `brands/house-of-uganda-ecosystem.md`

Any agent should confirm which one it's working on before generating anything.

There's also an open question about how **BSC** relates to the streetwear **BlandSheep** brand
(parent brand, sibling label, or shared asset pipeline) — worth settling with Spike directly
before a site gets built for either, since it affects domain names, palette, and whether they
should link to each other.

## Shared design systems (so builds don't clash by accident)

| System | Used by | Palette | Type |
|---|---|---|---|
| Cyberpunk / hacker-OS | BlandSheep (streetwear) | `#020304` bg, `#00ff41` green, `#00ffff` cyan | Bebas Neue + Share Tech Mono |
| Parchment / field-guide | House of Uganda (Bible) | matte black / bronze / forest green | Fraunces / Work Sans / IBM Plex Mono |
| Soho bougie | BlandSheep (food truck) | espresso / ivory / brass | Fraunces |
| Black / dark wood / ember | African Flame | black, dark wood, warm gold/ember | — |
| Spiral Media | DIASPORA + FREQUENCY | deep black, gold accents | Playfair Display / Space Mono |

## Build methodology

All new site builds in this workspace should go through the **10K Websites** approach —
a cinematic, scroll-driven build process (research → design package → hero video/visuals →
build → self-test → deploy). It lives at `.claude/skills/10k-websites/SKILL.md`.

> Heads up: only the main skill file was provided, not its `references/` files
> (`prompt-laws.md`, `design-package.md`, `scrub-pipeline.md`, `ffmpeg-recipes.md`,
> `deploy.md`, `troubleshooting.md`) that the main file repeatedly points to. If you have
> the original skill zip, drop the rest of those files into
> `.claude/skills/10k-websites/references/` — an agent following this skill will look for
> them and its process depends on them.

This methodology fits builds that want a generated cinematic hero (BSC's brutalist/parallax
site is the most obvious immediate fit). For brands with a firm "single self-contained HTML
file, no frameworks" rule already in place (the House of Uganda ecosystem), keep using that
existing approach rather than introducing new tooling mid-stream — the two aren't in conflict,
just different tools for different brands.

## Working style Spike has established (apply across all brands unless told otherwise)

- Prefers plain HTML, CSS, and vanilla JS — no frameworks, no build step, unless a brand's
  existing build already calls for something else (e.g. BlandSheep streetwear's Shopify/Supabase split)
- Gives brief creative direction and expects it interpreted fully, not built to a granular spec
- Prefers iterative, targeted refinement over full rebuilds
- Prefers living/editable, data-driven documents (calculators, cross-linked data) over static pages
- Cultural and factual accuracy is non-negotiable on anything Uganda/East-Africa-related

## Next steps

1. Confirm the BSC / BlandSheep-streetwear relationship question above.
2. Decide which brand to build or continue first.
3. If using the 10K Websites skill, supply its missing `references/` files.
4. Open the matching agent in `.claude/agents/` (see `README.md`) to start work.
