GivenNumber = int(input("Enter a number: "))
if GivenNumber > 0:

    i = 0
    for i in range(GivenNumber):
        count = GivenNumber - i
        print(count)
        i = i + 1

elif GivenNumber==0:
    print("BOOM!")
