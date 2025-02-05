def solution(clothes):
    dict_clothes = {}
    # make a dictionary that has the number of each type of clothes
    for cloth in clothes:
        if cloth[1] in dict_clothes:
            dict_clothes[cloth[1]].append(cloth[0])
        else:
            dict_clothes[cloth[1]] = [cloth[0]]
            
    answer = 1
    # initialize a variable 'answer': the number of combinations he can wear
            
    for i in range(len(list(dict_clothes.values()))):
        answer *= len(list(dict_clothes.values())[i]) + 1
        # he can wear each type of clothes or not wear it, 
        # so add 1 to the number of each type of clothes
        
    return answer - 1
    # he should wear at least one clothes, so subtract 1 from the answer
    
# Test cases
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))  # 5
        
