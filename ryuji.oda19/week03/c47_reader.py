class Reader:

    @staticmethod
    def read(filename):
        output = open(filename, "r").read()
        return output

    @staticmethod
    def readlines(filename):
        output = open(filename, "r").read()
        listing = list(output.split())
        return listing

#
# print(Reader().readlines("te.txt"))
#
# print(Reader().read("te.txt"))
