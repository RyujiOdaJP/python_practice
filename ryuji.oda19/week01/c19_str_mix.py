given_word = input('Enter a word: ')
j = len(given_word)


def align(word):
    align_word = ""
    for i in range(2):
        align_word += word[i]
    return align_word


def align_rev(word):
    align_rev_word = ""
    for i in range(2):
        align_rev_word += word[-i + 1]
    return align_rev_word


def rev(word):
    rev_word = ""
    for i in range(2):
        rev_word += word[-i - 1]
    return rev_word


if j == 2:

    print(align(given_word) * 2)

elif j == 1:
    print(given_word[0] * 4)

elif j == 0:
    print('0000')

else:
    print(align_rev(given_word) + rev(given_word))
