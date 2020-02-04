class Writer:
    # def __init__(self,filename, text):
    #     self._filename = filename
    #     self._text = text
    #     self.f = ''
    @staticmethod
    def write(filename, text):
        output = open(filename, "w+")
        output.write(text + "\n")
        return output

    @staticmethod
    def append(filename, text):
        output = open(filename, "a+")
        output.write(text + "\n")
        return output


# Writer().write("te.txt", "hahaha")
