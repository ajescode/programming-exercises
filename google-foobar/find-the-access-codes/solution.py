#I don't think this should be acceptable solution. Test case [1, 1, 1, 1] should return 1, not 4. Every element of this is case is the same, so should be accepted only unique passcodes. There is a lack of mention in the description of this task about this concern.
def solution(l):
    accesscodes = 0
    size = len(l)

    divisors = [0] * size

    for i in range(size - 1):
        for j in range(i + 1, size):
            if l[j] % l[i] == 0:
                divisors[i] += 1

    for i in range(size - 2):
        for j in range(i + 1, size - 1):
            if l[j] % l[i] == 0:
                accesscodes += divisors[j]

    return accesscodes
