List = list()
given_word = input('Enter something: ').replace(' ', '')

if given_word == '':
    print("EMPTY")

elif len(given_word) == 1:
    print(given_word[0].upper())

else:
    item = '-'
    combine = ''
    for i in range(len(given_word)):
        if i + 1 == len(given_word):
            item = ''
        List.append(given_word[i] * (i + 1) + item)

    for x in range(len(given_word)):
        combine = combine + List[x].title()
    print(combine)
