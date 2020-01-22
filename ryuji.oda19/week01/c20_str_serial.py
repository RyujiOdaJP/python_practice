GivenWord = []
GivenWord = input('Enter something: ')

print(len(GivenWord))

if GivenWord == '':
        print("Empty")

elif len(GivenWord)==1:
        print(GivenWord[0].upper().strip(' '), end='')

else:

    print(GivenWord[0].upper().strip(' '), end='-')

    for i in range(len(GivenWord)-1):
        if i  == len(GivenWord):
            break
        print(GivenWord[i+1].upper().strip(' '), end='')

        for j in range(i+1):
            if i+1 == len(GivenWord):
                break
            print(GivenWord[i+1], end='-')
