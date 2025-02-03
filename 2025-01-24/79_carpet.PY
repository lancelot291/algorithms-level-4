def solution(brown, yellow):
    for i in range(1, yellow + 3):
        for j in range(1, i+1):
            if 2*i + 2*j - 4 ==brown and i*j == yellow + brown:
                return [i, j]
            

# Test cases
brown = 10
yellow = 2
print(solution(brown, yellow))  # [4, 3]