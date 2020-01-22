GivenWord = []
GivenWord = input('Enter a word: ')
j = len(GivenWord)


def align():
    for i in range(2):
        print(GivenWord[i], end="")


def align_rev():
    for i in range(2):
        print(GivenWord[1 - i], end="")


def rev():
    k = j - 1
    for i in range(2):
        print(GivenWord[k], end="")
        k = k - 1


if j == 2:
    for i in range(2):
        align();
elif j == 1:
    for i in range(4):
        print(GivenWord[0], end="")
elif j == 0:
    print('0000')
else:
    align_rev();
    rev();