def p(n, c=0, a=1, b=1):
    while 1:
        a, b, c = b, (a+b) % n, c+1
        if a == 1 and b == 1:
            return c


def get_pisano_numbers(l):
    return [p(n) for n in l]
