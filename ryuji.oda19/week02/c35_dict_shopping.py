def dict_shopping(li):
    amount = 0
    quantity = 0

    try:
        for i in range(len(li)):
            element = li[i]
            if element['price'] < 0 or element['quantity'] < 1:
                return 'Invalid JSON'
            product = float("{0:.2f}".format(element['price'])) * int(element['quantity'])
            amount += product
            quantity += int(element['quantity'])

        amount = "{0:.2f}".format(amount)
        shopping_result = ('$' + str(amount), quantity)
        return shopping_result

    except TypeError and KeyError:
        return 'Invalid JSON'
# print(dict_shopping([{'price': 123.49, 'quantity': 3}]))
# print(dict_shopping([{'price': 0.01, 'quantity': 999}]))
