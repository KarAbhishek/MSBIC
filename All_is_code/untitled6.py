def isCircular(path):
    x = 0
    y = 0
    dir = 0
    path = path * 4 
    for i in range(len(path)):
        move = path[i]
        if move == 'R':
            dir = (dir + 1)%4
        elif move == 'L':
            dir = (4 + dir - 1)%4
        else:
            if dir == 0:
                y += 1
            elif dir == 1:
                x += 1
            elif dir == 2:
                y -= 1
            else:
                x -= 1
 
    return (x == 0 and y == 0)
    
print(isCircular('GR'))