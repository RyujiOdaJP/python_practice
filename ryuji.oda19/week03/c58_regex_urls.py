import re


def regex_urls(item):
    if item != '':
        result = re.findall(r'http[\w\d/:%#$&?()~_.=+-]+', item)
        return result
    else:
        return []

#
# print(regex_urls('<a href="https://w3resource.com">Python</a><a href="http://github.com">'))
# print(regex_urls(''))
# print(regex_urls("search engine: ​ http://www.google.com​ "))
