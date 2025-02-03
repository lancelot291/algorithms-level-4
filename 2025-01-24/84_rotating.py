
# has issues with strings like "([)]"
'''
def good_str(s):
    left_s = 0
    right_s = 0
    left_m = 0
    right_m = 0
    left_b = 0
    right_b = 0
    for i in range(len(s)):
        if s[i] == '(':
            left_s += 1
        elif s[i] == ')':
            right_s += 1
        elif s[i] == '[':
            left_b += 1
        elif s[i] == ']':
            right_b += 1
        elif s[i] == '{':
            left_m += 1
        elif s[i] == '}':
            right_m += 1

        if right_s > left_s or right_m > left_m or right_b > left_b:
            return False
        
    return True
    '''

# no issues

def good_str(s):
    stack = []
    
    for char in s:
        if char == '(' or char == '[' or char == '{':  # Opening brackets
            stack.append(char)
        elif char == ')':  # Closing parenthesis
            if not stack or stack[-1] != '(':  # Check if top matches
                return False
            stack.pop()
        elif char == ']':  # Closing square bracket
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        elif char == '}':  # Closing curly bracket
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0  # Stack must be empty for a valid sequence

def good_str_2(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


def solution(s):
    cnt = 0
    for _ in range(len(s)):
        if good_str(s):  # Check if rotated version is valid
            cnt += 1
        s = s[1:] + s[0]  # Rotate left instead of right for consistency
    return cnt




# Test cases
s = "}]()[{"
print(solution(s))  # 2
