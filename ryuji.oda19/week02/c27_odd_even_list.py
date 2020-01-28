def odd_even_list(a):
    judge = []

    for i in range(len(a)):
        if a[i] % 2 == 0:
            judge.append('EVEN')

        elif a[i] % 2 != 0:
            judge.append('ODD')

        elif a == []:
            judge = []

    return judge
