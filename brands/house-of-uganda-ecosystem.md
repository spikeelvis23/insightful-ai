# House of Uganda — Culinary Brand Ecosystem

An interconnected set of Ugandan / East African culinary brands, reference systems, and food
businesses. They share design language, data systems, and a cultural mission. Broader vision
across all of them: a marketing website, a mobile app, and an internal ops dashboard.

**Cultural & editorial rules that apply across every brand below (non-negotiable):**
- Editorial voice: "warm, direct, Kampala-rooted" — specific and grounded, not museum-placard prose
- Cultural accuracy is non-negotiable — no dish appears without genuine Ugandan/East African grounding (e.g. "Coastal Fish Curry" → corrected to "Nile Perch & Tilapia Stew," anchored in Lake Victoria). Origin badges distinguish "Uganda's Own" vs. "Shared — East Africa."
- Scientific precision over culinary vagueness — exact weights, baker's percentages, reproducible method steps, not "a little ginger"
- Data-driven cross-referencing — cross-references are computed from array filtering on exact name matches, never hand-typed links
- Lab data (pH, SHU, shelf-life) is flagged as needing third-party validation before production use — keep that caveat in any doc that carries it

**Shared technical approach:**
- All builds are single self-contained HTML files — plain HTML, inline CSS, vanilla JS. No frameworks, no build tools, beyond Google Fonts. Firm technical preference.
- Living/editable documents preferred — in-browser editability, dynamic rendering (batch scalers, cost calculators, auto-updating previews)
- Typography system across projects: Fraunces (display/serif headlines), Bebas Neue (labels/uppercase), Work Sans or Inter (body), IBM Plex Mono (data/labels)
- Data schemas: `SPICES`, `DISHES`, `BLENDS` JS arrays with defined fields, including `becomesSoups` for Book III linkage

---

## 1. House of Uganda (flagship reference + commercial brand)

- Flagship culinary reference and commercial brand
- **"Spice, Soup & Beverage Bible"** — living four-volume reference:
  - Book I: Spice Library
  - Book II: Sauces
  - Book III: Soups
  - Book IV: Drinks
- Public homepage design system: matte black / bronze / forest green palette; Fraunces / Work Sans / IBM Plex Mono; interactive "Sauce Lineage" visualization; animated hero
- Aesthetic choice made deliberately: parchment/field-guide look was chosen **over** a dark/gold look — Uganda flag colors (black, `#c8102e` red, `#c99a00` gold) exist as an option but were not selected for the main aesthetic
- Also has vision for internal ops software, not just the public site

### Book I status (fully built)
- Ch.1: Ugandan flavor theory
- Ch.2: 22 spice profiles with inline SVG botanical icons
- Ch.3: six East African spice blends
- Ch.4: Plate Map of 12 dishes, bidirectional cross-linking, origin badges
- Standalone Kampala Fire product detail page exists
- System is data-driven via JS arrays (cross-refs computed, not hand-typed)
- Known fixed bug: hardcoded spice count ("24") vs. actual `SPICES.length` — now dynamic

### Book II (Sauces) — ready to build
- Prompt and schema are ready, including a `becomesSoups` field for future Book III linkage

### Books III & IV — future
- Data linkage to Book I already scaffolded

---

## 2. House of Uganda — Sauce House (commercial sauce line)

Five named products:
1. **Kampala Fire** (flagship)
2. Golden Matoke Glaze
3. Pearl of Africa Peanut
4. Smoked Nile BBQ
5. Verde Village Sauce

---

## 3. Culinary Bible (Sauce Lab / R&D documentation system)

- Scientific R&D documentation system: exact weights, batch percentages, reproducible processes for sauces, soups, drinks, food items — built for multi-location replication
- **Flame Sauce No. 001** fully documented in the seven-layer R&D format:
  1. Identity
  2. Exact Formula
  3. Method
  4. Sensory Profile
  5. Food Safety & Shelf Life
  6. Cost & Yield
  7. Menu Applications
- Live batch scaler and cost calculator built
- Timing module (active/passive time distinction) built as a drop-in component across all four content categories
- On the horizon: fries sauces, soups, flame sauce variants

---

## 4. African Flame (founder platform / food company)

- Mission: transform how the world experiences African cuisine
- Home dashboard built: sidebar nav, bento grid of 12 project areas, animated mission progress indicators
- Black, dark wood, warm gold/ember accent palette
- Next priority module: **Sauce Lab**, then **Recipe Lab**
- Internal operations dashboard under development

---

## 5. BlandSheep (street food / food truck — NOT the streetwear brand)

- A street food and flavor brand with an urban Ugandan aesthetic
- Food truck concept: East African / Kampala-inspired street food
- Connected to Spike's BSC streetwear brand through shared design sensibility (concept-level, not shared codebase)
- Aesthetic pivoted from street-market to **"Soho bougie"** — Fraunces serif, espresso / ivory / brass palette (distinct from the cyberpunk streetwear BlandSheep palette)
- Built so far:
  - Interactive Flavor Bible: four dishes × proteins, sauces, flavor profiles, cost tiers, customer archetypes
  - Pili-Peanut Velvet Matrix sauce page: split-screen layout, trade-secret reveal panel, accordion recipe cards
- On the horizon: optional functional drag on the Pili-Peanut ratio dial; palette alignment to a DIASPORA brass system; photography swap for card swatches

---

## Working style across this whole ecosystem
- Spike gives brief aesthetic direction and expects the complete vision interpreted and executed without granular specs
- When a spec is too large for one pass, sequenced builds are fine (e.g. dashboard first, then modules)
- DeepSeek has been used for cross-session AI handoff prompts (general project handoff + a Book II–specific one) — if Spike has these, they're useful context to request
