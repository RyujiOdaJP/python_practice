GivenWord = []
GivenWord = input("Enter something: ")
if GivenWord == "":
    print("Nothing to display.")
else:
    i = 1
    Length = len(GivenWord)
    while i <= Length :
        reverse = Length - i
        print(GivenWord[reverse] ,end = "")
        i = i + 1
