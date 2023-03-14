def p(n):
    c, a, b = 0, 1, 1
    while 1:
        a, b = b, (a+b) % n
        c += 1
        if a == 1 and b == 1:
            return c


def get_pisano_numbers(l):
    return [p(n) for n in l]
