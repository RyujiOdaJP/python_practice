GivenNumber = int(input("Enter a number: "))
if GivenNumber >= 0:

    for i in range(GivenNumber):
        count = GivenNumber - i
        print(count)

    print("BOOM!")
