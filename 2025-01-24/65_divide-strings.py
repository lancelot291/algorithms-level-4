def solution(s):
    cnt = 0
    i = 0
    while i < len(s):
        x = s[i]
        x_same = 0
        x_diff = 0
        while i < len(s):
            if s[i] == x:
                x_same += 1
            else:
                x_diff += 1

            i+=1


            if x_same == x_diff:
                break
        cnt+=1

    return cnt
        
        







def solution_recursion(s):
    if len(s) <= 1:
        return 0
    x = s[0]
    x_same, x_diff = 0, 0
    for i in range(1, len(s)):
        if s[i] == x:
            x_same += 1
        else:
            x_diff += 1

        if x_same == x_diff:
            return 1 + solution_recursion(s[i+1:])
        elif i == len(s) - 1:
            return 1 

def solution_2(s, cnt = 0):  
    # only initializes when the second argument is not provided
    if len(s) <= 1:
        return cnt
    x = s[0]
    x_same, x_diff = 0, 0
    for i in range(len(s)):
        if s[i] == x:
            x_same += 1
        else:
            x_diff += 1

        if x_same == x_diff:
            return solution_2(s[i+1:], cnt + 1)
    return cnt+1



            
    



print(solution_2("banana"))
            

