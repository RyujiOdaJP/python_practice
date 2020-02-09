import requests as req


def get_html(url):
    resp = req.get(url)
    content = resp.text
    return content

print(get_html('https://w3resource.com/'))
