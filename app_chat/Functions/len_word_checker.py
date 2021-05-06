def insert(text, element, thing):
    result = list(text)
    result[element] = result[element]+thing
    return "".join(result)

def check_end_return(text, mode='mess'):
    max_len = len("ааааааааааааааааааааааааааааааааааааааааа")
    if mode == 'cnv_mode':
        max_len = len("ааааааааааааааааааааааааааааааааааааа")
    word_len_count = 0
    count = 0
    text = text
    for i in text:
        count += 1
        if not i == " ":
            word_len_count += 1
        else:
            word_len_count = 0
        if word_len_count >= max_len:
            word_len_count = 0
            text = insert(text, count, " ")
    return text

