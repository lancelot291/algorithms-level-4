def solution(citations):
    citations.sort(reverse=True) # we sort the list in descending order
    # [6, 5, 3, 1, 0]
    h = 0 #initialize h-index to 0
    for i, citation in enumerate(citations): #enumerate the list
        # because 'citaions' is sorted in descending order, 
        # comparing i, which gets increased by 1 each time, 
        # with the value of the citation 
        # until i gets bigger than the value returns the h-index
        if citation >= i + 1:
            h = i + 1
        else:
            break
    return h

'''
Checking h = 2

there are more than two (3) papers that have 2 or more citations
Remaining 2 papers have ≤ 2 citations (1,0) "check"

'''

     



