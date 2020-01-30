import random


def gen_passwords(chars, length, numbers):
    rtn = []
    rdm = ''

    for x in range(numbers):
        for i in range(length):
            rdm += random.choice(chars)

        rtn.append(rdm)
        rdm = ''
    return rtn


# print(gen_passwords('abc', 3, 2))
# print(gen_passwords('aBc_*&', 5, 3))
