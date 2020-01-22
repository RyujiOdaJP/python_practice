GivenWord = []
GivenWord = input("Enter something: ")
if GivenWord == '':
    print("Nothing to display.")
else:
    Length = len(GivenWord) - 1
    LastLetter = GivenWord[Length]
    print(LastLetter)
