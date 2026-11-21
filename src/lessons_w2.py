# Week 3-4 lessons: Python 8-14, JavaScript 8-14.
# Python tests can use: _output (all printed text), _code (the learner's code).
# JS tests can use: __logs (array of strings, one per console.log), __code, check(cond, message).

LESSONS = [
# ---------------------------------------------------------------- PYTHON 8
{
 "id": "py08",
 "goal": "Make decisions with `if`, `elif` and `else`, and get the indentation right.",
 "cards": [
  {"h": "if runs a block when the condition is True", "p": "End the `if` line with a colon. The lines inside are indented by 4 spaces. Python uses indentation, not braces, to know what is inside.", "code": "qty = 12000\nif qty > 10000:\n    print(\"Large order\")\n    print(\"Check capacity\")\nprint(\"Done\")   # always runs"},
  {"h": "else and elif", "p": "`else` runs when the condition is False. `elif` (else if) tests another condition. Python checks from the top and runs only the first branch that is True.", "code": "qty = 2500\nif qty >= 10000:\n    size = \"large\"\nelif qty >= 1000:\n    size = \"medium\"\nelse:\n    size = \"small\"\nprint(size)   # medium"},
  {"h": "Order matters", "p": "Put the most specific test first. If the first test is too wide, the later branches never run.", "code": "qty = 20000\nif qty >= 1000:\n    print(\"medium\")   # runs, and stops here\nelif qty >= 10000:\n    print(\"large\")    # never reached"},
  {"h": "Conditional expression", "p": "For a simple choice between two values, write it on one line: `a if condition else b`.", "code": "late_days = 3\nstatus = \"Late\" if late_days > 0 else \"On time\"\nprint(status)   # Late"}
 ],
 "odoo": "Odoo methods are full of these checks, for example `if order.state == 'draft':` before confirming. A compute method often uses if/elif to choose a value for each record.",
 "predict": {"code": "qty = 1000\nif qty > 1000:\n    print(\"A\")\nelif qty == 1000:\n    print(\"B\")\nelse:\n    print(\"C\")\nprint(\"D\")", "q": "What does this print?", "opts": ["A\nD", "B\nD", "B", "C\nD"], "ans": 1, "why": "1000 is not greater than 1000, so the first test fails. The elif is True, so B prints. D is not indented, so it always prints."},
 "bug": {"task": "For qty = 15000 this should print `large`, but it prints `medium`. Fix the order of the tests.", "code": "qty = 15000\nif qty >= 1000:\n    size = \"medium\"\nelif qty >= 10000:\n    size = \"large\"\nelse:\n    size = \"small\"\nprint(size)", "test": "assert size == \"large\", \"For 15000, size should be large\"\nassert _output.strip() == \"large\"", "hint": "Python stops at the first True test. Which test should come first?", "solution": "qty = 15000\nif qty >= 10000:\n    size = \"large\"\nelif qty >= 1000:\n    size = \"medium\"\nelse:\n    size = \"small\"\nprint(size)"},
 "write": {"task": "A shipment's `days_late` decides its status:\n- 0 or less: `On time`\n- 1 to 3: `Slightly late`\n- more than 3: `Very late`\nSet `status` with if/elif/else and print it. (For 5 it should be `Very late`.)", "starter": "days_late = 5\n", "test": "assert status == \"Very late\", \"For 5 days, status should be Very late\"\nassert \"elif\" in _code, \"Use if / elif / else\"\nfor d, want in [(0, \"On time\"), (-2, \"On time\"), (1, \"Slightly late\"), (3, \"Slightly late\"), (4, \"Very late\")]:\n    ns = {}\n    exec(_code.replace(\"days_late = 5\", f\"days_late = {d}\"), {\"print\": lambda *a, **k: None}, ns)\n    assert ns.get(\"status\") == want, f\"For days_late = {d}, status should be {want}\"", "solution": "days_late = 5\nif days_late <= 0:\n    status = \"On time\"\nelif days_late <= 3:\n    status = \"Slightly late\"\nelse:\n    status = \"Very late\"\nprint(status)"},
 "quiz": [
  {"q": "What ends an if line in Python?", "opts": ["A semicolon ;", "A colon :", "A brace {", "Nothing"], "ans": 1, "why": "if, elif and else lines end with a colon, and the block below is indented."},
  {"q": "How many branches of an if/elif/else chain can run?", "opts": ["All the True ones", "Exactly one at most", "Two", "None"], "ans": 1, "why": "Python runs the first True branch and skips the rest. If none is True and there's no else, none runs."},
  {"q": "x = \"yes\" if 0 else \"no\". What is x?", "opts": ["yes", "no", "0", "Error"], "ans": 1, "why": "0 is falsy, so the else value \"no\" is used."}
 ]
},
# ---------------------------------------------------------------- PYTHON 9
{
 "id": "py09",
 "goal": "Repeat work with `while` loops and make sure they stop.",
 "cards": [
  {"h": "while repeats while a condition is True", "p": "Python checks the condition before each round. When it becomes False, the loop ends and the code after it runs.", "code": "stock = 1000\nwhile stock > 0:\n    stock -= 300\n    print(\"Stock now\", stock)\nprint(\"Out of stock\")"},
  {"h": "Something must change", "p": "If nothing inside the loop changes the condition, it runs forever. That's an infinite loop. In this app, it stops after 10 seconds.", "code": "count = 0\nwhile count < 3:\n    print(\"Box\", count + 1)\n    count += 1   # without this line, it never ends"},
  {"h": "Counting and adding up", "p": "A common pattern: a counter for how many rounds, and a total that grows each round.", "code": "day = 0\nproduced = 0\nwhile produced < 5000:\n    produced += 1200\n    day += 1\nprint(day, \"days\")   # 5 days"},
  {"h": "while True with a stop", "p": "Sometimes you don't know the number of rounds. Use `while True:` and `break` to leave when you're done. You'll practise break in lesson 11.", "code": "n = 1\nwhile True:\n    n *= 2\n    if n > 100:\n        break\nprint(n)   # 128"}
 ],
 "odoo": "Odoo's scheduled actions (cron jobs) sometimes process records in a while loop, batch by batch, until nothing is left.",
 "predict": {"code": "n = 10\nwhile n > 0:\n    n -= 4\nprint(n)", "q": "What does this print?", "opts": ["0", "2", "-2", "-4"], "ans": 2, "why": "n goes 10 → 6 → 2 → -2. At -2 the condition n > 0 is False, so the loop stops and prints -2."},
 "bug": {"task": "This should print 1, 2, 3, 4, 5 (one per line) but never stops. Fix it.", "code": "i = 1\nwhile i <= 5:\n    print(i)", "test": "assert _output.split() == [\"1\", \"2\", \"3\", \"4\", \"5\"], \"Print the numbers 1 to 5, one per line\"", "hint": "What should change each round so the loop can end?", "solution": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1"},
 "write": {"task": "A factory makes `per_day = 1800` zippers a day. An order needs `target = 10000`. Use a while loop to count how many days it takes. Store it in `days` and print it (it should be 6).", "starter": "per_day = 1800\ntarget = 10000\n", "test": "assert days == 6, \"days should be 6\"\nassert \"while\" in _code, \"Use a while loop\"", "solution": "per_day = 1800\ntarget = 10000\ndays = 0\nmade = 0\nwhile made < target:\n    made += per_day\n    days += 1\nprint(days)"},
 "quiz": [
  {"q": "When does Python check a while condition?", "opts": ["Only once", "Before each round", "After the loop", "Only at the end"], "ans": 1, "why": "The condition is checked before every round, including the first."},
  {"q": "What causes an infinite loop?", "opts": ["Using print()", "The condition never becomes False", "Using +=", "A colon"], "ans": 1, "why": "If the condition stays True forever, the loop never ends."},
  {"q": "How many times does `while False:` run its block?", "opts": ["0", "1", "Forever", "Error"], "ans": 0, "why": "The condition is False from the start, so the block never runs."}
 ]
},
# ---------------------------------------------------------------- PYTHON 10
{
 "id": "py10",
 "goal": "Loop over sequences with `for`, and count with `range()`.",
 "cards": [
  {"h": "for goes through each item", "p": "A `for` loop takes each item of a sequence in turn, such as each character of a string. You don't need a counter.", "code": "for ch in \"OA1\":\n    print(ch)\n# O\n# A\n# 1"},
  {"h": "range() makes numbers", "p": "`range(stop)` gives 0 up to stop - 1. `range(start, stop)` starts somewhere else. `range(start, stop, step)` jumps by step.", "code": "for i in range(3):\n    print(i)          # 0 1 2\nfor i in range(1, 4):\n    print(i)          # 1 2 3\nfor i in range(0, 10, 5):\n    print(i)          # 0 5"},
  {"h": "Accumulating a total", "p": "Start a total before the loop, then add to it inside the loop.", "code": "total = 0\nfor carton in range(1, 6):\n    total += carton * 100\nprint(total)   # 1500"},
  {"h": "for or while?", "p": "Use `for` when you know what to loop over (a string, a range, later a list). Use `while` when you loop until something happens.", "code": "# for: 'do this 12 times'\n# while: 'keep going until stock is 0'"}
 ],
 "odoo": "You will write `for record in self:` in almost every Odoo method, because `self` can hold many records. It's the same for loop you learn today.",
 "predict": {"code": "total = 0\nfor i in range(1, 5):\n    total += i\nprint(total)", "q": "What does this print?", "opts": ["15", "10", "4", "6"], "ans": 1, "why": "range(1, 5) gives 1, 2, 3, 4 (5 is not included). 1 + 2 + 3 + 4 = 10."},
 "bug": {"task": "This should print the box numbers 1 to 5, but it prints 0 to 4. Fix the range.", "code": "for box in range(5):\n    print(\"Box\", box)", "test": "assert _output.strip().split(\"\\n\") == [f\"Box {i}\" for i in range(1, 6)], \"Print Box 1 to Box 5\"", "hint": "range() can take a start value.", "solution": "for box in range(1, 6):\n    print(\"Box\", box)"},
 "write": {"task": "Count how many letters in `code = \"KONTOOR-ZIP-0042\"` are digits. Use a for loop and the string method `isdigit()`. Store the answer in `digits` (it should be 4) and print it.", "starter": "code = \"KONTOOR-ZIP-0042\"\n", "test": "assert digits == 4, \"digits should be 4\"\nassert \"for \" in _code and \"isdigit\" in _code, \"Use a for loop and isdigit()\"", "solution": "code = \"KONTOOR-ZIP-0042\"\ndigits = 0\nfor ch in code:\n    if ch.isdigit():\n        digits += 1\nprint(digits)"},
 "quiz": [
  {"q": "What numbers does range(2, 6) give?", "opts": ["2 3 4 5 6", "2 3 4 5", "3 4 5 6", "2 4 6"], "ans": 1, "why": "range stops before the stop value."},
  {"q": "What does range(0, 10, 3) give?", "opts": ["0 3 6 9", "0 3 6", "3 6 9", "0 10 3"], "ans": 0, "why": "Start at 0, jump by 3, stop before 10: 0, 3, 6, 9."},
  {"q": "for ch in \"GAP\": runs how many times?", "opts": ["1", "2", "3", "4"], "ans": 2, "why": "Once for each character: G, A, P."}
 ]
},
# ---------------------------------------------------------------- PYTHON 11
{
 "id": "py11",
 "goal": "Control loops with `break`, `continue` and the loop `else`.",
 "cards": [
  {"h": "break leaves the loop", "p": "`break` stops the loop at once. Python continues with the code after the loop.", "code": "for qty in [500, 1200, 30000, 800]:\n    if qty > 10000:\n        print(\"Big order found:\", qty)\n        break\n    print(\"Checked\", qty)"},
  {"h": "continue skips one round", "p": "`continue` jumps to the next round, skipping the rest of this one.", "code": "for qty in [500, 0, 1200]:\n    if qty == 0:\n        continue        # skip empty lines\n    print(\"Pack\", qty)\n# Pack 500\n# Pack 1200"},
  {"h": "The loop else", "p": "A `for` or `while` can have an `else`. It runs only if the loop finished without `break`. It's perfect for 'search, and say if nothing was found'.", "code": "for po in [\"PO-1\", \"PO-2\"]:\n    if po == \"PO-9\":\n        print(\"Found\")\n        break\nelse:\n    print(\"Not found\")   # runs: no break happened"},
  {"h": "Keep it readable", "p": "break and continue are useful, but too many make a loop hard to follow. Use them for clear cases: stop when found, skip bad data."}
 ],
 "odoo": "When importing order lines, `continue` is a clean way to skip empty or invalid rows, and `break` stops a search once you've found the matching record.",
 "predict": {"code": "for i in range(5):\n    if i == 1:\n        continue\n    if i == 3:\n        break\n    print(i)\nelse:\n    print(\"end\")", "q": "What does this print?", "opts": ["0\n2", "0\n2\nend", "0\n1\n2", "0\n2\n4\nend"], "ans": 0, "why": "1 is skipped, 0 and 2 print, then break at 3. Because the loop ended with break, the else does not run."},
 "bug": {"task": "This should print `Not found` when PO-7 isn't in the list. Right now it prints `Not found` once for every PO. Fix it so it prints once, only if nothing matched.", "code": "pos = [\"PO-1\", \"PO-2\", \"PO-3\"]\nfor po in pos:\n    if po == \"PO-7\":\n        print(\"Found\")\n        break\n    else:\n        print(\"Not found\")", "test": "assert _output == \"Not found\\n\", \"Print Not found exactly once\"", "hint": "The else should belong to the for loop, not to the if. Check its indentation.", "solution": "pos = [\"PO-1\", \"PO-2\", \"PO-3\"]\nfor po in pos:\n    if po == \"PO-7\":\n        print(\"Found\")\n        break\nelse:\n    print(\"Not found\")"},
 "write": {"task": "Go through the characters of `line = \"GAP,1200,,500,X,300\"` split by commas. Skip empty parts with `continue`. Stop with `break` when you meet `X`. Add the other numbers into `total` (it should be 1700) and print it.", "starter": "line = \"GAP,1200,,500,X,300\"\nparts = line.split(\",\")\ntotal = 0\n", "test": "assert total == 1700, \"total should be 1700 (1200 + 500)\"\nassert \"continue\" in _code and \"break\" in _code, \"Use continue and break\"", "solution": "line = \"GAP,1200,,500,X,300\"\nparts = line.split(\",\")\ntotal = 0\nfor p in parts:\n    if p == \"\":\n        continue\n    if p == \"X\":\n        break\n    if p.isdigit():\n        total += int(p)\nprint(total)"},
 "quiz": [
  {"q": "What does continue do?", "opts": ["Ends the loop", "Skips to the next round", "Restarts from the first item", "Runs the else"], "ans": 1, "why": "continue skips the rest of this round only."},
  {"q": "When does a loop's else run?", "opts": ["Always", "Only after a break", "Only if the loop ended without break", "Never in a for loop"], "ans": 2, "why": "The else runs when the loop finishes normally."},
  {"q": "In nested loops, break leaves…", "opts": ["All loops", "Only the innermost loop", "The function", "The program"], "ans": 1, "why": "break only exits the loop it is directly inside."}
 ]
},
# ---------------------------------------------------------------- PYTHON 12
{
 "id": "py12",
 "goal": "Practise everything so far by building small number games and checks.",
 "cards": [
  {"h": "Plan before you code", "p": "Write the steps in plain English first: what goes in, what repeats, when it stops, what comes out. Then turn each step into a line of code.", "code": "# 1. read the guesses\n# 2. compare each with the secret\n# 3. say higher / lower / correct\n# 4. stop when correct"},
  {"h": "A guessing game", "p": "This uses input(), int(), a while loop, if/elif/else and break together. The Input box in this app gives one line to each input() call.", "code": "secret = 42\nwhile True:\n    guess = int(input(\"Guess: \"))\n    if guess < secret:\n        print(\"Higher\")\n    elif guess > secret:\n        print(\"Lower\")\n    else:\n        print(\"Correct!\")\n        break"},
  {"h": "Checking a number", "p": "% (remainder) answers many questions: is it even? Does it divide exactly? A loop can test many divisors.", "code": "n = 29\nis_prime = n > 1\nfor d in range(2, n):\n    if n % d == 0:\n        is_prime = False\n        break\nprint(is_prime)   # True"},
  {"h": "Test with several values", "p": "Try normal values, edge values (0, 1, the exact limit) and strange values. Most bugs hide at the edges."}
 ],
 "odoo": "Odoo developers check data in small loops like these all the time: validating quantities, checking sequence numbers, or finding gaps in OA numbers.",
 "predict": {"code": "count = 0\nfor n in range(1, 11):\n    if n % 3 == 0:\n        count += 1\nprint(count)", "q": "What does this print?", "opts": ["3", "4", "10", "33"], "ans": 0, "why": "Between 1 and 10, the multiples of 3 are 3, 6 and 9: three numbers."},
 "bug": {"task": "This game reads guesses until it's correct. With inputs 10, 50, 42 it should print Higher, Lower, Correct!, but it crashes. Fix it.", "stdin": "10\n50\n42", "code": "secret = 42\nwhile True:\n    guess = input()\n    if guess < secret:\n        print(\"Higher\")\n    elif guess > secret:\n        print(\"Lower\")\n    else:\n        print(\"Correct!\")\n        break", "test": "assert _output.split() == [\"Higher\", \"Lower\", \"Correct!\"], \"Expected Higher, Lower, Correct!\"", "hint": "input() gives a string. Can you compare a string with a number?", "solution": "secret = 42\nwhile True:\n    guess = int(input())\n    if guess < secret:\n        print(\"Higher\")\n    elif guess > secret:\n        print(\"Lower\")\n    else:\n        print(\"Correct!\")\n        break"},
 "write": {"task": "FizzBuzz for cartons: for numbers 1 to 15, print `Fizz` if divisible by 3, `Buzz` if divisible by 5, `FizzBuzz` if divisible by both, otherwise the number itself.", "starter": "", "test": "want = []\nfor n in range(1, 16):\n    want.append(\"FizzBuzz\" if n % 15 == 0 else \"Fizz\" if n % 3 == 0 else \"Buzz\" if n % 5 == 0 else str(n))\nassert _output.split() == want, \"Check each line from 1 to 15. 15 should be FizzBuzz\"", "solution": "for n in range(1, 16):\n    if n % 3 == 0 and n % 5 == 0:\n        print(\"FizzBuzz\")\n    elif n % 3 == 0:\n        print(\"Fizz\")\n    elif n % 5 == 0:\n        print(\"Buzz\")\n    else:\n        print(n)"},
 "quiz": [
  {"q": "In FizzBuzz, why must the 'both' test come first?", "opts": ["It's faster", "Otherwise 15 matches 'divisible by 3' first and prints Fizz", "Python requires it", "It doesn't matter"], "ans": 1, "why": "if/elif stops at the first True test, so the most specific test must come first."},
  {"q": "What is 17 % 4?", "opts": ["4", "1", "4.25", "0"], "ans": 1, "why": "17 = 4 × 4 + 1."},
  {"q": "Which values are the best tests for 'qty must be 1 to 100'?", "opts": ["50 only", "0, 1, 100, 101", "1000", "Any random value"], "ans": 1, "why": "Edge values just inside and just outside the limits find most bugs."}
 ]
},
# ---------------------------------------------------------------- PYTHON 13
{
 "id": "py13",
 "goal": "Store many values in a list, read them by position, and change them.",
 "cards": [
  {"h": "A list holds items in order", "p": "Write a list with square brackets and commas. It can hold any types, but usually holds one kind of thing. `len()` counts the items.", "code": "brands = [\"H&M\", \"GAP\", \"Kohl's\"]\nqtys = [1200, 500, 3400]\nprint(len(brands))   # 3"},
  {"h": "Indexes, like strings", "p": "The first item is at index 0, the last at -1. Reading an index that doesn't exist raises IndexError.", "code": "brands = [\"H&M\", \"GAP\", \"Kohl's\"]\nprint(brands[0])    # H&M\nprint(brands[-1])   # Kohl's\n# brands[3]  -> IndexError"},
  {"h": "Lists can change", "p": "Unlike strings, lists are mutable: you can replace an item by assigning to its index.", "code": "qtys = [1200, 500, 3400]\nqtys[1] = 650\nprint(qtys)   # [1200, 650, 3400]"},
  {"h": "Loop and check membership", "p": "`for item in list` visits each item. `in` checks if a value is in the list. `sum()`, `min()` and `max()` work on lists of numbers.", "code": "qtys = [1200, 650, 3400]\nfor q in qtys:\n    print(q)\nprint(650 in qtys)           # True\nprint(sum(qtys), max(qtys))  # 5250 3400"}
 ],
 "odoo": "Odoo recordsets feel like lists: you can loop over them, use len(), and index them. Values you send to Odoo, such as a list of ids [3, 7, 9], are plain Python lists.",
 "predict": {"code": "items = [10, 20, 30]\nitems[0] = items[-1] + 5\nprint(items)", "q": "What does this print?", "opts": ["[10, 20, 30]", "[35, 20, 30]", "[15, 20, 30]", "[10, 20, 35]"], "ans": 1, "why": "items[-1] is 30, plus 5 is 35, which replaces the first item."},
 "bug": {"task": "This should print the last shipment number, `SH-003`, but it crashes. Fix the index.", "code": "shipments = [\"SH-001\", \"SH-002\", \"SH-003\"]\nlast = shipments[3]\nprint(last)", "test": "assert last == \"SH-003\", \"last should be SH-003\"", "hint": "Three items have the indexes 0, 1 and 2. There's also a shortcut for 'the last one'.", "solution": "shipments = [\"SH-001\", \"SH-002\", \"SH-003\"]\nlast = shipments[-1]\nprint(last)"},
 "write": {"task": "`qtys` holds order quantities. Using a for loop (not sum()), add up only the quantities of 1000 or more into `big_total`, and count them in `big_count`. Print both. (Expected: 9600 and 3.)", "starter": "qtys = [1200, 500, 3400, 800, 5000]\n", "test": "assert big_total == 9600, \"big_total should be 9600\"\nassert big_count == 3, \"big_count should be 3\"\nassert \"for \" in _code and \"sum(\" not in _code, \"Use a for loop instead of sum()\"", "solution": "qtys = [1200, 500, 3400, 800, 5000]\nbig_total = 0\nbig_count = 0\nfor q in qtys:\n    if q >= 1000:\n        big_total += q\n        big_count += 1\nprint(big_total, big_count)"},
 "quiz": [
  {"q": "What is [5, 6, 7][-2]?", "opts": ["5", "6", "7", "Error"], "ans": 1, "why": "-1 is the last (7), -2 is the one before (6)."},
  {"q": "Which is true about lists?", "opts": ["They can't change", "They can be changed in place", "They only hold numbers", "They start at index 1"], "ans": 1, "why": "Lists are mutable, and indexes start at 0."},
  {"q": "What does 3 in [1, 2, 3] give?", "opts": ["3", "True", "2", "Error"], "ans": 1, "why": "in checks membership and returns True or False."}
 ]
},
# ---------------------------------------------------------------- PYTHON 14
{
 "id": "py14",
 "goal": "Grow, shrink, sort and slice lists with their methods.",
 "cards": [
  {"h": "Adding items", "p": "`append(x)` adds one item at the end. `extend(list)` adds many. `insert(i, x)` puts an item at a position.", "code": "pos = [\"PO-1\"]\npos.append(\"PO-2\")\npos.extend([\"PO-3\", \"PO-4\"])\npos.insert(0, \"PO-0\")\nprint(pos)   # ['PO-0', 'PO-1', 'PO-2', 'PO-3', 'PO-4']"},
  {"h": "Removing items", "p": "`remove(x)` deletes the first matching value. `pop()` removes and returns the last item; `pop(i)` removes position i.", "code": "pos = [\"PO-1\", \"PO-2\", \"PO-3\"]\npos.remove(\"PO-2\")\nlast = pos.pop()\nprint(pos, last)   # ['PO-1'] PO-3"},
  {"h": "sort() vs sorted()", "p": "`list.sort()` changes the list itself and returns None. `sorted(list)` returns a new sorted list and leaves the original alone. Add `reverse=True` for big to small.", "code": "qtys = [300, 5, 1200]\nprint(sorted(qtys))   # [5, 300, 1200]\nprint(qtys)           # [300, 5, 1200]\nqtys.sort(reverse=True)\nprint(qtys)           # [1200, 300, 5]"},
  {"h": "Slicing and copying", "p": "Slices work like strings: `lst[start:stop]`, and `lst[::-1]` reverses. `lst[:]` or `lst.copy()` makes a copy. Plain `b = a` does not copy: both names share one list.", "code": "a = [1, 2, 3, 4]\nprint(a[1:3])    # [2, 3]\nprint(a[::-1])   # [4, 3, 2, 1]\nb = a\nb.append(5)\nprint(a)         # [1, 2, 3, 4, 5]"}
 ],
 "odoo": "Recordsets have their own versions of these ideas: sorted(key=...), filtered(), and slicing like orders[:5] for the first five records.",
 "predict": {"code": "a = [3, 1, 2]\nb = a.sort()\nprint(a, b)", "q": "What does this print?", "opts": ["[1, 2, 3] [1, 2, 3]", "[3, 1, 2] [1, 2, 3]", "[1, 2, 3] None", "None None"], "ans": 2, "why": "sort() sorts the list in place and returns None, so b is None."},
 "bug": {"task": "`top3` should be the three biggest quantities, biggest first: [5000, 3400, 1200]. Fix it.", "code": "qtys = [1200, 500, 3400, 800, 5000]\ntop3 = qtys.sort(reverse=True)[:3]\nprint(top3)", "test": "assert top3 == [5000, 3400, 1200], \"top3 should be [5000, 3400, 1200]\"", "hint": "sort() returns None. Which function returns a new sorted list?", "solution": "qtys = [1200, 500, 3400, 800, 5000]\ntop3 = sorted(qtys, reverse=True)[:3]\nprint(top3)"},
 "write": {"task": "Start with `queue = [\"OA-101\", \"OA-102\"]`.\n1. Add \"OA-103\" at the end.\n2. Add \"OA-100\" at the start.\n3. Remove \"OA-102\".\n4. Make `backup`, a real copy of queue.\n5. Pop the last item from queue into `done`.\nPrint queue, backup and done.", "starter": "queue = [\"OA-101\", \"OA-102\"]\n", "test": "assert queue == [\"OA-100\", \"OA-101\"], \"queue should end as ['OA-100', 'OA-101']\"\nassert backup == [\"OA-100\", \"OA-101\", \"OA-103\"], \"backup should be a copy made before the pop\"\nassert backup is not queue, \"backup must be a copy, not the same list\"\nassert done == \"OA-103\", \"done should be OA-103\"", "solution": "queue = [\"OA-101\", \"OA-102\"]\nqueue.append(\"OA-103\")\nqueue.insert(0, \"OA-100\")\nqueue.remove(\"OA-102\")\nbackup = queue.copy()\ndone = queue.pop()\nprint(queue, backup, done)"},
 "quiz": [
  {"q": "What does append([7, 8]) do to [1]?", "opts": ["[1, 7, 8]", "[1, [7, 8]]", "[7, 8]", "Error"], "ans": 1, "why": "append adds one item, and here that item is a list. Use extend to add 7 and 8 separately."},
  {"q": "What does pop() return?", "opts": ["Nothing", "The removed last item", "The new list", "Its index"], "ans": 1, "why": "pop removes the last item and gives it back."},
  {"q": "After b = a, a list change through b…", "opts": ["only changes b", "also shows in a", "raises an error", "copies the list"], "ans": 1, "why": "b = a doesn't copy; both names point to the same list."}
 ]
},
# ---------------------------------------------------------------- JS 8
{
 "id": "js08",
 "goal": "Write reusable functions, including short arrow functions.",
 "cards": [
  {"h": "Function declarations", "p": "A function has a name, parameters in brackets, and a body in braces. `return` sends a value back. Without return, the result is `undefined`.", "code": "function lineTotal(qty, price) {\n  return qty * price;\n}\nconsole.log(lineTotal(1200, 0.35));   // 420"},
  {"h": "Arrow functions", "p": "A shorter way to write a function, often stored in a const. With one expression and no braces, the value is returned automatically.", "code": "const lineTotal = (qty, price) => qty * price;\nconst double = n => n * 2;\nconsole.log(lineTotal(10, 3), double(4));   // 30 8"},
  {"h": "Default parameters", "p": "Give a parameter a default value. It's used when the argument is missing (undefined).", "code": "const label = (po, brand = \"H&M\") => `${brand} ${po}`;\nconsole.log(label(\"PO-1\"));         // H&M PO-1\nconsole.log(label(\"PO-2\", \"GAP\"));  // GAP PO-2"},
  {"h": "Functions are values", "p": "You can pass a function to another function. That's exactly what map and filter do with the arrow functions you give them.", "code": "const isBig = q => q >= 1000;\nconsole.log([500, 1200, 3000].filter(isBig));   // [1200,3000]"}
 ],
 "odoo": "Arrow functions are everywhere in OWL code: event handlers like `() => this.save()`, and callbacks given to map, filter and the orm service.",
 "predict": {"code": "const f = (a, b = 10) => a + b;\nfunction g(x) { x * 2; }\nconsole.log(f(5), g(5));", "q": "What does this print?", "opts": ["15 10", "15 undefined", "NaN undefined", "15 null"], "ans": 1, "why": "f(5) uses the default b = 10. g has a body in braces but no return, so it returns undefined."},
 "bug": {"task": "`total` should be 420, but it's undefined. Fix the function.", "code": "function lineTotal(qty, price) {\n  qty * price;\n}\nconst total = lineTotal(1200, 0.35);\nconsole.log(total);", "test": "check(total === 420, \"total should be 420\");", "hint": "A function in braces only gives back what you return.", "solution": "function lineTotal(qty, price) {\n  return qty * price;\n}\nconst total = lineTotal(1200, 0.35);\nconsole.log(total);"},
 "write": {"task": "Write an arrow function `discountPrice(price, pct = 10)` that returns the price after a pct% discount. Log discountPrice(200) (should be 180) and discountPrice(200, 25) (should be 150).", "starter": "", "test": "check(typeof discountPrice === \"function\", \"Define discountPrice\");\ncheck(discountPrice(200) === 180, \"discountPrice(200) should be 180\");\ncheck(discountPrice(200, 25) === 150, \"discountPrice(200, 25) should be 150\");\ncheck(__code.includes(\"=>\"), \"Use an arrow function\");", "solution": "const discountPrice = (price, pct = 10) => price - price * pct / 100;\nconsole.log(discountPrice(200));\nconsole.log(discountPrice(200, 25));"},
 "quiz": [
  {"q": "What does a function return if it has no return statement?", "opts": ["null", "0", "undefined", "An error"], "ans": 2, "why": "Without return, a JavaScript function returns undefined."},
  {"q": "Which arrow function returns the square of n?", "opts": ["n => { n * n }", "n => n * n", "n -> n * n", "(n) { n * n }"], "ans": 1, "why": "Without braces, the expression is returned. With braces, you need return."},
  {"q": "When is a default parameter used?", "opts": ["When the argument is 0", "When the argument is undefined or missing", "When it is null", "Always"], "ans": 1, "why": "Defaults replace undefined only. null and 0 are kept."}
 ]
},
# ---------------------------------------------------------------- JS 9
{
 "id": "js09",
 "goal": "Unpack arrays and objects with destructuring, and copy or merge them with spread.",
 "cards": [
  {"h": "Object destructuring", "p": "Pull properties into variables in one line. You can rename with `:` and give defaults with `=`.", "code": "const order = { brand: \"GAP\", qty: 500 };\nconst { brand, qty, status = \"draft\" } = order;\nconsole.log(brand, qty, status);   // GAP 500 draft\nconst { brand: customer } = order;\nconsole.log(customer);             // GAP"},
  {"h": "Array destructuring", "p": "Variables take items by position. Skip one with an empty comma. Swap two values easily.", "code": "const [first, , third] = [\"PO\", \"HM\", \"88412\"];\nconsole.log(first, third);   // PO 88412\nlet a = 1, b = 2;\n[a, b] = [b, a];\nconsole.log(a, b);           // 2 1"},
  {"h": "Spread copies and merges", "p": "`...` spreads the items of an array or the properties of an object into a new one. Later properties win.", "code": "const base = { brand: \"H&M\", qty: 100 };\nconst updated = { ...base, qty: 250 };\nconsole.log(updated);              // {\"brand\":\"H&M\",\"qty\":250}\nconsole.log([...[1, 2], 3]);       // [1,2,3]"},
  {"h": "Rest collects the remaining", "p": "The same `...` on the left side collects what's left into an array or object.", "code": "const [head, ...others] = [10, 20, 30];\nconsole.log(head, others);   // 10 [20,30]\nconst { id, ...data } = { id: 7, name: \"Zip\", qty: 3 };\nconsole.log(data);           // {\"name\":\"Zip\",\"qty\":3}"}
 ],
 "odoo": "OWL and Odoo JS code destructure constantly, for example `const { resId, resModel } = this.props.record` or spreading a context: `{ ...context, default_partner_id: id }`.",
 "predict": {"code": "const a = { x: 1, y: 2 };\nconst b = { ...a, y: 9, z: 3 };\nconst { x, ...rest } = b;\nconsole.log(x, rest);", "q": "What does this print?", "opts": ["1 {\"y\":2,\"z\":3}", "1 {\"y\":9,\"z\":3}", "1 {\"x\":1,\"y\":9,\"z\":3}", "undefined {\"y\":9}"], "ans": 1, "why": "In b, y: 9 replaces the spread y: 2. Then x is taken out and rest gets the other properties."},
 "bug": {"task": "`copy` should be a separate object. Changing copy.qty must not change order.qty. Fix it.", "code": "const order = { brand: \"Kontoor\", qty: 1200 };\nconst copy = order;\ncopy.qty = 0;\nconsole.log(order.qty, copy.qty);", "test": "check(order.qty === 1200, \"order.qty must stay 1200\");\ncheck(copy.qty === 0 && copy.brand === \"Kontoor\", \"copy should have brand Kontoor and qty 0\");", "hint": "Assignment shares the object. Spread makes a new one.", "solution": "const order = { brand: \"Kontoor\", qty: 1200 };\nconst copy = { ...order };\ncopy.qty = 0;\nconsole.log(order.qty, copy.qty);"},
 "write": {"task": "From `line`, use destructuring to get `brand` and `qty`, and collect the remaining properties into `extra`. Then create `confirmed`: a new object with all of line's properties plus `state: \"confirmed\"`. Log brand, qty, extra and confirmed.", "starter": "const line = { brand: \"Carter's\", qty: 3000, size: \"5 inch\", color: \"black\" };\n", "test": "check(brand === \"Carter's\" && qty === 3000, \"brand and qty from destructuring\");\ncheck(JSON.stringify(extra) === JSON.stringify({ size: \"5 inch\", color: \"black\" }), \"extra should hold size and color\");\ncheck(confirmed.state === \"confirmed\" && confirmed.qty === 3000 && confirmed !== line, \"confirmed should be a new object with state confirmed\");\ncheck(line.state === undefined, \"Don't change line itself\");\ncheck(__code.includes(\"...\"), \"Use rest/spread\");", "solution": "const line = { brand: \"Carter's\", qty: 3000, size: \"5 inch\", color: \"black\" };\nconst { brand, qty, ...extra } = line;\nconst confirmed = { ...line, state: \"confirmed\" };\nconsole.log(brand, qty, extra, confirmed);"},
 "quiz": [
  {"q": "const { qty = 5 } = { qty: 0 }; What is qty?", "opts": ["5", "0", "undefined", "null"], "ans": 1, "why": "Defaults only apply to undefined. 0 is a real value."},
  {"q": "In { ...a, ...b }, if both have key k, which value wins?", "opts": ["a's", "b's", "Neither", "It throws"], "ans": 1, "why": "Later properties overwrite earlier ones."},
  {"q": "Is { ...obj } a deep copy?", "opts": ["Yes", "No, it's shallow: nested objects are still shared", "Only for arrays", "Only in OWL"], "ans": 1, "why": "Spread copies the top level only."}
 ]
},
# ---------------------------------------------------------------- JS 10
{
 "id": "js10",
 "goal": "Understand block scope, closures, and how `this` works in methods and arrow functions.",
 "cards": [
  {"h": "Block scope", "p": "`let` and `const` live only inside the braces `{ }` where you declare them. Outside, they don't exist.", "code": "if (true) {\n  const msg = \"inside\";\n  console.log(msg);\n}\n// console.log(msg);  -> ReferenceError"},
  {"h": "Closures", "p": "A function remembers the variables around it when it was created, even after the outer function has finished. That memory is a closure.", "code": "function makeCounter() {\n  let count = 0;\n  return () => {\n    count++;\n    return count;\n  };\n}\nconst next = makeCounter();\nnext();\nconsole.log(next());   // 2"},
  {"h": "this in a method", "p": "Inside a normal method, `this` is the object before the dot when you call it.", "code": "const order = {\n  qty: 1200,\n  show() { return `Qty ${this.qty}`; },\n};\nconsole.log(order.show());   // Qty 1200"},
  {"h": "Arrow functions keep the outer this", "p": "An arrow function has no `this` of its own; it uses `this` from where it was written. That's why arrow callbacks inside methods work well. A method taken off its object loses its `this`.", "code": "const order = {\n  qtys: [1, 2],\n  scaled() { return this.qtys.map(q => q * this.factor); },\n  factor: 10,\n};\nconsole.log(order.scaled());   // [10,20]\nconst f = order.show;           // detached: this is lost"}
 ],
 "odoo": "OWL templates call your methods with the right `this`, and in JavaScript code you'll write `() => this.doSomething()` so `this` stays your component. Forgetting this causes 'cannot read properties of undefined'.",
 "predict": {"code": "function make() {\n  let n = 0;\n  return () => ++n;\n}\nconst a = make();\nconst b = make();\na(); a();\nconsole.log(a(), b());", "q": "What does this print?", "opts": ["3 1", "1 1", "3 3", "2 1"], "ans": 0, "why": "Each call to make() creates its own n. a has been called three times (3); b only once (1)."},
 "bug": {"task": "`order.total()` should return [600, 1050] (each qty times this.price), but it crashes. Fix the callback.", "code": "const order = {\n  price: 0.5,\n  qtys: [1200, 2100],\n  total() {\n    return this.qtys.map(function (q) { return q * this.price; });\n  },\n};\nconst result = order.total();\nconsole.log(result);", "test": "check(JSON.stringify(result) === \"[600,1050]\", \"result should be [600,1050]\");", "hint": "A normal function callback gets its own `this`. Which kind of function keeps the outer this?", "solution": "const order = {\n  price: 0.5,\n  qtys: [1200, 2100],\n  total() {\n    return this.qtys.map(q => q * this.price);\n  },\n};\nconst result = order.total();\nconsole.log(result);"},
 "write": {"task": "Write `makeSequence(prefix)` that returns a function. Each call of that function returns the next code: `OA-1`, `OA-2`, … Use a closure. Create `nextOA = makeSequence(\"OA\")` and log three calls.", "starter": "", "test": "const s = makeSequence(\"PI\");\ncheck(s() === \"PI-1\" && s() === \"PI-2\", \"Each call should give the next number: PI-1, PI-2\");\nconst t2 = makeSequence(\"X\");\ncheck(t2() === \"X-1\", \"Each sequence should count on its own\");\ncheck(typeof nextOA === \"function\", \"Create nextOA\");", "solution": "function makeSequence(prefix) {\n  let n = 0;\n  return () => {\n    n++;\n    return `${prefix}-${n}`;\n  };\n}\nconst nextOA = makeSequence(\"OA\");\nconsole.log(nextOA());\nconsole.log(nextOA());\nconsole.log(nextOA());"},
 "quiz": [
  {"q": "Where can a const declared inside an if block be used?", "opts": ["Anywhere in the file", "Only inside that block", "Only in functions", "After the block"], "ans": 1, "why": "let and const are block-scoped."},
  {"q": "What is a closure?", "opts": ["A function that closes the program", "A function that remembers variables from where it was created", "A class", "A loop"], "ans": 1, "why": "The function keeps access to the outer variables."},
  {"q": "Why use arrow callbacks inside methods?", "opts": ["They're faster", "They keep the method's this", "They can't return values", "They create new scope for this"], "ans": 1, "why": "Arrow functions use this from the surrounding method."}
 ]
},
# ---------------------------------------------------------------- JS 11
{
 "id": "js11",
 "goal": "Model things with classes: constructors, methods, getters, fields and inheritance.",
 "cards": [
  {"h": "class and constructor", "p": "A class is a blueprint. `new` creates an object from it and runs `constructor`, where you set up `this`.", "code": "class Order {\n  constructor(brand, qty) {\n    this.brand = brand;\n    this.qty = qty;\n  }\n  label() {\n    return `${this.brand}: ${this.qty}`;\n  }\n}\nconst o = new Order(\"GAP\", 500);\nconsole.log(o.label());   // GAP: 500"},
  {"h": "Class fields and getters", "p": "Fields set default values without a constructor. A `get` method looks like a property when you read it.", "code": "class Line {\n  qty = 0;\n  price = 0.35;\n  get total() { return this.qty * this.price; }\n}\nconst l = new Line();\nl.qty = 1000;\nconsole.log(l.total);   // 350"},
  {"h": "extends and super", "p": "A subclass gets everything from its parent class. `super(...)` calls the parent constructor; `super.method()` calls the parent's method.", "code": "class UrgentOrder extends Order {\n  label() {\n    return super.label() + \" (URGENT)\";\n  }\n}\nconsole.log(new UrgentOrder(\"H&M\", 9000).label());\n// H&M: 9000 (URGENT)"},
  {"h": "static members", "p": "`static` belongs to the class itself, not to each object. You'll see it in every OWL component: `static template = ...`.", "code": "class Order2 {\n  static currency = \"USD\";\n}\nconsole.log(Order2.currency);   // USD"}
 ],
 "odoo": "Every OWL component is a class that extends Component, with `static template` and `static components`. Odoo models in Python are classes too, so this idea works on both sides.",
 "predict": {"code": "class A {\n  name = \"A\";\n  hello() { return \"I am \" + this.name; }\n}\nclass B extends A {\n  name = \"B\";\n}\nconsole.log(new B().hello());", "q": "What does this print?", "opts": ["I am A", "I am B", "I am undefined", "Error"], "ans": 1, "why": "hello() is inherited from A, but this is the B object, whose name field is \"B\"."},
 "bug": {"task": "This crashes with a ReferenceError. `UrgentOrder` must call the parent constructor before using `this`. Fix it so `u.label()` returns `H&M: 9000 (2 days)`.", "code": "class Order {\n  constructor(brand, qty) {\n    this.brand = brand;\n    this.qty = qty;\n  }\n  label() { return `${this.brand}: ${this.qty}`; }\n}\nclass UrgentOrder extends Order {\n  constructor(brand, qty, days) {\n    this.days = days;\n  }\n  label() { return `${super.label()} (${this.days} days)`; }\n}\nconst u = new UrgentOrder(\"H&M\", 9000, 2);\nconsole.log(u.label());", "test": "check(u.label() === \"H&M: 9000 (2 days)\", \"u.label() should be H&M: 9000 (2 days)\");", "hint": "In a subclass constructor, call super(...) first.", "solution": "class Order {\n  constructor(brand, qty) {\n    this.brand = brand;\n    this.qty = qty;\n  }\n  label() { return `${this.brand}: ${this.qty}`; }\n}\nclass UrgentOrder extends Order {\n  constructor(brand, qty, days) {\n    super(brand, qty);\n    this.days = days;\n  }\n  label() { return `${super.label()} (${this.days} days)`; }\n}\nconst u = new UrgentOrder(\"H&M\", 9000, 2);\nconsole.log(u.label());"},
 "write": {"task": "Write a class `Shipment` with:\n- a constructor(ref, cartons)\n- a field `delivered = false`\n- a method `deliver()` that sets delivered to true\n- a getter `status` that returns \"delivered\" or \"in transit\"\nCreate `s = new Shipment(\"SH-77\", 40)`, log s.status, call deliver(), log s.status again.", "starter": "", "test": "const t1 = new Shipment(\"SH-1\", 5);\ncheck(t1.ref === \"SH-1\" && t1.cartons === 5, \"Store ref and cartons\");\ncheck(t1.status === \"in transit\", \"A new shipment's status should be 'in transit'\");\nt1.deliver();\ncheck(t1.delivered === true && t1.status === \"delivered\", \"After deliver(), status should be 'delivered'\");\ncheck(/get\\s+status/.test(__code), \"Make status a getter\");", "solution": "class Shipment {\n  delivered = false;\n  constructor(ref, cartons) {\n    this.ref = ref;\n    this.cartons = cartons;\n  }\n  deliver() {\n    this.delivered = true;\n  }\n  get status() {\n    return this.delivered ? \"delivered\" : \"in transit\";\n  }\n}\nconst s = new Shipment(\"SH-77\", 40);\nconsole.log(s.status);\ns.deliver();\nconsole.log(s.status);"},
 "quiz": [
  {"q": "What does new do?", "opts": ["Copies a class", "Creates an object and runs the constructor", "Declares a variable", "Imports a module"], "ans": 1, "why": "new builds a new object from the class."},
  {"q": "How do you read a getter called total?", "opts": ["obj.total()", "obj.total", "obj.get(total)", "obj[total()]"], "ans": 1, "why": "Getters are read like properties, without brackets."},
  {"q": "Where does a static field live?", "opts": ["On each object", "On the class itself", "In the constructor", "In the module"], "ans": 1, "why": "Static members belong to the class, like Component's static template."}
 ]
},
# ---------------------------------------------------------------- JS 12
{
 "id": "js12",
 "goal": "Split code into modules with `export` and `import`, the way every Odoo JS file works.",
 "cards": [
  {"h": "One file, one module", "p": "A module is a JavaScript file with its own scope. Nothing leaks out unless you `export` it.", "code": "// money.js\nexport const CURRENCY = \"USD\";\nexport function lineTotal(qty, price) {\n  return qty * price;\n}"},
  {"h": "Named imports", "p": "Import exactly the names you need, in braces. You can rename with `as`.", "code": "// order.js\nimport { lineTotal, CURRENCY } from \"./money.js\";\nimport { lineTotal as total } from \"./money.js\";\nconsole.log(lineTotal(10, 2), CURRENCY);"},
  {"h": "Default export", "p": "A module can have one default export, imported without braces and with any name. Odoo code mostly prefers named exports, which are easier to search.", "code": "// shipment.js\nexport default class Shipment {}\n\n// main.js\nimport Shipment from \"./shipment.js\";"},
  {"h": "Why modules help", "p": "Each file has a clear job, names don't clash, and you can see what a file depends on by reading its imports. Note: this app's runner executes one snippet, so today's exercises practise the idea with objects instead of real files."}
 ],
 "odoo": "Every Odoo 20 JS file is an ES module, for example `import { Component, signal } from \"@odoo/owl\";` and `import { registry } from \"@web/core/registry\";`. `@web` points to the web addon's static/src folder.",
 "predict": {"code": "const money = (() => {\n  const RATE = 2;          // private\n  const total = q => q * RATE;\n  return { total };        // the 'exports'\n})();\nconsole.log(money.total(5), money.RATE);", "q": "This imitates a module. What does it print?", "opts": ["10 2", "10 undefined", "Error", "5 2"], "ans": 1, "why": "Only total is returned (exported). RATE stays private, so money.RATE is undefined, just like a name a module didn't export."},
 "bug": {"task": "These lines imitate a module that should export `formatPO`. The code that uses it crashes. Fix the 'exports' so `label` is `PO-00042`.", "code": "const poModule = (() => {\n  const formatPO = n => \"PO-\" + String(n).padStart(5, \"0\");\n  return {};\n})();\nconst label = poModule.formatPO(42);\nconsole.log(label);", "test": "check(label === \"PO-00042\", \"label should be PO-00042\");", "hint": "What does the module return? Nothing is exported yet.", "solution": "const poModule = (() => {\n  const formatPO = n => \"PO-\" + String(n).padStart(5, \"0\");\n  return { formatPO };\n})();\nconst label = poModule.formatPO(42);\nconsole.log(label);"},
 "write": {"task": "Write the real module syntax as a string, to practise it. Set `importLine` to the exact line that imports `Component` and `signal` from \"@odoo/owl\" (with a semicolon at the end). Then set `exportLine` to a line that exports a const `MAX_QTY` equal to 50000. Log both.", "starter": "", "test": "const norm = s => s.replace(/\\s+/g, \" \").trim();\ncheck(/^import \\{ ?(Component, ?signal|signal, ?Component) ?\\} from [\"']@odoo\\/owl[\"'];$/.test(norm(importLine)), \"importLine should look like: import { Component, signal } from \\\"@odoo/owl\\\";\");\ncheck(/^export const MAX_QTY = 50000;?$/.test(norm(exportLine)), \"exportLine should be: export const MAX_QTY = 50000;\");", "solution": "const importLine = 'import { Component, signal } from \"@odoo/owl\";';\nconst exportLine = \"export const MAX_QTY = 50000;\";\nconsole.log(importLine);\nconsole.log(exportLine);"},
 "quiz": [
  {"q": "How do you import a named export total from ./money.js?", "opts": ["import total from \"./money.js\"", "import { total } from \"./money.js\"", "require(total)", "include ./money.js"], "ans": 1, "why": "Named exports are imported inside braces."},
  {"q": "How many default exports can a module have?", "opts": ["None", "One", "Two", "Any number"], "ans": 1, "why": "At most one default export, plus any number of named exports."},
  {"q": "In Odoo, what does \"@web/core/registry\" point to?", "opts": ["A website URL", "The web addon's static/src/core/registry.js", "An npm package on the internet", "The Python registry"], "ans": 1, "why": "@web is an alias for the web module's static/src folder."}
 ]
},
# ---------------------------------------------------------------- JS 13
{
 "id": "js13",
 "goal": "Understand promises: values that arrive later, with then, catch and Promise.all.",
 "cards": [
  {"h": "Why promises", "p": "Talking to a server takes time. JavaScript doesn't wait and freeze; it gives you a Promise, which will later be fulfilled with a value or rejected with an error.", "code": "const p = new Promise(resolve => {\n  setTimeout(() => resolve(\"OA-1001 confirmed\"), 100);\n});\np.then(msg => console.log(msg));\nconsole.log(\"waiting...\");   // prints first!"},
  {"h": "then chains", "p": "`then` runs when the value arrives. Whatever you return from then becomes the value for the next then.", "code": "Promise.resolve(1200)\n  .then(qty => qty * 0.35)\n  .then(total => console.log(total));   // 420"},
  {"h": "catch handles errors", "p": "If any step rejects or throws, the chain jumps to `catch`. `finally` runs either way.", "code": "Promise.reject(new Error(\"Server down\"))\n  .then(() => console.log(\"never\"))\n  .catch(err => console.log(\"Failed:\", err.message))\n  .finally(() => console.log(\"done\"));"},
  {"h": "Promise.all waits for many", "p": "Start several jobs at once, then wait for all of them. The result is an array in the same order. If one fails, the whole thing fails.", "code": "const wait = (v, ms) => new Promise(r => setTimeout(() => r(v), ms));\nPromise.all([wait(\"GAP\", 50), wait(\"H&M\", 10)])\n  .then(names => console.log(names));   // [\"GAP\",\"H&M\"]"}
 ],
 "odoo": "Every call to the server, like `this.orm.searchRead(...)`, returns a promise. In OWL code you usually await it (next lesson) instead of writing then chains.",
 "predict": {"code": "console.log(\"A\");\nsetTimeout(() => console.log(\"B\"), 0);\nPromise.resolve().then(() => console.log(\"C\"));\nconsole.log(\"D\");", "q": "In what order are the lines printed?", "opts": ["A\nB\nC\nD", "A\nD\nC\nB", "A\nD\nB\nC", "A\nC\nD\nB"], "ans": 1, "why": "Normal code runs first (A, D). Then promise callbacks (C) run before timer callbacks (B), even with a 0 ms timer."},
 "bug": {"task": "This should log the total, 420. Nothing useful arrives at the second then. Fix the chain.", "code": "let result;\nPromise.resolve(1200)\n  .then(qty => { qty * 0.35; })\n  .then(total => { result = total; console.log(total); });\nawait new Promise(r => setTimeout(r, 20));", "test": "check(result === 420, \"result should be 420\");", "hint": "A then callback with braces must return its value.", "solution": "let result;\nPromise.resolve(1200)\n  .then(qty => qty * 0.35)\n  .then(total => { result = total; console.log(total); });\nawait new Promise(r => setTimeout(r, 20));"},
 "write": {"task": "`fetchQty(brand)` imitates a server call. Use Promise.all to load the quantities for \"H&M\", \"GAP\" and \"Kohl's\" at the same time, then put the sum in `total` (it should be 5100) and log it. Use then (not await) for this exercise; the last line waits for you.", "starter": "const fetchQty = brand => new Promise(resolve => {\n  const data = { \"H&M\": 1200, \"GAP\": 500, \"Kohl's\": 3400 };\n  setTimeout(() => resolve(data[brand]), 10);\n});\nlet total;\n\n// your code here\n\nawait new Promise(r => setTimeout(r, 100));\n", "test": "check(total === 5100, \"total should be 5100\");\ncheck(__code.includes(\"Promise.all\"), \"Use Promise.all\");", "solution": "const fetchQty = brand => new Promise(resolve => {\n  const data = { \"H&M\": 1200, \"GAP\": 500, \"Kohl's\": 3400 };\n  setTimeout(() => resolve(data[brand]), 10);\n});\nlet total;\n\nPromise.all([fetchQty(\"H&M\"), fetchQty(\"GAP\"), fetchQty(\"Kohl's\")])\n  .then(qtys => {\n    total = qtys.reduce((a, b) => a + b, 0);\n    console.log(total);\n  });\n\nawait new Promise(r => setTimeout(r, 100));\n"},
 "quiz": [
  {"q": "What are the three states of a promise?", "opts": ["start, middle, end", "pending, fulfilled, rejected", "open, closed, error", "true, false, null"], "ans": 1, "why": "A promise starts pending, then is either fulfilled or rejected."},
  {"q": "Where does an error in a then chain go?", "opts": ["It's ignored", "To the next catch", "To finally only", "It stops the browser"], "ans": 1, "why": "Rejections skip the remaining thens until a catch."},
  {"q": "What does Promise.all give when all succeed?", "opts": ["The first value", "An array of values in order", "The fastest value", "Nothing"], "ans": 1, "why": "It resolves with all values, in the same order as the input."}
 ]
},
# ---------------------------------------------------------------- JS 14
{
 "id": "js14",
 "goal": "Write asynchronous code that reads like normal code with `async` and `await`.",
 "cards": [
  {"h": "async functions", "p": "An `async` function always returns a promise. Inside it, `await` pauses that function until a promise settles, without freezing the page.", "code": "const wait = ms => new Promise(r => setTimeout(r, ms));\nasync function confirmOrder() {\n  await wait(50);\n  return \"confirmed\";\n}\nconfirmOrder().then(s => console.log(s));"},
  {"h": "await gives you the value", "p": "Instead of `.then(value => ...)`, write `const value = await promise;`. The code reads top to bottom. (In this app's runner you can use await directly at the top level.)", "code": "const fetchQty = () => new Promise(r => setTimeout(() => r(1200), 20));\nconst qty = await fetchQty();\nconsole.log(qty * 0.35);   // 420"},
  {"h": "try / catch for errors", "p": "A rejected promise makes `await` throw. Catch it with try/catch, the same tool you use for normal errors.", "code": "async function load() {\n  throw new Error(\"Access denied\");\n}\ntry {\n  await load();\n} catch (err) {\n  console.log(\"Could not load:\", err.message);\n}"},
  {"h": "One after another, or together?", "p": "Two awaits in a row run one after the other. If the jobs don't depend on each other, start them together and use `await Promise.all([...])`, which is faster.", "code": "// slow: about 200 ms\n// const a = await job(100); const b = await job(100);\n// fast: about 100 ms\n// const [a, b] = await Promise.all([job(100), job(100)]);"}
 ],
 "odoo": "OWL code loads data like this: `onWillStart(async () => { this.orders = await this.orm.searchRead(\"sale.order\", [], [\"name\"]); })`. You'll write that in the OWL lessons.",
 "predict": {"code": "async function f() {\n  console.log(\"in f\");\n  return 5;\n}\nconst p = f();\nconsole.log(typeof p);\nconsole.log(await p);", "q": "What does this print?", "opts": ["in f\nnumber\n5", "in f\nobject\n5", "object\nin f\n5", "in f\nobject\nundefined"], "ans": 1, "why": "The code before the first await runs at once, so \"in f\" prints first. An async function returns a promise (typeof \"object\"), and awaiting it gives 5."},
 "bug": {"task": "`qty` should be the number 1200, but it's a Promise, so `total` is NaN. Fix it.", "code": "const fetchQty = () => new Promise(r => setTimeout(() => r(1200), 10));\nconst qty = fetchQty();\nconst total = qty * 0.35;\nconsole.log(total);", "test": "check(qty === 1200, \"qty should be 1200\");\ncheck(total === 420, \"total should be 420\");", "hint": "You need to wait for the value.", "solution": "const fetchQty = () => new Promise(r => setTimeout(() => r(1200), 10));\nconst qty = await fetchQty();\nconst total = qty * 0.35;\nconsole.log(total);"},
 "write": {"task": "Write an async function `loadOrder(id)` that awaits `fakeServer(id)` and returns the order. If the server rejects, catch the error and return `null` instead. Then log `await loadOrder(1)` (an order) and `await loadOrder(99)` (null).", "starter": "const fakeServer = id => new Promise((resolve, reject) => {\n  setTimeout(() => {\n    if (id === 1) resolve({ id: 1, name: \"OA-1001\", brand: \"Kontoor\" });\n    else reject(new Error(\"Record not found\"));\n  }, 10);\n});\n", "test": "const a = await loadOrder(1);\ncheck(a && a.name === \"OA-1001\", \"loadOrder(1) should return the order\");\nconst b = await loadOrder(99);\ncheck(b === null, \"loadOrder(99) should return null\");\ncheck(/async/.test(__code) && /await/.test(__code) && /catch/.test(__code), \"Use async, await and try/catch\");", "solution": "const fakeServer = id => new Promise((resolve, reject) => {\n  setTimeout(() => {\n    if (id === 1) resolve({ id: 1, name: \"OA-1001\", brand: \"Kontoor\" });\n    else reject(new Error(\"Record not found\"));\n  }, 10);\n});\nasync function loadOrder(id) {\n  try {\n    return await fakeServer(id);\n  } catch (err) {\n    return null;\n  }\n}\nconsole.log(await loadOrder(1));\nconsole.log(await loadOrder(99));"},
 "quiz": [
  {"q": "What does an async function always return?", "opts": ["undefined", "A promise", "A string", "Whatever you return, unchanged"], "ans": 1, "why": "Even return 5 becomes a promise that resolves to 5."},
  {"q": "How do you handle a rejected await?", "opts": ["if (error)", "try / catch", "Promise.ignore", "You can't"], "ans": 1, "why": "A rejected promise makes await throw, so try/catch handles it."},
  {"q": "Two independent server calls should be…", "opts": ["awaited one by one", "started together with Promise.all", "run in a while loop", "avoided"], "ans": 1, "why": "Starting them together saves time."}
 ]
},
]
