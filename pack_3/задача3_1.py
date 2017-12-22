SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            arr.append(c)
        elif c in SYMBOLS_R:
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return True
