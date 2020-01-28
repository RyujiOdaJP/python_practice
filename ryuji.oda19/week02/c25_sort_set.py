a = [1, 2, 3, 1, 2, 5, 6, 7, 8]
b = ['a','a','b','g']

print(sorted(list(set(a))))


def set_sort(a):
    fe = sorted(list(set(a)))
    return fe

def set_sort_rev(a):
    fe = sorted(list(set(a)), reverse=True)
    return fe
