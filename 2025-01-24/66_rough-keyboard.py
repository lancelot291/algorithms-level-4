
def solution(keymap, targets):
    
    answer_list = []
    for target in targets:
        min_presses = []
        flag = 0
        for ch in target:
            if ch not in "".join(keymap):
                min_presses.append(-1)
                flag = 1
                break
            else:
                arr = []
                for text in keymap:
                    press = (text.find(ch) + 1) if ch in text else 100
                    arr.append(press)
                min_presses.append(min(arr))
        answer_list.append(sum(min_presses)if flag == 0 else '')

    return answer_list

# Test cases
keymap = ["ABACD", "BCEFD"]
targets = ["ABCD", "AABB"]
print(solution(keymap, targets)) 


                
            

