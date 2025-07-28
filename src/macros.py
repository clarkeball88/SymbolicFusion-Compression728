# macros.py – Symbolic macros
macro_library = {
    'PI': [2, 2, 7],
    'SQRT2': [9, 9, 7, 0],
    'PHI': [8, 9, 5, 5],
}

def get_macro(name):
    return macro_library.get(name.upper(), [])
