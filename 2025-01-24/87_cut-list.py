def solution(n, left, right):
    arr = [[n]*n for i in range(n)]
    for i in range(0, n):
        arr[i][i] = i+1
        for j in range(0, i):
            arr[i][j] = i+1
            arr[j][i] = i+1
    

    onedim_list = []
    for i in range(n):
        onedim_list += arr[i]

    return onedim_list[left:right+1]

def solution(n, left, right):
    result = []  # Initialize result list
    
    for index in range(left, right + 1):  
        row = index // n  # Calculate row index
        col = index % n   # Calculate column index
        result.append(max(row, col) + 1)  # Compute value
    
    return result  # Return the extracted portion




# Test cases
n = 3
left = 2
right = 5
print(solution(n, left, right))  # [3, 3, 3, 2]
        
    


