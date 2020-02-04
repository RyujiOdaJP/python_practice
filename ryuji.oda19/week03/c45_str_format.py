class StringFormat:

    @staticmethod
    def first(word):
        return word[0]

    @staticmethod
    def last(word):
        return word[-1]

    @staticmethod
    def lower(word):
        return word.lower()

    @staticmethod
    def upper(word):
        return word.upper()

    @staticmethod
    def reversed(word):
        return word[::-1]


# str_format = StringFormat()
# print(str_format.first("Python"))
# print(str_format.last("Python"))
# print(str_format.lower("Python"))
# print(str_format.upper("Python"))
# print(str_format.reversed("Python"))
