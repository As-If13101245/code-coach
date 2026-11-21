# Week 1-2 lessons: Python 1-7, JavaScript 1-7.
# Python tests can use: _output (all printed text), _code (the learner's code).
# JS tests can use: __logs (array of strings, one per console.log), __code, check(cond, message).

LESSONS = [
# ---------------------------------------------------------------- PYTHON 1
{
 "id": "py01",
 "goal": "Run your first Python code and control exactly what print() shows.",
 "cards": [
  {"h": "Python runs top to bottom", "p": "A Python program is a list of instructions. Python runs them one line at a time, from the first line down. If a line has a mistake, Python stops there and shows an error.", "code": "print(\"Line 1\")\nprint(\"Line 2\")"},
  {"h": "print() shows output", "p": "`print()` writes text to the screen. Text goes inside quotes. Give it several values separated by commas and it prints them with a space between.", "code": "print(\"Hello\")\nprint(\"Order\", 1001, \"ready\")   # Order 1001 ready"},
  {"h": "sep= and end=", "p": "`sep` changes what goes between values (default: a space). `end` changes what goes at the end (default: a new line `\\n`).", "code": "print(\"OA\", \"2026\", \"1001\", sep=\"-\")  # OA-2026-1001\nprint(\"Loading\", end=\"...\")\nprint(\"done\")                          # Loading...done"},
  {"h": "Comments", "p": "Anything after `#` is a comment. Python ignores it. Use comments to explain why, not what.", "code": "# Odoo logs use print-like output while debugging\nprint(\"debug\")  # temporary"}
 ],
 "odoo": "Odoo itself is a large Python program. When you start the Odoo server, everything in the terminal log is Python output.",
 "predict": {"code": "print(\"Hello\", \"Odoo\", sep=\"-\")\nprint(\"A\", end=\"\")\nprint(\"B\")", "q": "What does this print?", "opts": ["Hello Odoo\nA\nB", "Hello-Odoo\nAB", "Hello-Odoo\nA B", "Hello-Odoo A B"], "ans": 1, "why": "sep=\"-\" joins the first two words with a dash. end=\"\" stops print from adding a new line, so B appears right after A."},
 "bug": {"task": "This should print exactly two lines: `Welcome, Asif` and `Day 1 of Python`. Fix the two mistakes.", "code": "Print(\"Welcome, Asif\")\nprint(\"Day 1 of Python)", "test": "assert _output == \"Welcome, Asif\\nDay 1 of Python\\n\", \"Output should be exactly two lines\"", "hint": "Python is case-sensitive, and every opening quote needs a closing quote.", "solution": "print(\"Welcome, Asif\")\nprint(\"Day 1 of Python\")"},
 "write": {"task": "Using ONE print() call and sep=, print these three lines:\n`Order OA-1001`\n`Customer: H&M`\n`Qty: 5000`", "starter": "# One print() call only\n", "test": "assert _code.count(\"print(\") == 1, \"Use exactly one print() call\"\nassert _output == \"Order OA-1001\\nCustomer: H&M\\nQty: 5000\\n\", \"Check the three lines\"", "solution": "print(\"Order OA-1001\", \"Customer: H&M\", \"Qty: 5000\", sep=\"\\n\")"},
 "quiz": [
  {"q": "What is the default value of end in print()?", "opts": ["A space", "Nothing", "A new line (\\n)", "A comma"], "ans": 2, "why": "print() ends with a new line unless you change end."},
  {"q": "What does print(\"a\", \"b\", sep=\"\") show?", "opts": ["a b", "ab", "a,b", "a\\nb"], "ans": 1, "why": "An empty separator joins the values with nothing between them."},
  {"q": "Which line is a comment?", "opts": ["// total", "# total", "/* total */", "-- total"], "ans": 1, "why": "Python comments start with #. The others are from other languages."}
 ]
},
# ---------------------------------------------------------------- PYTHON 2
{
 "id": "py02",
 "goal": "Store values in variables and know the basic types.",
 "cards": [
  {"h": "A variable is a name for a value", "p": "`=` means assign: put the value on the right into the name on the left. You can change it later.", "code": "qty = 5000\nqty = qty + 500\nprint(qty)   # 5500"},
  {"h": "Naming rules", "p": "Names use letters, digits and `_`, and can't start with a digit. Python style is snake_case. Names are case-sensitive: `Qty` and `qty` are different.", "code": "unit_price = 0.12   # good\n# 2nd_order = 1    -> SyntaxError\n# unit-price = 1   -> Python reads this as unit minus price"},
  {"h": "Basic types", "p": "`int` whole numbers, `float` decimals, `str` text, `bool` True/False, `None` means no value. `type()` tells you the type.", "code": "print(type(5000))     # <class 'int'>\nprint(type(0.12))     # <class 'float'>\nprint(type(\"H&M\"))    # <class 'str'>\nprint(type(True))     # <class 'bool'>\nprint(type(None))     # <class 'NoneType'>"},
  {"h": "Two handy tricks", "p": "Assign several names at once, and swap two values without a temporary variable.", "code": "a, b = 1, 2\na, b = b, a\nprint(a, b)   # 2 1"}
 ],
 "odoo": "Odoo field types map to these: fields.Integer holds an int, fields.Float a float, fields.Char a str, fields.Boolean a bool. An empty field often reads as False in Odoo, not None.",
 "predict": {"code": "x = 5\ny = x\nx = 10\nprint(y)", "q": "What does this print?", "opts": ["10", "5", "15", "Error"], "ans": 1, "why": "y got the value 5 when it was assigned. Changing x afterwards doesn't change y."},
 "bug": {"task": "This should print the order total, 600.0. Fix the variable name.", "code": "qty = 5000\nunit-price = 0.12\ntotal = qty * unit_price\nprint(total)", "test": "assert abs(total - 600) < 1e-9, \"total should be 600\"\nassert \"600\" in _output", "hint": "A dash is the minus sign in Python. Use an underscore.", "solution": "qty = 5000\nunit_price = 0.12\ntotal = qty * unit_price\nprint(total)"},
 "write": {"task": "Create four variables: `customer` = \"Kontoor\", `qty` = 1200, `price` = 0.35, `is_urgent` = True. Then print the type of each one.", "starter": "", "test": "assert customer == \"Kontoor\" and qty == 1200 and price == 0.35 and is_urgent is True, \"Check the four values\"\nassert isinstance(qty, int) and isinstance(price, float)\nassert \"<class 'str'>\" in _output and \"<class 'bool'>\" in _output, \"Print the type of each variable\"", "solution": "customer = \"Kontoor\"\nqty = 1200\nprice = 0.35\nis_urgent = True\nprint(type(customer))\nprint(type(qty))\nprint(type(price))\nprint(type(is_urgent))"},
 "quiz": [
  {"q": "Which is a valid variable name?", "opts": ["2total", "total-qty", "total_qty", "total qty"], "ans": 2, "why": "Only letters, digits and _, and it can't start with a digit."},
  {"q": "What is type(3.0)?", "opts": ["int", "float", "str", "number"], "ans": 1, "why": "Any number with a decimal point is a float, even 3.0."},
  {"q": "After a, b = 1, 2 and a, b = b, a, what is a?", "opts": ["1", "2", "3", "Error"], "ans": 1, "why": "The values swap, so a becomes 2."}
 ]
},
# ---------------------------------------------------------------- PYTHON 3
{
 "id": "py03",
 "goal": "Do arithmetic correctly, including the operators that surprise beginners.",
 "cards": [
  {"h": "The operators", "p": "`+ - *` as usual. `/` always gives a float. `//` is floor division (whole part). `%` is the remainder. `**` is power.", "code": "print(7 / 2)    # 3.5\nprint(7 // 2)   # 3\nprint(7 % 2)    # 1\nprint(2 ** 10)  # 1024"},
  {"h": "Order of operations", "p": "`**` first, then `* / // %`, then `+ -`. Use brackets when in doubt; they also make code easier to read.", "code": "print(2 + 3 * 4)     # 14\nprint((2 + 3) * 4)   # 20"},
  {"h": "Float surprises", "p": "Computers store decimals in binary, so some results are slightly off. Use round() for display, and never compare floats with == when money matters.", "code": "print(0.1 + 0.2)            # 0.30000000000000004\nprint(round(0.1 + 0.2, 2))  # 0.3"},
  {"h": "Update in place", "p": "`+=`, `-=`, `*=` and friends update a variable using its current value.", "code": "stock = 1000\nstock -= 250\nstock *= 2\nprint(stock)   # 1500"}
 ],
 "odoo": "Odoo avoids float errors in money with float_round() and float_compare() using the currency's precision. Now you know why they exist.",
 "predict": {"code": "print(7 // 2, 7 % 2, 2 ** 3)", "q": "What does this print?", "opts": ["3.5 1 6", "3 1 8", "3 0 8", "4 1 8"], "ans": 1, "why": "7 // 2 is 3, the remainder of 7 / 2 is 1, and 2 ** 3 is 8."},
 "bug": {"task": "The average of three shipments (10, 20 and 30) should be 20.0, but this prints 40.0. Fix it.", "code": "a, b, c = 10, 20, 30\navg = a + b + c / 3\nprint(avg)", "test": "assert avg == 20.0, \"avg should be 20.0\"", "hint": "Division happens before addition. Group the sum.", "solution": "a, b, c = 10, 20, 30\navg = (a + b + c) / 3\nprint(avg)"},
 "write": {"task": "A production run made `total_pcs = 12345` zippers. They are packed in boxes of `box_size = 500`. Calculate `boxes` (full boxes only) and `left` (pieces left over), then print: `24 boxes, 345 left`", "starter": "total_pcs = 12345\nbox_size = 500\n", "test": "assert boxes == 24 and left == 345, \"boxes should be 24 and left 345\"\nassert _output.strip() == \"24 boxes, 345 left\", \"Print: 24 boxes, 345 left\"", "solution": "total_pcs = 12345\nbox_size = 500\nboxes = total_pcs // box_size\nleft = total_pcs % box_size\nprint(boxes, \"boxes,\", left, \"left\")"},
 "quiz": [
  {"q": "What is 10 / 5 in Python 3?", "opts": ["2", "2.0", "2.5", "Error"], "ans": 1, "why": "/ always returns a float."},
  {"q": "What is 17 % 5?", "opts": ["3", "2", "3.4", "12"], "ans": 1, "why": "17 = 3 × 5 + 2, so the remainder is 2."},
  {"q": "What is 2 + 2 ** 3?", "opts": ["64", "10", "16", "12"], "ans": 1, "why": "Power first: 2 ** 3 = 8, then 2 + 8 = 10."}
 ]
},
# ---------------------------------------------------------------- PYTHON 4
{
 "id": "py04",
 "goal": "Build, measure, index and slice strings.",
 "cards": [
  {"h": "Making strings", "p": "Use single or double quotes. Triple quotes allow several lines. `\\n` is a new line and `\\t` a tab.", "code": "a = 'H&M'\nb = \"Kohl's\"   # double quotes let you use '\nc = \"\"\"Line 1\nLine 2\"\"\""},
  {"h": "Joining and repeating", "p": "`+` joins strings, `*` repeats them, `len()` counts characters. You can't add a str and an int directly.", "code": "print(\"OA-\" + \"1001\")   # OA-1001\nprint(\"-\" * 10)          # ----------\nprint(len(\"ZIPPER\"))     # 6\n# print(\"Qty: \" + 5000)  -> TypeError"},
  {"h": "Indexing", "p": "Each character has a position starting at 0. Negative positions count from the end: -1 is the last.", "code": "s = \"ZIPPER\"\nprint(s[0])    # Z\nprint(s[-1])   # R"},
  {"h": "Slicing", "p": "`s[start:stop]` takes characters from start up to, but not including, stop. Leave one side empty to go to the edge.", "code": "s = \"OA-2026-1001\"\nprint(s[3:7])   # 2026\nprint(s[:2])    # OA\nprint(s[-4:])   # 1001"},
  {"h": "Strings can't be changed", "p": "Strings are immutable. You don't edit one; you build a new one.", "code": "s = \"zipper\"\n# s[0] = \"Z\"   -> TypeError\ns = \"Z\" + s[1:]\nprint(s)   # Zipper"}
 ],
 "odoo": "Odoo record names such as 'S00042' or 'WH/OUT/00017' are strings. Slicing like name[-5:] is a quick way to pull out the number part.",
 "predict": {"code": "s = \"ZIPPER\"\nprint(s[1:4], s[-1])", "q": "What does this print?", "opts": ["ZIP R", "IPP R", "IPPE R", "IPP E"], "ans": 1, "why": "Positions 1, 2 and 3 are I, P, P (the stop index 4 is not included). s[-1] is the last letter, R."},
 "bug": {"task": "`year` should be \"2026\". Fix the slice.", "code": "code = \"OA-2026-1001\"\nyear = code[3:6]\nprint(year)", "test": "assert year == \"2026\", \"year should be 2026\"", "hint": "The stop position is not included. Count positions from 0.", "solution": "code = \"OA-2026-1001\"\nyear = code[3:7]\nprint(year)"},
 "write": {"task": "From `po = \"PO-HM-88412\"`, use slicing to create `brand` (\"HM\") and `number` (\"88412\"), then print both.", "starter": "po = \"PO-HM-88412\"\n", "test": "assert brand == \"HM\", \"brand should be HM\"\nassert number == \"88412\", \"number should be 88412\"\nassert \"[\" in _code, \"Use slicing\"", "solution": "po = \"PO-HM-88412\"\nbrand = po[3:5]\nnumber = po[-5:]\nprint(brand, number)"},
 "quiz": [
  {"q": "What is \"Python\"[0]?", "opts": ["P", "y", "n", "Error"], "ans": 0, "why": "Indexing starts at 0."},
  {"q": "What is \"Python\"[2:]?", "opts": ["Py", "thon", "ython", "tho"], "ans": 1, "why": "From position 2 to the end: t, h, o, n."},
  {"q": "What happens with \"Qty: \" + 5?", "opts": ["Qty: 5", "TypeError", "Qty:5", "Qty: 55"], "ans": 1, "why": "You can't add str and int. Use str(5) or an f-string."}
 ]
},
# ---------------------------------------------------------------- PYTHON 5
{
 "id": "py05",
 "goal": "Clean and format text with string methods and f-strings.",
 "cards": [
  {"h": "Case and spaces", "p": "Methods return a new string. `strip()` removes spaces at both ends.", "code": "s = \"  kontoor  \"\nprint(s.strip())          # kontoor\nprint(s.strip().upper())  # KONTOOR\nprint(\"gap inc\".title())  # Gap Inc"},
  {"h": "Find and replace", "p": "`replace(old, new)`, `find()` gives a position or -1, `startswith()` / `endswith()` give True or False.", "code": "code = \"WH/OUT/00017\"\nprint(code.replace(\"/\", \"-\"))   # WH-OUT-00017\nprint(code.startswith(\"WH\"))    # True\nprint(code.find(\"OUT\"))         # 3"},
  {"h": "split() and join()", "p": "`split(sep)` cuts a string into a list. `sep.join(list)` glues a list back into one string.", "code": "parts = \"PO-HM-88412\".split(\"-\")\nprint(parts)            # ['PO', 'HM', '88412']\nprint(\" / \".join(parts)) # PO / HM / 88412"},
  {"h": "f-strings", "p": "Put `f` before the quotes, then any expression inside `{}`. Add a format after `:` such as `.2f` (2 decimals) or `,` (thousands).", "code": "qty, price = 12500, 0.3456\nprint(f\"Qty: {qty:,}\")                # Qty: 12,500\nprint(f\"Total: {qty * price:.2f}\")    # Total: 4320.00"}
 ],
 "odoo": "Odoo uses f-strings and _() for messages. In SQL, never build queries with f-strings; you'll learn why in the PostgreSQL lesson.",
 "predict": {"code": "name = \"  kohl's \"\nprint(name.strip().title())", "q": "What does this print?", "opts": ["Kohl's", "Kohl'S", "KOHL'S", "kohl's"], "ans": 1, "why": "title() capitalises the letter after any non-letter, including an apostrophe. A real-world gotcha with brand names."},
 "bug": {"task": "This should print `Total: 1234.50`. Fix it.", "code": "total = 1234.5\nprint(\"Total: {total:.2f}\")", "test": "assert _output == \"Total: 1234.50\\n\", \"Should print Total: 1234.50\"", "hint": "Something is missing before the opening quote.", "solution": "total = 1234.5\nprint(f\"Total: {total:.2f}\")"},
 "write": {"task": "Given `raw = \"h&m, gap, carter's, kohl's\"`, build `result` = \"H&M | GAP | CARTER'S | KOHL'S\" using split(), upper() and join(), then print it.", "starter": "raw = \"h&m, gap, carter's, kohl's\"\n", "test": "assert result == \"H&M | GAP | CARTER'S | KOHL'S\", \"Check the result string\"\nassert \"join\" in _code and \"split\" in _code, \"Use split() and join()\"", "solution": "raw = \"h&m, gap, carter's, kohl's\"\nresult = \" | \".join(raw.upper().split(\", \"))\nprint(result)"},
 "quiz": [
  {"q": "What does \"a,b,c\".split(\",\") return?", "opts": ["\"abc\"", "['a', 'b', 'c']", "('a','b','c')", "['a,b,c']"], "ans": 1, "why": "split() returns a list of the pieces."},
  {"q": "f\"{3.14159:.2f}\" gives…", "opts": ["3.14", "3.1", "3.15", "3.14159"], "ans": 0, "why": ".2f rounds to 2 decimal places."},
  {"q": "What does \"OA\".find(\"X\") return?", "opts": ["0", "None", "-1", "Error"], "ans": 2, "why": "find() returns -1 when the text isn't there. (index() would raise an error.)"}
 ]
},
# ---------------------------------------------------------------- PYTHON 6
{
 "id": "py06",
 "goal": "Read input and convert between types safely.",
 "cards": [
  {"h": "input() always gives a string", "p": "`input()` waits for the user and returns what they typed, as a str, even if they typed a number. In this app, type input lines in the Input box before you run.", "code": "qty = input(\"Qty? \")\nprint(type(qty))   # <class 'str'>"},
  {"h": "Converting", "p": "`int()`, `float()` and `str()` convert values. Converting text that isn't a number raises ValueError.", "code": "print(int(\"42\") + 1)     # 43\nprint(float(\"0.35\"))     # 0.35\nprint(str(5000) + \" pcs\") # 5000 pcs\n# int(\"12.5\")  -> ValueError\nprint(int(float(\"12.5\"))) # 12"},
  {"h": "The bool() trap", "p": "Any non-empty string is True, even \"False\" and \"0\". Only the empty string is False.", "code": "print(bool(\"False\"))   # True\nprint(bool(\"\"))        # False"}
 ],
 "odoo": "Values from web forms, CSV imports and XML-RPC often arrive as strings. Converting them correctly is daily work in integrations.",
 "predict": {"code": "print(\"5\" + \"3\", int(\"5\") + int(\"3\"))", "q": "What does this print?", "opts": ["8 8", "53 8", "53 53", "8 53"], "ans": 1, "why": "Adding two strings joins them (\"53\"). Adding two ints adds them (8)."},
 "bug": {"task": "With the input 10, this should print 20, but it prints 1010. Fix it.", "code": "qty = input()\nprint(qty * 2)", "stdin": "10", "test": "assert _output.strip() == \"20\", \"Should print 20\"", "hint": "Convert the text to a number first.", "solution": "qty = int(input())\nprint(qty * 2)"},
 "write": {"task": "Read two inputs: a price (a decimal) and a quantity (a whole number). Print the total with 2 decimals, like `Total: 420.00`.", "starter": "", "stdin": "0.35\n1200", "test": "assert _output.strip().endswith(\"Total: 420.00\"), \"With 0.35 and 1200 it should print Total: 420.00\"\nassert \"float(\" in _code and \"int(\" in _code, \"Convert with float() and int()\"", "solution": "price = float(input())\nqty = int(input())\ntotal = price * qty\nprint(f\"Total: {total:.2f}\")"},
 "quiz": [
  {"q": "What type does input() return?", "opts": ["int", "str", "It depends on what was typed", "float"], "ans": 1, "why": "Always str."},
  {"q": "What is bool(\"0\")?", "opts": ["False", "True", "0", "Error"], "ans": 1, "why": "\"0\" is a non-empty string, so it's True."},
  {"q": "What does int(\"3.7\") do?", "opts": ["3", "4", "3.7", "ValueError"], "ans": 3, "why": "int() can't read a decimal string. Use int(float(\"3.7\"))."}
 ]
},
# ---------------------------------------------------------------- PYTHON 7
{
 "id": "py07",
 "goal": "Write true/false logic with comparisons, and, or, not.",
 "cards": [
  {"h": "Comparisons give True or False", "p": "`== != < > <= >=`. `==` compares values; `=` assigns.", "code": "qty = 500\nprint(qty == 500)   # True\nprint(qty != 500)   # False\nprint(qty >= 1000)  # False"},
  {"h": "and, or, not", "p": "`and`: both must be True. `or`: at least one True. `not` flips it. Python stops early once it knows the answer (short-circuit).", "code": "shipped, late = True, False\nprint(shipped and not late)   # True\nprint(late or shipped)        # True"},
  {"h": "Chained comparisons", "p": "Python lets you write ranges naturally.", "code": "qty = 300\nprint(100 <= qty <= 500)   # True"},
  {"h": "Truthy and falsy", "p": "In conditions, these count as False: `0`, `0.0`, `\"\"`, `[]`, `{}`, `None`. Everything else is True. To test for None, use `is None`.", "code": "note = \"\"\nprint(bool(note))      # False\nvalue = None\nprint(value is None)   # True"}
 ],
 "odoo": "Odoo empty fields are falsy (often False), so Odoo code checks `if record.partner_id:` instead of comparing to None. Domains like ('qty', '>=', 100) are comparisons too.",
 "predict": {"code": "print(bool(\"\"), bool(\"0\"), 0 == False)", "q": "What does this print?", "opts": ["False False False", "False True True", "True True False", "False True False"], "ans": 1, "why": "An empty string is falsy; \"0\" is a non-empty string, so it's truthy; and 0 equals False in Python."},
 "bug": {"task": "`ok` should be True when qty is between 100 and 500 (inclusive). Fix the line.", "code": "qty = 500\nok = qty > 100 and < 500\nprint(ok)", "test": "assert ok is True, \"ok should be True for 500\"", "hint": "Each side of and must be a full comparison, or use a chained comparison with <=.", "solution": "qty = 500\nok = 100 <= qty <= 500\nprint(ok)"},
 "write": {"task": "An order is late if it was shipped AND delivered after the promised day. Given the variables, create `late` with one boolean expression and print it. (Here it should be True.)", "starter": "promised_day = 10\ndelivered_day = 12\nshipped = True\n", "test": "assert late is True, \"late should be True\"\nassert \"and\" in _code, \"Use and\"", "solution": "promised_day = 10\ndelivered_day = 12\nshipped = True\nlate = shipped and delivered_day > promised_day\nprint(late)"},
 "quiz": [
  {"q": "What is not (3 > 2)?", "opts": ["True", "False", "None", "Error"], "ans": 1, "why": "3 > 2 is True, and not flips it."},
  {"q": "Which value is truthy?", "opts": ["[]", "0", "\" \" (a space)", "None"], "ans": 2, "why": "A string containing a space isn't empty, so it's truthy."},
  {"q": "Best way to check if x is None?", "opts": ["x == None", "x is None", "not x", "x = None"], "ans": 1, "why": "is None is the correct, reliable check. not x is also True for 0 and \"\"."}
 ]
},
# ---------------------------------------------------------------- JS 1
{
 "id": "js01",
 "goal": "Run JavaScript and use console.log to see what your code does.",
 "cards": [
  {"h": "Where JavaScript runs", "p": "JavaScript runs in every web browser, and on servers with Node.js. Odoo's whole web interface, including OWL, is JavaScript running in your browser.", "code": "console.log(\"Hello from JavaScript\");"},
  {"h": "console.log()", "p": "`console.log()` prints to the console. Several values are printed with spaces between them. In this app, each call becomes one output line.", "code": "console.log(\"Order\", 1001, \"ready\");   // Order 1001 ready"},
  {"h": "Statements and semicolons", "p": "Each instruction is a statement, usually ending with `;`. JavaScript can insert them for you, but writing them avoids rare bugs. Comments use `//` or `/* … */`.", "code": "// a comment\nlet qty = 5000;   /* another comment */\nconsole.log(qty);"},
  {"h": "typeof", "p": "`typeof` tells you a value's type as a string.", "code": "console.log(typeof 5000);    // number\nconsole.log(typeof \"H&M\");   // string\nconsole.log(typeof true);    // boolean"}
 ],
 "odoo": "In Odoo, open the browser's developer tools (F12 → Console) to see logs from OWL components and errors from the web client.",
 "predict": {"code": "console.log(\"2\" + 2, 2 + 2);", "q": "What does this print?", "opts": ["4 4", "22 4", "\"22\" 4", "Error"], "ans": 1, "why": "If either side of + is a string, JavaScript joins them as text: \"22\". 2 + 2 is the number 4."},
 "bug": {"task": "This should print two lines: `Welcome, Asif` and `Day 1 of JavaScript`. Fix the two mistakes.", "code": "Console.log(\"Welcome, Asif\");\nconsole.log(\"Day 1 of JavaScript);", "test": "check(__logs[0] === \"Welcome, Asif\" && __logs[1] === \"Day 1 of JavaScript\", \"Print the two lines exactly\");", "hint": "JavaScript is case-sensitive, and every quote must be closed.", "solution": "console.log(\"Welcome, Asif\");\nconsole.log(\"Day 1 of JavaScript\");"},
 "write": {"task": "Print these three lines, one console.log each:\n`Order OA-1001`\n`Customer: H&M`\n`Qty: 5000`", "starter": "", "test": "check(__logs.join(\"|\") === \"Order OA-1001|Customer: H&M|Qty: 5000\", \"Print the three lines in order\");", "solution": "console.log(\"Order OA-1001\");\nconsole.log(\"Customer: H&M\");\nconsole.log(\"Qty: 5000\");"},
 "quiz": [
  {"q": "What does typeof 3.5 return?", "opts": ["\"float\"", "\"number\"", "\"decimal\"", "\"int\""], "ans": 1, "why": "JavaScript has one number type for whole numbers and decimals."},
  {"q": "Which is a JavaScript comment?", "opts": ["# note", "// note", "-- note", "<!-- note -->"], "ans": 1, "why": "// starts a one-line comment in JavaScript."},
  {"q": "Where does OWL code run?", "opts": ["On the Odoo server, in Python", "In the browser", "In PostgreSQL", "Only in Node.js"], "ans": 1, "why": "OWL is a front-end framework; it runs in the user's browser."}
 ]
},
# ---------------------------------------------------------------- JS 2
{
 "id": "js02",
 "goal": "Declare variables with let and const, and know JavaScript's types.",
 "cards": [
  {"h": "let and const", "p": "`const` for values you won't reassign (the default choice). `let` for values that change. Avoid the old `var`.", "code": "const customer = \"Kontoor\";\nlet qty = 1200;\nqty = qty + 300;   // fine\n// customer = \"GAP\";  -> TypeError"},
  {"h": "The types", "p": "Primitives: `number`, `string`, `boolean`, `undefined` (declared but no value), `null` (deliberately empty), plus `bigint` and `symbol`. Everything else is an object.", "code": "let note;\nconsole.log(note);          // undefined\nconsole.log(typeof null);   // object  (a famous old bug)"},
  {"h": "const doesn't freeze objects", "p": "`const` stops you reassigning the name, but you can still change the contents of an object or array.", "code": "const items = [\"zipper\"];\nitems.push(\"slider\");\nconsole.log(items.length);   // 2"}
 ],
 "odoo": "Odoo's JavaScript style uses const by default and let only when a value changes. You'll see this in every OWL component.",
 "owl2": "",
 "predict": {"code": "const a = [1];\na.push(2);\nconsole.log(a.length, typeof null);", "q": "What does this print?", "opts": ["1 null", "2 object", "Error", "2 null"], "ans": 1, "why": "const allows changing an array's contents, so the length is 2. typeof null is \"object\", a long-standing quirk."},
 "bug": {"task": "This crashes. Make it run so `qty` ends up as 200.", "code": "const qty = 100;\nqty = 200;\nconsole.log(qty);", "test": "check(qty === 200, \"qty should be 200\");", "hint": "A value that changes needs a different keyword.", "solution": "let qty = 100;\nqty = 200;\nconsole.log(qty);"},
 "write": {"task": "Declare `customer` = \"Kontoor\" with const and `qty` = 1200 with let. Increase qty by 300, then log `typeof qty` and `qty` in one console.log (it should print `number 1500`).", "starter": "", "test": "check(customer === \"Kontoor\", \"customer should be Kontoor\");\ncheck(qty === 1500, \"qty should be 1500\");\ncheck(__logs.includes(\"number 1500\"), \"Log: number 1500\");\ncheck(/const\\s+customer/.test(__code) && /let\\s+qty/.test(__code), \"Use const for customer and let for qty\");", "solution": "const customer = \"Kontoor\";\nlet qty = 1200;\nqty += 300;\nconsole.log(typeof qty, qty);"},
 "quiz": [
  {"q": "Which should you use by default?", "opts": ["var", "let", "const", "Nothing"], "ans": 2, "why": "Use const unless you need to reassign."},
  {"q": "What is a declared variable with no value?", "opts": ["null", "undefined", "0", "\"\""], "ans": 1, "why": "JavaScript gives it undefined."},
  {"q": "Can you push into a const array?", "opts": ["No, it's constant", "Yes", "Only once", "Only with var"], "ans": 1, "why": "const locks the name, not the contents."}
 ]
},
# ---------------------------------------------------------------- JS 3
{
 "id": "js03",
 "goal": "Work with strings and build text with template literals.",
 "cards": [
  {"h": "Template literals", "p": "Backticks allow `${…}` expressions inside the text and multi-line strings. They're the JavaScript version of Python's f-strings.", "code": "const qty = 1200, price = 0.35;\nconsole.log(`Total: ${qty * price}`);   // Total: 420"},
  {"h": "Length, index and slice", "p": "Positions start at 0. `slice(start, end)` excludes end. `at(-1)` gives the last character.", "code": "const s = \"ZIPPER\";\nconsole.log(s.length, s[0], s.at(-1));   // 6 Z R\nconsole.log(s.slice(1, 4));              // IPP"},
  {"h": "Useful methods", "p": "Like Python, these return new strings.", "code": "console.log(\"  gap \".trim().toUpperCase());     // GAP\nconsole.log(\"WH/OUT/17\".includes(\"OUT\"));     // true\nconsole.log(\"PO-HM-88412\".split(\"-\"));         // [\"PO\",\"HM\",\"88412\"]\nconsole.log(\"7\".padStart(5, \"0\"));            // 00007"}
 ],
 "odoo": "OWL templates handle most text, but you'll use template literals for notification messages and building values in JavaScript code.",
 "predict": {"code": "const s = \"ZIPPER\";\nconsole.log(s.slice(1, 4), s.at(-1));", "q": "What does this print?", "opts": ["ZIP R", "IPP R", "IPPE R", "IPP E"], "ans": 1, "why": "slice(1, 4) gives positions 1–3: IPP. at(-1) is the last character, R."},
 "bug": {"task": "`msg` should be \"Total: 420\". Fix it.", "code": "const total = 420;\nconst msg = \"Total: ${total}\";\nconsole.log(msg);", "test": "check(msg === \"Total: 420\", \"msg should be Total: 420\");", "hint": "${} only works inside one kind of quote.", "solution": "const total = 420;\nconst msg = `Total: ${total}`;\nconsole.log(msg);"},
 "write": {"task": "From `po = \"PO-HM-88412\"`, use split(\"-\") to get the brand and number, then build `label` = \"HM #88412\" with a template literal and log it.", "starter": "const po = \"PO-HM-88412\";\n", "test": "check(label === \"HM #88412\", \"label should be HM #88412\");\ncheck(__code.includes(\"split\") && __code.includes(\"`\"), \"Use split() and a template literal\");", "solution": "const po = \"PO-HM-88412\";\nconst parts = po.split(\"-\");\nconst label = `${parts[1]} #${parts[2]}`;\nconsole.log(label);"},
 "quiz": [
  {"q": "Which creates a template literal?", "opts": ["'text'", "\"text\"", "`text`", "<text>"], "ans": 2, "why": "Template literals use backticks."},
  {"q": "\"abc\".at(-1) is…", "opts": ["a", "c", "undefined", "Error"], "ans": 1, "why": "at(-1) gives the last character."},
  {"q": "\"7\".padStart(3, \"0\") is…", "opts": ["700", "007", "0007", "7"], "ans": 1, "why": "It pads on the left until the length is 3."}
 ]
},
# ---------------------------------------------------------------- JS 4
{
 "id": "js04",
 "goal": "Make decisions with if/else, and avoid JavaScript's equality traps.",
 "cards": [
  {"h": "if / else if / else", "p": "Conditions go in brackets, blocks in braces.", "code": "const qty = 2500;\nif (qty >= 10000) {\n  console.log(\"large\");\n} else if (qty >= 1000) {\n  console.log(\"medium\");\n} else {\n  console.log(\"small\");\n}"},
  {"h": "Always use ===", "p": "`==` converts types before comparing, which causes surprises. `===` compares value and type. Use `===` and `!==`.", "code": "console.log(0 == \"\");    // true  (surprise!)\nconsole.log(0 === \"\");   // false"},
  {"h": "Truthy and falsy", "p": "Falsy values: `false`, `0`, `\"\"`, `null`, `undefined`, `NaN`. Unlike Python, an empty array `[]` and empty object `{}` are truthy!", "code": "if ([]) console.log(\"empty array is truthy\");"},
  {"h": "Shortcuts", "p": "The ternary `cond ? a : b` picks a value. `??` gives a default only for null/undefined.", "code": "const late = true;\nconsole.log(late ? \"Late\" : \"On time\");   // Late\nconst note = null;\nconsole.log(note ?? \"no note\");           // no note"}
 ],
 "odoo": "OWL templates use the same idea: t-if=\"props.record.data.state === 'done'\". Strict equality avoids bugs with Odoo's false-for-empty fields.",
 "predict": {"code": "console.log(0 == \"\", 0 === \"\", null ?? \"none\");", "q": "What does this print?", "opts": ["false false null", "true false none", "true true none", "false false none"], "ans": 1, "why": "== converts \"\" to 0, so it's true; === also checks the type, so it's false. null ?? \"none\" gives the default."},
 "bug": {"task": "status is \"on time\", but this logs \"Late!\". Fix the condition.", "code": "const status = \"on time\";\nif (status = \"late\") {\n  console.log(\"Late!\");\n} else {\n  console.log(\"On time\");\n}", "test": "check(__logs[0] === \"On time\", \"It should log On time\");", "hint": "One = assigns. Comparing needs three.", "solution": "const status = \"on time\";\nif (status === \"late\") {\n  console.log(\"Late!\");\n} else {\n  console.log(\"On time\");\n}"},
 "write": {"task": "Given `qty = 2500`, set `size` to \"large\" if qty >= 10000, \"medium\" if qty >= 1000, otherwise \"small\". Log size.", "starter": "const qty = 2500;\nlet size;\n", "test": "check(size === \"medium\", \"For 2500, size should be medium\");\ncheck(__code.includes(\"if\") || __code.includes(\"?\"), \"Use if/else or the ternary\");", "solution": "const qty = 2500;\nlet size;\nif (qty >= 10000) {\n  size = \"large\";\n} else if (qty >= 1000) {\n  size = \"medium\";\n} else {\n  size = \"small\";\n}\nconsole.log(size);"},
 "quiz": [
  {"q": "Is [] truthy in JavaScript?", "opts": ["Yes", "No", "Only in strict mode", "Error"], "ans": 0, "why": "Empty arrays and objects are truthy in JavaScript (unlike Python)."},
  {"q": "What is 0 ?? 5?", "opts": ["0", "5", "null", "false"], "ans": 0, "why": "?? only replaces null or undefined, and 0 is neither. (0 || 5 would give 5.)"},
  {"q": "Which comparison should you use?", "opts": ["==", "===", "=", "=>"], "ans": 1, "why": "=== compares value and type without conversion."}
 ]
},
# ---------------------------------------------------------------- JS 5
{
 "id": "js05",
 "goal": "Repeat work with for, while, for...of and for...in.",
 "cards": [
  {"h": "Classic for", "p": "Start; keep going while true; step.", "code": "for (let i = 1; i <= 3; i++) {\n  console.log(`Box ${i}`);\n}"},
  {"h": "while", "p": "Runs while a condition is true. Make sure it eventually becomes false.", "code": "let stock = 1000;\nwhile (stock > 0) {\n  stock -= 400;\n}\nconsole.log(stock);   // -200"},
  {"h": "for...of for values", "p": "The everyday loop over arrays and strings.", "code": "const brands = [\"H&M\", \"GAP\"];\nfor (const b of brands) {\n  console.log(b);\n}"},
  {"h": "for...in for object keys", "p": "Loops over property names. Use for...of for arrays and for...in (or Object.keys) for objects. `break` stops; `continue` skips.", "code": "const order = { brand: \"H&M\", qty: 1200 };\nfor (const key in order) {\n  console.log(key, order[key]);\n}"}
 ],
 "odoo": "In OWL templates, t-foreach does the looping for you. In JavaScript code you'll use for...of on record lists from the orm service.",
 "predict": {"code": "let s = \"\";\nfor (let i = 0; i < 3; i++) {\n  s += i;\n}\nconsole.log(s);", "q": "What does this print?", "opts": ["3", "012", "0123", "6"], "ans": 1, "why": "s starts as a string, so each number is appended as text: \"0\", \"01\", \"012\"."},
 "bug": {"task": "This should add 1 to 5 and give 15, but gives 10. Fix the loop.", "code": "let total = 0;\nfor (let i = 1; i < 5; i++) {\n  total += i;\n}\nconsole.log(total);", "test": "check(total === 15, \"total should be 15\");", "hint": "Does the loop include 5?", "solution": "let total = 0;\nfor (let i = 1; i <= 5; i++) {\n  total += i;\n}\nconsole.log(total);"},
 "write": {"task": "Given `orders = [1200, 500, 3400, 800]`, use a for...of loop to count how many are over 1000. Store it in `count` and log it.", "starter": "const orders = [1200, 500, 3400, 800];\nlet count = 0;\n", "test": "check(count === 2, \"count should be 2\");\ncheck(/for\\s*\\(\\s*(const|let)\\s+\\w+\\s+of/.test(__code), \"Use for...of\");", "solution": "const orders = [1200, 500, 3400, 800];\nlet count = 0;\nfor (const q of orders) {\n  if (q > 1000) count++;\n}\nconsole.log(count);"},
 "quiz": [
  {"q": "Best loop for the values of an array?", "opts": ["for...in", "for...of", "while", "do...while"], "ans": 1, "why": "for...of gives each value directly."},
  {"q": "What does continue do?", "opts": ["Stops the loop", "Skips to the next round", "Restarts the loop", "Nothing"], "ans": 1, "why": "It skips the rest of this round and continues with the next."},
  {"q": "for (const k in {a:1, b:2}) gives k as…", "opts": ["1 then 2", "\"a\" then \"b\"", "[a,1] pairs", "Error"], "ans": 1, "why": "for...in loops over keys."}
 ]
},
# ---------------------------------------------------------------- JS 6
{
 "id": "js06",
 "goal": "Use arrays and the methods you'll use daily: map, filter, reduce, find.",
 "cards": [
  {"h": "Arrays basics", "p": "`push` adds to the end, `pop` removes from the end, `includes` checks membership, `indexOf` finds a position.", "code": "const qtys = [1200, 500];\nqtys.push(3400);\nconsole.log(qtys.length, qtys.includes(500));   // 3 true"},
  {"h": "map and filter", "p": "`map` makes a new array by transforming each item. `filter` keeps items that pass a test. Neither changes the original.", "code": "const qtys = [1200, 500, 3400];\nconsole.log(qtys.map(q => q * 2));        // [2400,1000,6800]\nconsole.log(qtys.filter(q => q > 1000));  // [1200,3400]"},
  {"h": "reduce and find", "p": "`reduce` combines everything into one value. `find` returns the first match or undefined.", "code": "const qtys = [1200, 500, 3400];\nconsole.log(qtys.reduce((sum, q) => sum + q, 0));   // 5100\nconsole.log(qtys.find(q => q < 1000));              // 500"},
  {"h": "The sort() trap", "p": "By default, sort() compares items as strings! For numbers, pass a compare function.", "code": "console.log([10, 9, 1].sort());                // [1,10,9]\nconsole.log([10, 9, 1].sort((a, b) => a - b)); // [1,9,10]"}
 ],
 "odoo": "Records from the orm service arrive as arrays of objects. map/filter/reduce are how you'll compute totals and lists before showing them in OWL.",
 "predict": {"code": "console.log([10, 9, 1].sort());", "q": "What does this print? (Arrays print like JSON here.)", "opts": ["[1,9,10]", "[1,10,9]", "[10,9,1]", "[9,10,1]"], "ans": 1, "why": "Without a compare function, sort() compares \"10\", \"9\", \"1\" as text, and \"10\" comes before \"9\"."},
 "bug": {"task": "`qtys` should end up sorted as numbers: [5, 40, 300, 1200]. Fix it.", "code": "const qtys = [300, 5, 1200, 40];\nqtys.sort();\nconsole.log(qtys);", "test": "check(JSON.stringify(qtys) === \"[5,40,300,1200]\", \"qtys should be [5,40,300,1200]\");", "hint": "Give sort() a function that subtracts.", "solution": "const qtys = [300, 5, 1200, 40];\nqtys.sort((a, b) => a - b);\nconsole.log(qtys);"},
 "write": {"task": "Using `orders`, create `total` (the sum of all qty, using reduce) and `brands` (an array of brand names, using map). Log both.", "starter": "const orders = [\n  { brand: \"H&M\", qty: 1200 },\n  { brand: \"GAP\", qty: 500 },\n  { brand: \"Kohl's\", qty: 3400 },\n];\n", "test": "check(total === 5100, \"total should be 5100\");\ncheck(JSON.stringify(brands) === JSON.stringify([\"H&M\",\"GAP\",\"Kohl's\"]), \"brands should be [H&M, GAP, Kohl's]\");\ncheck(__code.includes(\"reduce\") && __code.includes(\"map\"), \"Use reduce and map\");", "solution": "const orders = [\n  { brand: \"H&M\", qty: 1200 },\n  { brand: \"GAP\", qty: 500 },\n  { brand: \"Kohl's\", qty: 3400 },\n];\nconst total = orders.reduce((sum, o) => sum + o.qty, 0);\nconst brands = orders.map(o => o.brand);\nconsole.log(total, brands);"},
 "quiz": [
  {"q": "Does map() change the original array?", "opts": ["Yes", "No, it returns a new one", "Only for numbers", "Only if you use const"], "ans": 1, "why": "map, filter and reduce return new values."},
  {"q": "What does find() return if nothing matches?", "opts": ["null", "-1", "undefined", "[]"], "ans": 2, "why": "find returns undefined. (findIndex returns -1.)"},
  {"q": "[3,1,2].filter(n => n > 1) gives…", "opts": ["[3,2]", "[1]", "true", "2"], "ans": 0, "why": "filter keeps the items that pass: 3 and 2."}
 ]
},
# ---------------------------------------------------------------- JS 7
{
 "id": "js07",
 "goal": "Create and use objects, and understand that objects are shared by reference.",
 "cards": [
  {"h": "Object literals", "p": "Objects group named values (properties). Read them with dot or bracket notation.", "code": "const order = { brand: \"H&M\", qty: 1200 };\nconsole.log(order.brand);     // H&M\nconsole.log(order[\"qty\"]);    // 1200"},
  {"h": "Brackets for dynamic keys", "p": "When the key is in a variable, you must use brackets. `order.field` looks for a key literally called \"field\".", "code": "const field = \"qty\";\nconsole.log(order[field]);   // 1200\nconsole.log(order.field);    // undefined"},
  {"h": "Add, change, delete, list", "p": "Objects are flexible. `Object.keys/values/entries` turn them into arrays.", "code": "order.status = \"shipped\";\ndelete order.qty;\nconsole.log(Object.keys(order));   // [\"brand\",\"status\"]"},
  {"h": "Objects are shared, not copied", "p": "Assigning an object to another name doesn't copy it. Both names point to the same object. Use spread `{ ...obj }` for a shallow copy.", "code": "const a = { qty: 1 };\nconst b = a;\nb.qty = 5;\nconsole.log(a.qty);          // 5\nconst c = { ...a, qty: 9 };\nconsole.log(a.qty, c.qty);   // 5 9"}
 ],
 "odoo": "OWL props, records and env are objects. The shared-reference rule explains many 'why did my other component change?' bugs.",
 "predict": {"code": "const a = { q: 1 };\nconst b = a;\nb.q = 5;\nconsole.log(a.q);", "q": "What does this print?", "opts": ["1", "5", "undefined", "Error"], "ans": 1, "why": "a and b point to the same object, so changing b.q changes a.q."},
 "bug": {"task": "`value` should be 1200, but it's undefined. Fix the lookup.", "code": "const order = { brand: \"H&M\", qty: 1200 };\nconst field = \"qty\";\nconst value = order.field;\nconsole.log(value);", "test": "check(value === 1200, \"value should be 1200\");", "hint": "The key name is inside a variable.", "solution": "const order = { brand: \"H&M\", qty: 1200 };\nconst field = \"qty\";\nconst value = order[field];\nconsole.log(value);"},
 "write": {"task": "Add a property `status: \"shipped\"` to `order`. Then build `summary` = \"Kontoor: 1200 pcs (shipped)\" with a template literal using the object's properties, and log it.", "starter": "const order = { brand: \"Kontoor\", qty: 1200 };\n", "test": "check(order.status === \"shipped\", \"order.status should be shipped\");\ncheck(summary === \"Kontoor: 1200 pcs (shipped)\", \"Check the summary text\");\ncheck(__code.includes(\"${\"), \"Use a template literal\");", "solution": "const order = { brand: \"Kontoor\", qty: 1200 };\norder.status = \"shipped\";\nconst summary = `${order.brand}: ${order.qty} pcs (${order.status})`;\nconsole.log(summary);"},
 "quiz": [
  {"q": "With const key = \"qty\", which reads order.qty?", "opts": ["order.key", "order[key]", "order->key", "order(key)"], "ans": 1, "why": "Brackets evaluate the variable."},
  {"q": "How do you shallow-copy an object?", "opts": ["const b = a", "const b = { ...a }", "const b = copy a", "const b = a.clone"], "ans": 1, "why": "Spread copies the top-level properties into a new object."},
  {"q": "Object.keys({x: 1, y: 2}) returns…", "opts": ["[1, 2]", "[\"x\", \"y\"]", "2", "{x, y}"], "ans": 1, "why": "keys returns the property names."}
 ]
},
]
