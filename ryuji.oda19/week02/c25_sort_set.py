def sort_set(a):
    fe = sorted(list(set(a)))
    return fe


def sort_set_rev(a):
    fe = sorted(list(set(a)), reverse=True)
    return fe

#
# a = [1, 2, 3, 1, 2, 5, 6, 7, 8]
# b = ['a','a','b','g']
#
# print(sort_set(b))
# print(sort_set_rev(b))
