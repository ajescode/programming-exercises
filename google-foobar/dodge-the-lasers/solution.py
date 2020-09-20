sqrt1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


def solution(s):
    n = long(s)
    return str(beatty(n))


def beatty(n):
    if n < 1:
        return 0

    np = (sqrt1 * n) // 10 ** 100

    return n * np + n * (n + 1) / 2 - (np * (np + 1)) / 2 - beatty(np)


