def solution(priorities, location):
    priorities_index = []
    for i in range(len(priorities)):
        priorities_index.append([i, priorities[i]])
        
    print(priorities_index)
    
    pop_order = []
    while len(priorities_index) > 0:
        if priorities_index[0][1] == max(priorities):
            priorities.pop(0)
            pop_order.append(priorities_index.pop(0))
        else:
            priorities = priorities[1:] + [priorities[0]]
            priorities_index = priorities_index[1:] + [priorities_index[0]]
            
        print(priorities)
    print(pop_order)
    
    for i in range(len(pop_order)):
        if pop_order[i][0] == location:
            return i + 1
        
        
# Test cases
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))  # 1
            