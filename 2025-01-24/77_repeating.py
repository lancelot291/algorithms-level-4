def solution(s):
    cnt_loop = 0
    cnt_zero = 0
    while s != '1':
        len_1 = len(s)
        s = s.replace('0', '')
        len_2 = len(s)
        c = len(s)
        s = bin(c)[2:]
        cnt_loop  += 1
        cnt_zero += len_1 - len_2

    return [cnt_loop, cnt_zero]

# Test cases
s = "110010101001"
print(solution(s))

