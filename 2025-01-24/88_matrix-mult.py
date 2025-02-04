def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            arr.append(temp)
        ans.append(arr)

    return ans

# Test cases
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))  # [[22, 18, 11], [36, 28, 18], [29, 20, 14]]