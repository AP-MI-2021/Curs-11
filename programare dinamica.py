"""
C(n, k) = n!/(k!(n-k)!)
C(n, k) = cate combinari de n luate cate k exista
C(n, k) = 1                           k = 0
        = 1                           k = n
        = C(n-1, k-1) + C(n-1, k)   , else

C(40, 20) = C(39, 19) + C(39, 20)
          = C(38, 18) + C(38, 19) + C(38, 19) + C(38, 20)
                        ^^^^^^^^^^^^^^^^^^^^^
                        Subprobleme suprapuse
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

def cnk_rec(n, k):
    if k == 0 or n == k:
        return 1

    return cnk_rec(n-1, k-1) + cnk_rec(n-1, k)

#print(cnk_rec(40, 20)) - foarte incet


def cnk_iter(n, k):
    cnk = [[1, 0]]
    for i in range(1, n+1):
        cnk.append([1] * (i + 1))
        cnk[-1].append(0)
        for j in range(1, i+1):
            cnk[i][j] = cnk[i - 1][j - 1] + cnk[i - 1][j]

    return cnk[n][k]

print(cnk_iter(40, 20))


def cnk_memoized(n, k):

    d = {}
    def inner(n, k):
        if k == 0 or n == k:
            return 1

        if (n, k) in d:
            return d[(n, k)]
        d[(n, k)] = inner(n - 1, k - 1) + inner(n - 1, k)
        return d[(n, k)]

    return inner(n, k)

print(cnk_memoized(40, 20))
