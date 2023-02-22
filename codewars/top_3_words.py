import re

def top_3_words(text):
    exp = re.compile("[a-z']+", re.IGNORECASE | re.ASCII)
    words_list = exp.findall(text)
    for x in words_list:
        if (len(x) == x.count("'")):
            words_list.remove(x)
    if len(words_list) == 0:
        return list()
    words_list = [x.lower() for x in words_list]
    count_list = [words_list.count(x) for x in words_list]
    top_3, k = list(), 0
    while (k < 3) and (len(words_list) > 0):
        max_count = max(count_list)
        max_idx = count_list.index(max_count)
        max_word = words_list[max_idx]
        top_3.append(max_word)
        for i in range(0, max_count):
            tmp_idx = words_list.index(max_word)
            words_list.pop(tmp_idx)
            count_list.pop(tmp_idx)
        k+=1

    return top_3[:k]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")