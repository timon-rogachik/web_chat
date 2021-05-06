border_key = "),<-|<_*/*\*_>|->,("
def translate_ltt(list):
    string = ""
    for i in range(0, len(list)):
        string += list[i]
        if not i == len(list)-1:
            string += border_key

    return string

def translate_ttl(text):
    return text.split(border_key)