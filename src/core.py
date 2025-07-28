# core.py – Core symbolic operations
from macros import get_macro
from constants import mirrored_map

def symbolic_add(a, b):
    return [x + y for x, y in zip(a, b)]

def symbolic_sub(a, b):
    return [x - y for x, y in zip(a, b)]

def symbolic_mul(a, b):
    return [a[0]*b[0], a[1]*b[1]]

def symbolic_div(a, b):
    if b[0] == 0 or b[1] == 0:
        raise ZeroDivisionError("Symbolic divide by zero")
    return [a[0] // b[0], a[1] // b[1]]

def symbolic_not(a):
    return [~x for x in a]

def symbolic_and(a, b):
    return [x & y for x, y in zip(a, b)]

def symbolic_or(a, b):
    return [x | y for x, y in zip(a, b)]

def symbolic_xor(a, b):
    return [x ^ y for x, y in zip(a, b)]
