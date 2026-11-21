// Runs Python with Pyodide in a worker so an endless loop can be stopped.
// Note: while user code awaits (asyncio.sleep), stdout stays redirected; only one run happens at a time.
importScripts("https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js");
let pyodide = null;
const ready = loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/" })
  .then(p => { pyodide = p; self.postMessage({ type: "ready" }); })
  .catch(e => self.postMessage({ type: "loaderror", message: String(e) }));

const HARNESS = `
import sys, io, json, traceback, ast, inspect
_lines = __stdin.split("\\n") if __stdin else []
def _input(prompt=""):
    print(prompt, end="")
    if not _lines:
        raise EOFError("No more input. Type values in the Input box, one per line.")
    return _lines.pop(0)
_buf = io.StringIO()
_ns = {"__name__": "__main__", "input": _input}
_old = sys.stdout
sys.stdout = _buf
_err = None
try:
    # top-level await is allowed: the browser already runs an event loop, so asyncio.run() can't be used here
    _r = eval(compile(__user_code, "main.py", "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT), _ns)
    if inspect.iscoroutine(_r):
        await _r
except SyntaxError as e:
    _err = f"SyntaxError on line {e.lineno}: {e.msg}"
except BaseException as e:
    _line = None
    for f in traceback.extract_tb(e.__traceback__):
        if f.filename == "main.py":
            _line = f.lineno
    _err = f"{type(e).__name__}: {e}" + (f"  (line {_line})" if _line else "")
finally:
    sys.stdout = _old
_out = _buf.getvalue()
_res = {"out": _out, "err": _err, "pass": None, "fail": None}
if __test and _err is None:
    _ns["_output"] = _out
    _ns["_code"] = __user_code
    try:
        exec(__test, _ns)
        _res["pass"] = True
    except AssertionError as e:
        _res["pass"] = False
        _res["fail"] = str(e) or "A check failed."
    except Exception as e:
        _res["pass"] = False
        _res["fail"] = f"{type(e).__name__}: {e}"
json.dumps(_res)
`;

self.onmessage = async (e) => {
  const { id, code, test, stdin } = e.data;
  await ready;
  if (!pyodide) { self.postMessage({ type: "result", id, err: "Python could not load. Check your connection and try again." }); return; }
  try {
    pyodide.globals.set("__user_code", code);
    pyodide.globals.set("__test", test || "");
    pyodide.globals.set("__stdin", stdin || "");
    // stdlib modules such as sqlite3 are separate packages in Pyodide; load them from the same pinned CDN
    try { await pyodide.loadPackagesFromImports(code); } catch (e) {}
    const res = JSON.parse(await pyodide.runPythonAsync(HARNESS));
    self.postMessage({ type: "result", id, ...res });
  } catch (err) {
    self.postMessage({ type: "result", id, err: String(err) });
  }
};
