import re


def regex_para(item):

    if item != '':
        return re.sub(r'\([^)]*\)','',item)

    else:
        return ''

# print(regex_para(3,'5akAaa2??ca1 opo aO emak'))
# print(regex_para(3,'(hello) Welcome to KIT (Kirirom Institute of Technology)!'))

