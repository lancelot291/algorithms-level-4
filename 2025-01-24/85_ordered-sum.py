def solution(elements):
    elements_doubled = elements + elements
    n = len(elements)
    all_list = []
    for length in range(1, n + 1):
        for i in range(n):
            all_list.append(sum(elements_doubled[i:i + length]))
    return len(set(all_list))

# Test cases
elements = [7,9,1,1,4]
print(solution(elements))  # 28
