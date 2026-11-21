PY = [
 ("Basics", ["Running Python and print()", "Variables and types", "Numbers and arithmetic", "Strings: the basics", "String methods and f-strings", "Input and type conversion", "Booleans and comparisons", "if / elif / else"]),
 ("Loops", ["while loops", "for loops and range()", "break, continue and loop else", "Practice: number games"]),
 ("Data structures", ["Lists", "List methods and slicing", "Tuples and unpacking", "Dictionaries", "Dictionary methods and looping", "Sets", "Comprehensions", "Nested data (lists of dicts)"]),
 ("Functions", ["Defining functions", "Parameters and defaults", "*args and **kwargs", "Scope and the LEGB rule", "Lambdas, sorted() and key=", "Recursion", "Docstrings and type hints"]),
 ("Files and errors", ["Exceptions: try / except", "raise and custom exceptions", "Files and the with statement", "JSON and CSV"]),
 ("Object-oriented programming", ["Classes and objects", "__init__ and attributes", "Instance, class and static methods", "Inheritance and super()", "Multiple inheritance and the MRO", "Dunder methods", "Properties", "Abstract classes and composition", "Project: a mini ORM model"]),
 ("Modules", ["Modules and imports", "Packages, venv and pip"]),
 ("Intermediate Python", ["Iterators and the iterator protocol", "Generators and yield", "Closures", "Decorators", "Decorators with arguments", "Context managers", "itertools and functools"]),
 ("Advanced Python", ["Typing in depth", "Dataclasses and enums", "Descriptors (how fields work)", "Metaclasses (how Odoo registers models)", "async / await", "Performance and profiling"]),
 ("Professional Python", ["Testing with unittest and pytest", "Logging and debugging", "Python and PostgreSQL", "How Odoo's ORM uses all of this", "Capstone project"]),
]
JS = [
 ("Modern JavaScript", ["JavaScript in the browser and console.log", "let, const and types", "Strings and template literals", "Conditions and equality", "Loops", "Arrays and array methods", "Objects", "Functions and arrow functions", "Destructuring and spread", "Scope, closures and this", "Classes", "Modules: import and export", "Promises", "async / await"]),
 ("The DOM", ["Selecting and changing the page", "Events", "Practice: a to-do list in plain JavaScript"]),
 ("OWL 3 basics", ["What OWL is: your first component", "Templates: t-out, t-if, t-foreach", "Props", "Event handling with t-on", "Signals: reactive state", "computed() and effect()", "Forms and t-model"]),
 ("OWL components", ["Lifecycle hooks", "Sub-components and composition", "Slots", "Child-to-parent communication", "Refs", "Lists and keys", "Practice: a shipment tracker widget"]),
 ("Advanced OWL", ["The environment and plugins", "Writing your own hooks", "Async loading", "Performance", "OWL 2 to OWL 3: what changed"]),
 ("OWL in Odoo 20", ["JS assets in an Odoo module", "Services: orm, notification, action", "Registries", "Patching existing components", "Field widgets", "Systray items and client actions", "Views: the basics", "Testing your components", "Capstone project"]),
]
def flat(units, prefix):
    out = []
    for unit, titles in units:
        for t in titles:
            out.append({"id": f"{prefix}{len(out)+1:02d}", "track": prefix, "n": len(out)+1, "unit": unit, "title": t})
    return out
def schedule():
    py, js = flat(PY, "py"), flat(JS, "js")
    days, i, j = [], 0, 0
    while i < len(py) or j < len(js):
        if i < len(py): days.append(py[i]["id"]); i += 1
        if j < len(js): days.append(js[j]["id"]); j += 1
    return py, js, days
