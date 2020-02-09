import re


def regex_word(length, item):
    itemlist = list(item.split())
    print(itemlist)

    if length > 0 and item != '':
        return re.sub('[a-zA-Z0-9]{0,4}','',item)

    else:
        return ''

# print(regex_word(3,'5akAaa2??ca1 oda aO emak'))
# print(regex_word(3,";l"))
