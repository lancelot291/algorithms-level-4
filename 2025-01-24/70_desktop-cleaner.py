def solution(wallpaper):
    lst_luy = []
    for i in range(len(wallpaper)):
        index = wallpaper[i].find('#') if '#' in wallpaper[i] else 50
        lst_luy.append(index)
    luy = min(lst_luy)

    lux = 0
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            lux = i
            break
    
    lst_rdy = []
    for i in range(len(wallpaper)-1, -1, -1):
        index = wallpaper[i].rindex('#') if '#' in wallpaper[i] else 0
        lst_rdy.append(index+1)
    rdy = max(lst_rdy)  

    rdx = 0
    for i in range(len(wallpaper)-1, -1, -1):
        if '#' in wallpaper[i]:
            rdx = i+1
            break

    return [lux, luy, rdx, rdy]

# Test cases
wallpaper  = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper)) 