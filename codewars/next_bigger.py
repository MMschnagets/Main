def next_bigger(n):
    if (n<10):
        return -1
    str_n = str(n)
    dict_unique = {}
    length = len(str_n)
    for k in str_n:
        if k not in dict_unique.keys():
            dict_unique.update({k: str_n.count(k)})
    x = n + 1
    while x < pow(10, length):
        str_x = str(x)
        count_of_digits = 0
        for k in dict_unique.keys():
            if dict_unique.get(k) == str_x.count(k):
                count_of_digits+=str_x.count(k)
        if count_of_digits == length:
            return x
        x+=1
    return -1

print(next_bigger(249891781))