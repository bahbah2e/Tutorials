# -----------
# User Instructions:
# 
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    x = init[0]
    y = init[1]
    g = 0
    step = 1

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            expand[x][y] = step
            step += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    
    return expand

def path(expand, goal):
    path = [['' for row in range(len(grid[0]))] for col in range(len(grid))]
    start = goal
    found = False
    path[start[0]][start[1]] = "*"
    
    while not found:
        x = start[0]
        y = start[1]
        min = expand[x][y]
        direction = 0
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                next = expand[x2][y2]
                if next > 0 and next < min:
                    direction = i
                    start[0] = x2
                    start[1] = y2
                if next == 1:
                    found = True

        path[start[0]][start[1]] = delta_name[direction+2%4]
        
    for i in range(len(path)):
        print path[i]

expand = search()
path(expand, goal)

