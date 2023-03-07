import math
    

def sum_of_squares(n):
    n_iter = n
    result = 0
    while n_iter != 0:

        if (n_iter<4):
            result += n_iter
            return result
        else:
            max_number = 0
            max_value = 0

            for elem in range(math.floor(math.sqrt(n)), math.floor(math.sqrt(n//5)), -1):
                calc_el = pow(elem, 2)
                n_temp = n_iter // calc_el

                if (calc_el * n_temp > max_value * max_number):
                    max_number = n_temp
                    max_value = calc_el
            
            result +=  max_number
            n_iter -= max_value * max_number
        
    return result

print(sum_of_squares(15))