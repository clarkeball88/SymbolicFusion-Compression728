# validator.py – Unit test validator
from core import symbolic_add, symbolic_sub, symbolic_mul, symbolic_div

def validate(test_cases):
    results = []
    for (a, op, b, expected) in test_cases:
        if op == '+':
            result = symbolic_add(a, b)
        elif op == '-':
            result = symbolic_sub(a, b)
        elif op == '*':
            result = symbolic_mul(a, b)
        elif op == '/':
            result = symbolic_div(a, b)
        else:
            result = None
        results.append((result == expected, result))
    return results
