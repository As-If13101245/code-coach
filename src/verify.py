"""Check every lesson: solutions pass, starters/buggy code fail, predict answers match real output,
quiz answers are valid. Needs python3 and node; DOM/OWL lessons ("runner": "dom") also need
Google Chrome or Chromium (run headless).  Run from the repo root:  python3 src/verify.py
"""
import io, os, sys, ast, json, shutil, asyncio, inspect, tempfile, subprocess, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from build import load_lessons, OWL_URL
from syllabus import schedule

class _Timeout(BaseException): pass
def _alarm(*a): raise _Timeout("Stopped after 5 seconds (endless loop?)")
import signal; signal.signal(signal.SIGALRM, _alarm)

class _Cap(io.StringIO):
    def write(self, s):  # an endless print loop must not eat all memory
        if self.tell() > 1_000_000: raise _Timeout("Too much output (endless loop?)")
        return super().write(s)

def run_py(code, test, stdin=""):
    signal.setitimer(signal.ITIMER_REAL, 5)
    try: return _run_py(code, test, stdin)
    finally: signal.setitimer(signal.ITIMER_REAL, 0)

def _run_py(code, test, stdin=""):
    lines = stdin.split("\n") if stdin else []
    def fake_input(prompt=""):
        print(prompt, end="")
        if not lines: raise EOFError("No input")
        return lines.pop(0)
    ns = {"__name__": "__main__", "input": fake_input}; buf = _Cap()
    try:
        with contextlib.redirect_stdout(buf):
            # same as the app: top-level await is allowed (the browser already runs an event loop)
            r = eval(compile(code, "main.py", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT), ns)
            if inspect.iscoroutine(r): asyncio.run(r)
        ns["_output"] = buf.getvalue(); ns["_code"] = code
        if test: exec(test, ns)
        return True, buf.getvalue()
    except BaseException as e:
        return False, f"{type(e).__name__}: {e}"

JS = r'''
const __logs=[]; const fmt=v=>typeof v==="string"?v:(v===undefined?"undefined":(typeof v==="function"?v.toString():JSON.stringify(v)));
const console={log:(...a)=>__logs.push(a.map(fmt).join(" ")),info:(...a)=>__logs.push(a.map(fmt).join(" ")),warn:(...a)=>__logs.push("⚠ "+a.map(fmt).join(" ")),error:(...a)=>__logs.push("✖ "+a.map(fmt).join(" "))};
function check(c,m){ if(!c) throw new Error(m||"Check failed"); }
const __code = %s;
(async function(){ %s
;%s
})().then(()=>setTimeout(()=>process.stdout.write("PASS\n"+__logs.join("\n")),50)).catch(e=>process.stdout.write("FAIL "+e.message));
'''
def run_js(code, test):
    r = subprocess.run(["node", "-e", JS % (json.dumps(code), code, test)], capture_output=True, text=True, timeout=15)
    out = r.stdout + r.stderr
    return out.startswith("PASS"), out[5:] if out.startswith("PASS") else out[:300]

# ---------- DOM / OWL lessons: run every case in headless Chrome, each in a fresh sandboxed frame ----------
# The page is served from a local HTTP server and POSTs its results back, so OWL runs in real time.
PAGE = r"""<!DOCTYPE html><html><body><script>
const FRAME = %s, CASES = %s;
function one(c){ return new Promise(resolve => {
  const f = document.createElement("iframe"); f.setAttribute("sandbox", "allow-scripts allow-forms"); f.srcdoc = FRAME;
  const t = setTimeout(() => { removeEventListener("message", on); f.remove(); resolve({ err: "Timed out after 8 seconds" }); }, 8000);
  function on(e){ if (e.source !== f.contentWindow || !e.data || !e.data.__cc) return;
    if (e.data.ready){ f.contentWindow.postMessage({ __cc: "run", code: c.code, test: c.test }, "*"); return; }
    if (e.data.resize) return;
    removeEventListener("message", on); clearTimeout(t); f.remove(); resolve(e.data); }
  addEventListener("message", on);
  document.body.appendChild(f); }); }
(async () => { const res = {}; for (const c of CASES) res[c.key] = await one(c);
  await fetch("/results", { method: "POST", body: JSON.stringify(res) }); })();
</script></body></html>"""

def chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(name): return shutil.which(name)
    return None

def owl_source():
    cache = os.path.join(tempfile.gettempdir(), "code-coach-owl-" + OWL_URL.split("@odoo/owl@")[1].split("/")[0] + ".js")
    if not os.path.exists(cache):
        import urllib.request
        urllib.request.urlretrieve(OWL_URL, cache)
    return open(cache, encoding="utf-8").read()

