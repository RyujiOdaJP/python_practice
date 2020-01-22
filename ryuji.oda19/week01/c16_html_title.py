GivenWord = input("Enter a title: ")
HTML = "<h1>" + GivenWord + "</h1>"

if GivenWord == '':
    print('Nothing to display.')
else:
    print(HTML)
