def solution(progresses, speeds):
    days_left = []
    for i in range(len(progresses)):
        days_left.append((100 - progresses[i] + speeds[i] - 1) // speeds[i])
        # calculate the number of days left for each progress and append to the list
    for i in range(1, len(days_left)):
        if days_left[i] < days_left[i - 1]:
            days_left[i] = days_left[i - 1]
            # if the number of days left for the progress is less than the previous one,
            # change the number of days left to the previous one
            # ex) [5, 10, 1, 1, 20, 1] -> [5, 10, 10, 10, 20, 20]
            
        set_days_left = set(days_left)
        # make a set of the number of days left ex) {5, 10, 20}
        
        answer = []
        
        for i in sorted(set_days_left):
            answer.append(days_left.count(i))
            
    return answer

# Test cases
progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))  # [2, 1]