class HTMLGen:

    def __init__(self):
        self._comment = ['<!--', '', '-->']
        self._title = ['<title>', '', '</title>']
        self._body = ['<body>', '', '</body>']
        self._div = ['<div>', '', '</div>']
        self._p = ['<p>', '', '</p>']
        self._href = ['<a href="', '', '">', '', '</a>']

        self.string = ''

    def __getattr__(self, item):
        return self.comment(item)

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

    def body(self, item):
        self._body[1] = item
        for i in range(len(self._body)):
            self.string += self._body[i]
        return self.string

    def div(self, item):
        self._div[1] = item
        for i in range(len(self._div)):
            self.string += self._div[i]
        return self.string

    def p(self, item):
        self._p[1] = item
        for i in range(len(self._p)):
            self.string += self._p[i]
        return self.string

    def href(self, link, item):
        self._href[1] = link
        self._href[3] = item
        for i in range(len(self._href)):
            self.string += self._href[i]
        return self.string


print(HTMLGen().comment("Hello!!"))
print(HTMLGen().title("Hello!!"))
print(HTMLGen().body("Hello!!"))
print(HTMLGen().div("Hello!!"))
print(HTMLGen().p("Hello!!"))
print(HTMLGen().href("python.org", "Hello!!"))
# print(HTMLGen().a("Hello!!"))

