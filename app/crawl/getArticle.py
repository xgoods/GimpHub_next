import lxml.html

def get_generic_title(url):

    t = lxml.html.parse(url)
    return t.find(".//title").text

def get_generic_article(url):
    t = lxml.html.parse(url)
    out = ""
    for article in t.find(".//article"):
        out += article.text
    if out.isspace():
        return None
    return out

def get_generic_image(url):
    t = lxml.html.parse(url)

    img = t.find("//img")
    return img.get('src')

#print get_generic_image('http://www.quickmeme.com/p/3vzw6l')


