def list_number(a,b,reversed=False):
    L = []
    sum1 = a


    for i in range(b - a + 1):
        L.append(sum1)
        sum1 += 1
    R = sorted(L, reverse = reversed)
    return R
