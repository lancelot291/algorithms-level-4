def steps(n):
    arr = [0, 1, 2]
    for i in range(3, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]
def solution(n):
    return steps(n)%1234567

# Test cases
n = 3
print(solution(n))  # 2
    