def solution(survey, choices):
    result = ''
    score = {'R': 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            score[survey[i][0]] += 4 - choices[i]



    for i in range(0,7,2): 
        lst = list(score.keys())
        if score[lst[i]] > score[lst[i+1]]:
            result += lst[i]
        elif score[lst[i]] < score[lst[i+1]]:
            result += lst[i+1]
        elif score[lst[i]] == score[lst[i+1]]:
            ch = lst[i] if ord(lst[i]) < ord(lst[i+1]) else lst[i+1]
            result += ch

    return result
            
 



survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))  

    

    