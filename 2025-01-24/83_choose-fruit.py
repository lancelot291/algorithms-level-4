def solution(k, tangerine):
    M = max(tangerine)

    # Count the number of each size of tangerine
    fruit_size_num = {}
    for i in range(1, M+1):
        fruit_size_num[i] = 0
    for i in tangerine:
        fruit_size_num[i] += 1

    
    # a list that has the sorted number of each size of tangerine
    fruit_size_list = sorted(fruit_size_num.values(), reverse=True)

    kind = 0
    sum = 0
    for i in range(len(fruit_size_list)):
        sum += fruit_size_list[i]
        if sum >= k:
            kind = i+1
            break
    return kind

# Test cases
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))  # 3