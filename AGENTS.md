# AGENTS.md – LK Informatik Skript

## What this repo is

Static website: 13 HTML pages covering a German Gymnasium J2 computer science curriculum.
Hosted at: https://dirk-mayrock.github.io/informatik-skript/

---

## Critical: never edit HTML files directly

All 13 `Thema*.html` files are **generated**. Hand-edits will be overwritten next build.

The only editable sources are:
- `Thema*.md` — content (Markdown)
- `build_html.py` — generator, HTML structure, per-topic viz snippets (`VIZUALIZATIONS` dict)
- `lk-style.css` — global design tokens, Dark/Light mode variables
- `lk-viz.css` — viz widget styles + Light-mode overrides
- `lk-script.js` — theme toggle, copy buttons, progress bar, rating bar animations
- `lk-viz.js` — all interactive visualizations (one `initTN*` function per widget)
- `index.html` — standalone homepage, **not** generated

After any change to the above, regenerate all HTML:

```bash
cd "…/hannah_script"
python3 build_html.py      # writes all 13 Thema*.html
```

Then deploy:

```bash
git add .
git commit -m "…"
git push                   # GitHub Pages rebuilds automatically (~1 min)
```

---

## File map

| File | Role |
|---|---|
| `build_html.py` | Generator. Contains `TOPICS` list, `VIZUALIZATIONS` dict (HTML per topic), `md_to_html()` converter, `build_page()` template |
| `lk-style.css` | Design tokens. `:root` = dark mode, `body.light` = light mode overrides |
| `lk-viz.css` | Viz widget styles. Has its own `body.light` block at the bottom — **always add light-mode overrides here when adding new viz CSS** |
| `lk-script.js` | Shared JS: `initThemeToggle()`, `copyCode()`, `toggleTask()`, progress bar, rating bar observer. Theme persisted in `localStorage` as `lk-theme` |
| `lk-viz.js` | All interactive widgets. One `initTN*` function per widget; all called from a single `DOMContentLoaded` listener at the bottom |
| `index.html` | Standalone homepage — edited directly, not generated |

---

## Adding or changing a visualization

1. **Add/update the HTML snippet** in `build_html.py` → `VIZUALIZATIONS[N]`. Use `id="viz-tN-*"` naming (e.g. `viz-t3-foo`).
2. **Add/update the JS** in `lk-viz.js`. Add a new `function initTN*()` and call it in the `DOMContentLoaded` boot block at the bottom.
3. **Add light-mode CSS** in `lk-viz.css` under the `body.light` block if the widget uses `var(--bg-code)` as a background (it renders dark in light mode).
4. Run `python3 build_html.py` and verify in browser before pushing.

### Thema 4 special case
The 32 IEEE-754 bit cells are injected by `IEEE_BIT_INIT` (inline `<script>` tag in `build_html.py`), not in the viz HTML snippet, because they need the DOM ready before JS runs. Do not remove this block.

---

## Known typo in codebase — do not fix silently

The dict in `build_html.py` is named `VIZUALIZATIONS` (one 'u' missing). The name is referenced in `main()` — if you rename it, update both places.

---

## Thema 2 slug is different

The file is `Thema2_Binaere_Arithmetik_V2.md/.html` (note `_V2`). The `TOPICS` list in `build_html.py` reflects this. Don't rename it without updating `TOPICS`.

---

## Sidebar active state

Each page sets `--active: var(--cN)` via an inline `<style>` block in `build_page()`. The 13 accent colors are defined in `lk-style.css` as `--c1` through `--c13`. Sidebar highlighting uses these same variables via `data-c` attributes.

---

## Step-navigation widgets (T12, T13)

These use **pre-recorded frame arrays**, not `async/await`. All steps are computed synchronously on "build/start", then navigated with prev/next buttons.

- **T12 (Struktogramm):** `initT12Trace()` builds a `steps[]` array, then prev/next update `stepIdx`.
- **T13 (Sortier-Rennen):** `initT13SortRace()` calls four `simulate*()` functions synchronously, stores results in `allFrames`, then prev/next/auto update a shared `frameIdx` across all four arenas simultaneously.

Do not switch these back to `async/await` — backwards stepping is only possible with pre-recorded frames.

---

## Light mode

`body.light` is toggled by `lk-script.js:initThemeToggle()` and persisted via `localStorage('lk-theme')`.

The main problem area is anything that uses `var(--bg-code)` as a background color — in light mode `--bg-code` is `#1e2235` (dark), so inputs and panels built on it need explicit `body.light` overrides in `lk-viz.css`.

---

## Deploy

- GitHub repo: `dirk-mayrock/informatik-skript` (public)
- Pages source: `main` branch, root `/`
- No build step on GitHub — static files served directly
- `Lernaufschriebe.pdf` is gitignored (personal source document)
