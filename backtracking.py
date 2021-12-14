def get_permutari(n, stiva=[]):
    if len(stiva) == n:
        print(stiva)
        return

    for i in range(n):
        if i not in stiva:
            stiva.append(i)
            get_permutari(n, stiva)
            stiva.pop()



get_permutari(4) # 0 1 2, 0 2 1, 1 0 2, 1 2 0, 2 0 1, 2 1 0