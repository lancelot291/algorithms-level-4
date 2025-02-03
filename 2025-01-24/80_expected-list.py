def solution(n,a,b):
    cnt = 0
    while 1:
        if a == b:
            return cnt
        a = (a+1)//2
        b = (b+1)//2
        cnt+=1

# Test cases
n = 8
a = 4
b = 7
print(solution(n,a,b))  # 3
