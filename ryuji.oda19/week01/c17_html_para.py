GivenWord = input('Enter a sentence: ')
HTML = []

if GivenWord == 'GENERATE':
    print('Nothing to display.')
else:
    count = 1
    while GivenWord != 'GENERATE':
        HTML.append('<p>' + GivenWord + '</p>')
        GivenWord = input('Enter a sentence: ')
        #count = count + 1

    for i in range(len(HTML)):
     print(HTML[i])
