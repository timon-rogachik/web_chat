import validators


def url_her(text):
    if "https://" in text or "www" in text:
        for i in range (0, len(parsing(text)[1])):
            if validators.url(parsing(text)[1][i]):
                return True
    return False

def parsing(text):
    other = text.split('https://')
    links = []
    for h in range(0, len(other)):
        links.append('')
    for p in range(1, len(other)):
        half_link = other[p]
        link = half_link.split(" ")[0]
        if not validators.url('https://'+link):
            link = 'https://'+half_link.split(",")[0]
        if validators.url('https://'+link):
            links[p] = 'https://'+link.replace(",", "")
        other[p] = other[p].replace(link.replace(",", ""), "")

    result = ""
    for f in range(0, len(other)):
        result+=(links[f]+other[f])
    print(other, " | ", links, " | ", result)
    return (other, links, result)


# print(parsing("сылкаааааааа: https://stackoverflow.com/questions/1107737/numeric-for-loop-in-django-templates рабоооооотаай!!!"))

