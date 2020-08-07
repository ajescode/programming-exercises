def solution(n):
    s = [[0 for i in range(n + 1)] for j in range(n + 1)]

    s[0][0] = 1

    for i in xrange(1, n + 1):
        for k in xrange(0, n + 1):
            s[i][k] = s[i - 1][k]
            if k >= i:
                s[i][k] += s[i - 1][k - i]
    return s[n][n] - 1
