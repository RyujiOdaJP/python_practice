List = list()
given_word = input("Enter something: ")

if given_word == "":
    print("Nothing to display.")

else:

    combine = ''
    for i in range(len(given_word)):
        List.append(given_word[-i - 1])

    for x in range(len(given_word)):
        combine = combine + List[x]

    print(combine)
