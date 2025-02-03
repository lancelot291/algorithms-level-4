def solution(park, routes):
    W, H = len(park[0]), len(park)

    # the location of the dog
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                dog = [i, j]
                break

    # the dog is going through the routes
    for route in routes:
        # determine the way the dog is going
        if route[0] == 'E': 
            for i in range(int(route[-1])):
                dog[1] += 1
                if dog[1] >= W or park[dog[0]][dog[1]] == 'X':
                    dog[1] -= (i+1)
                    break
        elif route[0] == 'W':
            for i in range(int(route[-1])):
                dog[1] -= 1
                if dog[1] < 0 or park[dog[0]][dog[1]] == 'X':
                    dog[1] += (i+1)
                    break
        elif route[0] == 'S':
            for i in range(int(route[-1])):
                dog[0] += 1
                if dog[0] >= H or park[dog[0]][dog[1]] == 'X':
                    dog[0] -= (i+1)
                    break
        elif route[0] == 'N':
            for i in range(int(route[-1])):
                dog[0] -= 1
                if dog[0] < 0 or park[dog[0]][dog[1]] == 'X':
                    dog[0] += (i+1)
                    break
    return dog

# Test cases
park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))  

                  