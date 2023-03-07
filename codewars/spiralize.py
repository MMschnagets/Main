def spiralize(size):
    spiral = [[0 for i in range(0, size)] for j in range(0, size)]
    phase_cor = 0
    current_i = 0
    current_j = 0
    zero_cor = 1
    
    while phase_cor<size - phase_cor:
        if (phase_cor + 2 > size - phase_cor - 2) and (size%2==0):
            zero_cor = 0
        for current_j in range(phase_cor - 1, size - phase_cor):
            spiral[current_i][current_j] = 1
        for current_i in range(phase_cor, size - phase_cor):
            spiral[current_i][current_j] = 1
        for current_j in range(size - phase_cor - 1, phase_cor - zero_cor, -1):
            spiral[current_i][current_j] = 1
        phase_cor +=2
        for current_i in range(size - phase_cor + 1, phase_cor - 1, -1):
            spiral[current_i][current_j] = 1

    return spiral

spiralize(7)