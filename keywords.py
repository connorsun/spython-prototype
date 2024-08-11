py_to_s_keywords = {
    "False": "Falso",
    "None": "Ninguno",
    "True": "Verdad",
    "and": "y",
    "as": "como",
    "assert": "afirma",
    "async": "asinc",
    "await": "espera",
    "break": "rompe",
    "class": "clase",
    "continue": "continua",
    "def": "def",
    "del": "borra",
    "elif": "sinosi",
    "else:": "sino:",
    "except": "excepto",
    "finally": "final",
    "for": "por",
    "from": "de",
    "global": "global",
    "if": "si",
    "import": "importa",
    "in": "en",
    "is": "es",
    "lambda": "lambda",
    "nonlocal": "no local",
    "not": "no",
    "or": "o",
    "pass": "pasa",
    "raise": "eleva",
    "return": "devuelve",
    "try:": "intenta:",
    "while": "mientras",
    "with": "con",
    "yield": "produce",
    "input": "introducir",
    "print": "imprimir"
    }
# excepto could be iffy
# nonlocal is makey uppy
# deal with else, elif, and not
# raise: keep as raise or throw?
s_to_py_keywords = {val: key for key, val in py_to_s_keywords.items()}