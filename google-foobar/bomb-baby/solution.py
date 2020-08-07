def solution(x, y):
    x = long(x)
    y = long(y)
    cycles = 0
    while x > 1 and y > 1:
        cycles += long(x / y)
        x, y = y, x % y

    if y == 1:
        cycles += x - 1
        x = 1

    if x != 1 and y != 1:
        cycles = 'impossible'

    return str(cycles)
