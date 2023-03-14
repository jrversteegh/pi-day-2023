def p(n, c=1, a=1, b=2):
    while a != 1 or b != 1:
        a, b, c = b, (a+b) % n, c+1
    return c


def get_pisano_numbers(l):
    return [p(n) for n in l]
