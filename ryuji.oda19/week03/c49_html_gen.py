class HTMLGen:

    def __init__(self):
        self._comment = ['<!--','','-->']
        self._title = ['<title>','','</title>']
        self._body = ['<body>','</body>']
        self._div = ['div','</div>']
        self._p = ['<p>','</p>']

        self.string = ''

    def __getattr__(self, item):
        return 'There is nothing tag like that.'

    def comment(self, item):
        self._comment[1] = item
        for i in range(len(self._comment)):
            self.string += self._comment[i]
        return self.string

    def title(self, item):
        self._title[1] = item
        for i in range(len(self._title)):
            self.string += self._title[i]
        return self.string


print(HTMLGen().comment("Hello!!"))