class MathsModule:

    @staticmethod
    def get_min(item):
        return min(item)

    @staticmethod
    def get_max(item):
        return max(item)

    @staticmethod
    def get_min_max(item):
        smallest = min(item)
        largest = max(item)
        return smallest, largest

    @staticmethod
    def average(item):
        amount = 0
        for i in range(len(item)):
            amount += item[i]
        ave = amount / len(item)
        return ave

    @staticmethod
    def diff(item):
        return max(item) - min(item)

# numbers = [1,2,3,4,5]
# print(MathsModule().get_min(numbers))
# print(MathsModule.get_max(numbers))
# print(MathsModule.get_min_max(numbers))
# print(MathsModule.average(numbers))
# print(MathsModule.diff(numbers))
