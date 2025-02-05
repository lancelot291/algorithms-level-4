def solution(want, number, discount):
    total_dict = {}
    # make a dictionary that has the number of things that he wants to buy
    for i in range(len(want)):
        total_dict[want[i]] = number[i]
        #add the values to the dictionary
        
    cnt = 0
    # initialize a variable cnt(the number of days that he can buy all the things he wants)
    for i in range(len(discount) - 9):
        ten_day_list = discount[i:i + 10]
        temp_dict = {}
        # make a dictionary thst has the number of each item that is in sale for the 10 days
        for item in ten_day_list:
            if item in temp_dict:
                temp_dict[item] += 1
            else:
                temp_dict[item] = 1
        if temp_dict == total_dict:
            cnt += 1
            # if the dictionary of the 10 days is the same as 
            # the dictionary of the number of items he wants to buy, add 1 to cnt
    return cnt

# Test cases
want  = ["banana", "apple", "rice", "pork", "pot"]
number  = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))  
