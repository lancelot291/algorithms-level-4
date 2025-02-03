def solution(s):
    s = s.split()
    s = [int(i) for i in s]
    return str(min(s)) + " " + str(max(s))

# Test cases
s = "1 2 3 4"
print(solution(s))  