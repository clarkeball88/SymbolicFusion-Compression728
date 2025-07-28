# encoder.py – Symbolic-to-binary encoder with macro folding
from macros import macro_library

def encode_symbolic(symbolic_value):
    return ''.join(format(x, '06b') for x in symbolic_value)

def fold_macros(program):
    folded = []
    for instruction in program:
        if instruction in macro_library:
            folded.append(f"MACRO_{instruction}")
        else:
            folded.append(encode_symbolic(instruction))
    return folded
