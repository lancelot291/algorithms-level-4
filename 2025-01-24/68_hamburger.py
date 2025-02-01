def solution(ingredient):
    pattern = [1, 2, 3, 1]
    stack = []
    cnt = 0
    for n in ingredient:
        stack.append(n)
        if stack[-4:] == pattern:
            cnt += 1
            del stack[-4:]
      

    return cnt

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
