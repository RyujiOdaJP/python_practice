import re


def regex_html(item):
    if item != '':
        return re.sub(r'<.+?>', '', item)

    else:
        return ''


# print(regex_html("<html lang = 'pl' ><body>content of body</body>...</html>"))
# print(regex_html(3,'(hello) Welcome to KIT (Kirirom Institute of Technology)!'))
# print(regex_html(''))