def run_dom_cases(cases):
    import threading, http.server
    exe = chrome()
    if not exe: raise SystemExit("DOM lessons need Google Chrome or Chromium to verify.")
    frame = open(os.path.join(HERE, "dom-frame.html")).read().replace("__OWL_SCRIPT__", "<script>" + owl_source() + "</script>")
    page = (PAGE % (json.dumps(frame).replace("</", "<\\/"), json.dumps(cases).replace("</", "<\\/"))).encode()
    got = {}; done = threading.Event()
    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a): pass
        def do_GET(self):
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers(); self.wfile.write(page)
        def do_POST(self):
            got.update(json.loads(self.rfile.read(int(self.headers["Content-Length"])))); self.send_response(204); self.end_headers(); done.set()
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with tempfile.TemporaryDirectory() as d:
        proc = subprocess.Popen([exe, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
                                 f"--user-data-dir={d}/profile", f"http://127.0.0.1:{srv.server_address[1]}/"],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            if not done.wait(60 + 10 * len(cases)): raise SystemExit("Chrome did not finish the DOM cases.")
        finally:
            proc.kill(); proc.wait(); srv.shutdown()
    return got

def dom_result(m, with_test):
    if m.get("err"): return False, m["err"]
    if with_test and m.get("pass") is not True: return False, m.get("fail", "failed")
    return True, m.get("out", "")

# ---------- run ----------
problems = 0
def problem(msg):
    global problems; problems += 1; print("PROBLEM " + msg)

py_meta, js_meta, days = schedule(); ids = {l["id"] for l in py_meta + js_meta}
lessons = load_lessons()
dom_cases = []
for L in lessons:
    if L.get("runner") == "dom":
        for part in ("bug", "write"):
            p = L[part]
            dom_cases.append({"key": f"{L['id']}:{part}:sol", "code": p["solution"], "test": p["test"]})
            dom_cases.append({"key": f"{L['id']}:{part}:start", "code": p.get("code", p.get("starter", "")), "test": p["test"]})
        dom_cases.append({"key": f"{L['id']}:predict", "code": L["predict"]["code"], "test": ""})
dom = run_dom_cases(dom_cases) if dom_cases else {}

for L in lessons:
    lid = L["id"]
    for key in ("id", "goal", "cards", "predict", "bug", "write", "quiz"):
        if key not in L: problem(f"{lid} missing {key}")
    if lid not in ids: problem(f"{lid} is not in syllabus.py"); continue
    py = lid.startswith("py"); is_dom = L.get("runner") == "dom"
    if not py and int(lid[2:]) >= 15 and not is_dom: problem(f"{lid} should have \"runner\": \"dom\"")
    if not (3 <= len(L["cards"]) <= 5): problem(f"{lid} has {len(L['cards'])} cards (3-5)")
    if len(L["quiz"]) != 3: problem(f"{lid} needs exactly 3 quiz items")
    for part in ("bug", "write"):
        p = L[part]; stdin = p.get("stdin", ""); start = p.get("code", p.get("starter", ""))
        if is_dom:
            a = dom_result(dom[f"{lid}:{part}:sol"], True); b = dom_result(dom[f"{lid}:{part}:start"], True)
        elif py:
            a = run_py(p["solution"], p["test"], stdin); b = run_py(start, p["test"], stdin)
        else:
            a = run_js(p["solution"], p["test"]); b = run_js(start, p["test"])
        if not a[0] or b[0]:
            problem(f"{lid} {part}: solution passes={a[0]} ({a[1][:160]}) | starter fails={not b[0]}")
    pr = L["predict"]
    if len(pr["opts"]) != 4 or len(set(pr["opts"])) != 4: problem(f"{lid} predict needs 4 different options")
    exp = pr["opts"][pr["ans"]]
    if is_dom: ok, got = dom_result(dom[f"{lid}:predict"], False)
    else: ok, got = (run_py(pr["code"], "") if py else run_js(pr["code"], ""))
    if got.rstrip("\n") != exp:
        problem(f"{lid} predict: got {got!r}, expected {exp!r}")
    for q in L["quiz"]:
        if len(q["opts"]) != 4 or not (0 <= q["ans"] < len(q["opts"])): problem(f"{lid} quiz options/index")
print(f"Checked {len(lessons)} lessons ({len(dom_cases)} DOM cases in Chrome).")
print("All lessons OK." if not problems else f"{problems} problem(s).")
sys.exit(1 if problems else 0)
