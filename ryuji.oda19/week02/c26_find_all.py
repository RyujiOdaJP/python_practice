def find_all(a, b):
    position = []

    for i in range(len(a)):
        if a[i] == b:
            position.append(i)

    if not position:
        return None

    return position


def find_first(a, b):
    try:
        firstone = a.index(b)
        return firstone

    except ValueError:
        return None
#
# print(find_all([8, 8, 8], 8))
# print(find_first([1, 2, 3, 1, 2, 3, 1, 2, 3], 1))
# print(find_all([1, 2, 3, 1, 2, 3, 1, 2, 3], 4))
