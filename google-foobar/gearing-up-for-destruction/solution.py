from fractions import Fraction


def solution(pegs):
    n = len(pegs)

    if n <= 1:
        return [-1, 1]

    is_even = True if n % 2 == 0 else False

    formula = 0
    if n > 2:
        for i in xrange(1, n - 1):
            formula += 2 * (-1) ** (i + 1) * pegs[i]

    formula -= pegs[0]
    formula += pegs[n - 1] if is_even else -pegs[n - 1]
    formula = float(formula)

    r1 = Fraction(formula * 2 / 3 if is_even else 2 * formula).limit_denominator()

    if r1 < 2:
        return [-1, -1]

    dist = pegs[0] + r1
    for k in xrange(1, n - 1):
        current_r = pegs[k] - dist
        if current_r >= 1:
            dist = dist + 2 * current_r
        else:
            return [-1, -1]

    return [r1.numerator, r1.denominator]
