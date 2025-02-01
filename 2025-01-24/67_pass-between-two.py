def solution_0(s, skip, index):
    s_new = []
    for ch in s:
        i = 0
        while 1:
            if chr((ord(ch) + 1 - ord('a'))%26 + ord('a')) not in skip:
                ch = chr((ord(ch) + 1 - ord('a'))%26 + ord('a'))
                i+=1
            else:
                ch = chr((ord(ch) + 1 - ord('a'))%26 + ord('a'))
            if i == index:
                break
        s_new.append(ch)

    return "".join(s_new)
              

def solution(s, skip, index):
    s_new = []
    skipset = set(skip)
    for ch in s:
        i = 0
        while i < index:
            ch = chr((ord(ch) + 1 - ord('a'))%26 + ord('a'))
            if ch not in skipset:
                i += 1
        s_new.append(ch)
            
    return "".join(s_new)

s = "aukks"
skip = "wbqd"

print(solution_0(s, skip, 5))

            
            
        
        
    