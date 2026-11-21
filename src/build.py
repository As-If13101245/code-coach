"""Build the site into the repository root (GitHub Pages serves the root).
Run from the repo root:  python3 src/build.py
"""
import json, os, glob, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
import sys; sys.path.insert(0, HERE)
from syllabus import schedule

# OWL 3 for the DOM/OWL lessons. Same version as Odoo 20 (master) ships in addons/web/static/lib/owl.
OWL_URL = "https://cdn.jsdelivr.net/npm/@odoo/owl@3.0.0-alpha.50/dist/owl.iife.min.js"

def load_lessons():
    out = []
    for path in sorted(glob.glob(os.path.join(HERE, "lessons_w*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.extend(mod.LESSONS)
    ids = [l["id"] for l in out]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: raise SystemExit(f"Duplicate lesson ids: {dup}")
    return out

if __name__ == "__main__":
    py, js, days = schedule()
    syl = py + js
    meta = {l["id"]: l for l in syl}
    lessons = [{**meta[L["id"]], **L} for L in load_lessons()]
    lessons.sort(key=lambda l: days.index(l["id"]))
    html = open(os.path.join(HERE, "template.html")).read()
    frame = open(os.path.join(HERE, "dom-frame.html")).read().replace("__OWL_SCRIPT__", f'<script src="{OWL_URL}"></script>')
    html = html.replace("__DOM_FRAME__", json.dumps(frame).replace("</", "<\\/"))
    html = html.replace("__SYLLABUS__", json.dumps(syl, ensure_ascii=False)).replace("__SCHEDULE__", json.dumps(days))
    open(os.path.join(ROOT, "index.html"), "w").write(html)
    json.dump(lessons, open(os.path.join(ROOT, "lessons.json"), "w"), ensure_ascii=False, indent=1)
    json.dump({"start": "2026-11-22", "schedule": days, "syllabus": syl}, open(os.path.join(ROOT, "syllabus.json"), "w"), ensure_ascii=False, indent=1)
    shutil.copy(os.path.join(HERE, "py-worker.js"), os.path.join(ROOT, "py-worker.js"))
    print(f"Built {len(lessons)} lessons of {len(days)} days.")
