def p(n):
    c, f = 0, [1, 1]
    while 1:
        f.append((f[-2]+f[-1]) % n)
        c += 1
        if f[-1] == 1 and f[-2] == 1:
            return c


def get_pisano_numbers(l):
    return [p(n) for n in l]
