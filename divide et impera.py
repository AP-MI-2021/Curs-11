lst = [2, 4, 6, 7, 11, 12, 12, 13, 13, 13, 15, 20, 23, 101]


def binary_search(lst, v):
    """
    return True daca v e in lst si False altfel.
    :param lst:
    :param v:
    :return:
    """
    st = 0
    dr = len(lst) - 1

    while st < dr:
        m = st + (dr - st) // 2 # (st + dr) // 2
        if lst[m] < v:
            st = m + 1
        else:
            dr = m

    return lst[st] == v


print(2, binary_search(lst, 2))
print(101, binary_search(lst, 101))
print(1, binary_search(lst, 1))
print(213, binary_search(lst, 213))
print(12, binary_search(lst, 12))
print(13, binary_search(lst, 13))
print(15, binary_search(lst, 15))
print(14, binary_search(lst, 14))


"""
a**n    = 1                     daca n = 0
        = (a**(n/2))**2         daca n = 2k
        = (a**((n-1)/2))**2*a   daca n = 2k+1

"""