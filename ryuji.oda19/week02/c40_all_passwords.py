import itertools


def all_passwords(letter,length):
    l = list(set(itertools.product(letter, repeat=length)))
    print(l)
    l2 = []
    s = ''
    for i in range(len(l)):

        for x in range(length):
            s += l[i][x]

        l2.append(s)
        s = ''
    pwd = sorted(l2)
    return pwd

# print(all_passwords('ab12',3))
# print(all_passwords('AAAABC6789',3))