def find_all(a,b):
    position = []

    for i in range(len(a)):
        if a[i] == b:
            position.append(i)

        if position == []:
            position = None

    return position

def find_first(a,b):
    firstone = a.index(b)
    return firstone
