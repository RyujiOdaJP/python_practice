import random

GivenNumber = input('Enter a number: ')
for i in range(int(GivenNumber)):
    print(random.randrange(0, 2))