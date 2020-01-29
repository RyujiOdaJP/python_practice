import random


def gen_pass(chars, length, numbers):
    rtn = []
    rdm = ''

    for x in range(numbers):
        for i in range(length):
            rdm += random.choice(chars)

        rtn.append(rdm)
        rdm = ''
    return rtn


# print(gen_pass('abc', 3, 2))
# print(gen_pass('aBc_*&', 5, 3))
