def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    L = arr[0]
    for i in range(1, len(arr)):
        L = lcm(L, arr[i])

    return L

# Test cases
arr = [2, 6, 8, 14]
print(solution(arr))  # 168