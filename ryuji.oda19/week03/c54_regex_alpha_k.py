import re


def regex_alpha_k(item):
    match = re.findall(r'[a-k]|[A-K]|[0-5]', item)
    # print(match, len(item))

    if len(match) == len(item) and item != '':
        return True

    else:
        return False

# print(regex_alpha_k('5akAaa2ca1'))
# print(regex_alpha_k(""))
