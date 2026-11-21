# Code Coach

A static learning app (GitHub Pages) that teaches Asif Python and JavaScript/OWL 3 (Odoo 20) from basic to advanced. One ~30-minute lesson a day, alternating Python and JavaScript/OWL, 105 days from 2026-11-22.

- Live site: https://as-if13101245.github.io/code-coach/
- A daily reminder (a Claude scheduled task) reads `syllabus.json` and `lessons.json` from the `main` branch, so keep their format stable.
- Progress is stored in the browser's localStorage under the key `code-coach`. Never rename lesson ids or that key, or learners lose progress.

## Layout

```
src/                  <- edit these
  syllabus.py         105-day syllabus (titles, units) and the day schedule
  lessons_w1.py       lessons py01–py07, js01–js07
  lessons_w2.py ...   add one file per weekly batch
  template.html       the app (HTML/CSS/JS); build injects syllabus, schedule and the DOM frame
  dom-frame.html      the sandboxed page that runs "runner": "dom" lessons (OWL loaded as global `owl`)
  py-worker.js        runs Python with Pyodide in a Web Worker (top-level await allowed; loads sqlite3 etc. on import)
  build.py            writes index.html, lessons.json, syllabus.json, py-worker.js to the repo root; OWL_URL pins OWL
  verify.py           tests every lesson (needs python3, node, and Google Chrome/Chromium for DOM lessons)
index.html, lessons.json, syllabus.json, py-worker.js   <- generated: never edit by hand
sw.js, manifest.webmanifest, icon-*.png                 <- static
```

## Commands (run from the repo root)

```bash
python3 src/build.py     # regenerate the site
python3 src/verify.py    # must print "All lessons OK." before any commit
```

## Adding the next weekly batch

1. Find the next 14 lesson ids in schedule order: `python3 -c "import sys; sys.path.insert(0,'src'); from syllabus import schedule; print(schedule()[2])"` and skip ids already written.
2. Create `src/lessons_wN.py` with `LESSONS = [ ... ]`. Copy the structure of `lessons_w1.py` exactly.
3. Run build, then verify. Fix every PROBLEM line. Then commit with a message like `Add lessons py08–py14, js08–js14` and push.
4. If `sw.js` behaviour changes, bump `CACHE` in sw.js (e.g. `code-coach-v2`).

## Lesson format

Each lesson is a dict:

- `id` — must match `syllabus.py` (e.g. `py08`, `js15`). Title, unit, track and number come from the syllabus; don't repeat them.
- `goal` — one sentence. Backticks render as inline code.
- `cards` — 3–5 items `{"h": heading, "p": short explanation, "code": optional example}`. One idea per card, short sentences, plain English (the learner is preparing for IELTS too).
- `odoo` — one or two sentences linking the topic to real Odoo work. Must be accurate; never invent Odoo APIs.
- `owl2` — JS/OWL lessons only, when OWL 3 differs from OWL 2 (Odoo 17/19): one or two sentences on the old way. Omit or leave empty otherwise.
- `predict` — `{"code", "q", "opts": [4 strings], "ans": index, "why"}`. `opts[ans]` must equal the exact output (lines joined by `\n`). JS arrays/objects print as `JSON.stringify` output.
- `bug` — `{"task", "code" (buggy), "test", "hint", "solution"}`; optional `"stdin"` (Python input lines joined by `\n`).
- `write` — `{"task", "starter", "test", "solution"}`; optional `"stdin"`.
- `quiz` — exactly 3 items `{"q", "opts": [4], "ans", "why"}`.

### Tests

- Python: the test runs in the same namespace after the learner's code. Available: `_output` (all printed text) and `_code` (their source). Use `assert cond, "friendly message"`. The message is shown to the learner, so make it say what's expected.
- JavaScript: the test is appended to the learner's code inside one async function, so it sees their `const`/`let` variables. Available: `__logs` (one string per console.log), `__code`, and `check(cond, "message")`.
- Every `solution` must pass, and every buggy `code` / `starter` must fail. `verify.py` enforces both.
- Check behaviour, not exact wording, where reasonable. Add a `_code` / `__code` check only when the task requires a technique (e.g. "use a comprehension").

### Content rules

- Basic to advanced, in syllabus order. Use only concepts already taught or taught in this lesson.
- Use examples from Asif's world: garment orders, zippers, brands (H&M, Kontoor, GAP, Kohl's, Carter's), OA/PI numbers, shipments, Odoo records.
- OWL lessons target **OWL 3 / Odoo 20** (signals, `computed`, `effect`, plugins). Check every OWL 3 API against the official docs at https://odoo.github.io/owl/ before using it; if unsure, say so and leave it out rather than guess.
- JS runners: js01–js14 run in a Web Worker (no DOM). js15+ must have `"runner": "dom"`: they run in a sandboxed iframe (`src/dom-frame.html`) with a real `document` and OWL 3 (`@odoo/owl@3.0.0-alpha.50`, the same build Odoo 20 master ships) as the global `owl`. Start OWL code with `const { Component, xml, mount, signal } = owl;` and `await mount(...)`. Tests may call `await __tick()` to let OWL re-render after a click or a signal change. **Run** shows a live preview; **Check** runs hidden. verify.py runs these cases in headless Chrome.
- OWL 3 facts checked against the docs (doc/v3 in the odoo/owl repo): templates read the component through `this.` (`t-out="this.count()"`, `t-on-click="this.add"`); `t-esc` is gone; props come from `props = useProps({ name: t.string(), qty: t.number().optional(0) })` (static props/defaultProps are ignored); `t-foreach` needs `t-key`; `t-model` takes a signal (`t-model.proxy` for a proxy path); `t-ref` takes `signal.ref()`; `useState`/`reactive` → `proxy`; `env`/`useSubEnv` → plugins (`Plugin`, `usePlugin`, `providePlugins`); `useEffect` has no dependency array; `onWillUpdateProps`, `onWillRender`, `onRendered`, `this.render`, `useComponent` are removed; `useExternalListener` → `useListener`.
- Odoo 20 (master, checked 2026-11-21): services are moving to plugins (`ORM` in `@web/core/orm_plugin`, `NotificationPlugin` in `@web/core/notifications/notification_plugin`, `ActionPlugin` in `@web/webclient/actions/action_plugin`), registered with `services.add(...)` from `@web/core/services`. `useService("orm")` etc. still work through a temporary bridge marked "@todo owl3 migration". `registry.category("systray"/"actions"/"services")` and `patch()` from `@web/core/utils/patch` still exist. Re-check before writing the Odoo 20 unit (js37+).
- Python runs in the browser via Pyodide 0.26.4: no network, no files on disk beyond Pyodide's in-memory filesystem, no psycopg2. For the PostgreSQL lesson use `sqlite3` to demonstrate, and explain the PostgreSQL differences in the cards. For the async lesson: `asyncio.run()` can't run in the browser (a loop is already running), so exercises use top-level `await main()`; explain that normal Python uses `asyncio.run(main())`. verify.py supports the same.

## Don'ts

- Don't edit generated files by hand.
- Don't rename or reorder existing lesson ids, or change `START` / the schedule after lessons have started.
- Don't commit if `verify.py` reports problems.
- Don't add trackers, analytics or external requests beyond the pinned Pyodide/OWL CDNs.
