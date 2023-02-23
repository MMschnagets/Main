def next_bigger(n):
    if (n<10):
        return -1
    str_n = str(n)
    digits_list = [int(x) for x in str_n]
    digits_list.reverse()
    length = len(digits_list)

    for i in range(0, length):
        for j in range(i + 1, length):
            if (digits_list[i]>digits_list[j]):
                digits_list[j], digits_list[i] = digits_list[i], digits_list[j]
                str_num = str()
                digits_list.reverse()
                for k in digits_list:
                    str_num += str(k)
                return int(str_num)
    
    return -1

next_bigger("144")