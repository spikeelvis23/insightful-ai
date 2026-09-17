# Workspace instructions

This is a multi-brand website workspace. Read `PROJECT.md` first, every session, before doing
any work — it explains what's in here, how the brands relate, and known naming overlaps
(there are two unrelated "BlandSheep" concepts, see PROJECT.md).

## Brand blueprints
Full detail on each brand lives in `brands/`. Never start building a brand's site without
reading its blueprint file first — palette, typography, and design direction are already
decided for every brand and should not be re-invented.

## Agents
Specialist subagents live in `.claude/agents/`. Route work to them rather than doing
everything in the main thread:
- **brand-strategist** — resolves which brand/file a vague request maps to, writes the brief
- **copywriter** — writes on-brand, on-voice copy (cultural accuracy is mandatory for anything
  House of Uganda)
- **video-director** — runs the 10K Websites cinematic pipeline (Higgsfield generation, gates,
  cost approvals) for brands that want a scroll-driven hero video, most likely BSC
- **site-builder** — implements the actual HTML/CSS/JS
- **deploy-engineer** — self-test, copy-quality gate, and shipping; on-call dev after launch

Typical flow for a new build: brand-strategist -> copywriter -> (video-director if cinematic) ->
site-builder -> deploy-engineer.

## Skills
`.claude/skills/10k-websites/SKILL.md` holds the full cinematic scroll-site build process.
Its `references/` files are not yet populated — see the note inside PROJECT.md and the skill
file itself. Don't invent replacements for those files; ask Spike to supply them if a build
actually needs them.

## Standing preferences
- Plain HTML, CSS, vanilla JS by default, no frameworks, no build step — unless a brand's own
  blueprint already calls for something else.
- Iterative, targeted changes over full rebuilds.
- Never re-litigate a design decision a blueprint file marks as already made.
- Flag naming or ownership ambiguity (e.g. BSC vs. BlandSheep streetwear) instead of guessing.
