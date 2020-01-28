def int_list(L):
    if len(L) == 0:
        return False
    else:
        try:
            X = [isinstance(L[i],int) for i in range(len(L))]

            print(X)
            return all(X)

        except TypeError:
            return False
