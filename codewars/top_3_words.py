import re

def top_3_words(text):
    exp = re.compile("[a-z']+", re.IGNORECASE | re.ASCII)
    words_list = exp.findall(text)
    if len(words_list) == 0:
        return list()
    words_list = [x.lower() for x in words_list]
    words_list = sorted(words_list, key = words_list.count, reverse = True)
    top_3, k = list(), 0
    while (k < 3) and (len(words_list) > 0):
        top_3.append(words_list[0]) 
        words_list = words_list[0 + words_list.count(words_list[0]):]
        k+=1

    return top_3[:k]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")