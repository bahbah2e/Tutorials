# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def get_neighbors(node_in, closed):
    neighbor_nodes = []
    
    closed.append(cost_to_position(node_in))
    cost = node_in[0] + 1
    for i in range(len(delta)):
        neighbor = []

        neighbor.append(cost)
        neighbor.append(node_in[1] + delta[i][0])
        neighbor.append(node_in[2] + delta[i][1])

        position = cost_to_position(neighbor)
        if (contains(closed, position) == 1):
            continue
        
        if (in_map(position) == 0):
            continue

        x = position[1]
        y = position[0]

        if (grid[x][y]== 1):
            continue

        neighbor_nodes.append(neighbor)

    return neighbor_nodes

def in_map(position):
    if (position[0] < 0) or (position[1] < 0):
        return 0
    lenx = len(grid[0])-1
    leny = len(grid)-1

    if (position[0] > lenx) or (position[1] > leny):
        return 0

    return 1

def cost_to_position(cost):
    position = []
    position.append(cost[1])
    position.append(cost[2])
    return position

def contains(list, test_element):
    for i in range(len(list)):
        if (list[i] == test_element):
            return 1
    return 0

def max_cost(list):
    max = 0
    for i in range(len(list)):
        if (list[i][0] > max):
            max = list[i][0]
    return max

def min_cost(list, heuristic):
    min = heuristic
    for i in range(len(list)):
        if (list[i][0] < min):
            min = list[i][0]
    return min

def min_list(list, min):
    mins = []
    for i in range(len(list)):
        if (list[i][0] == min):
            mins.append(list[i])
    return mins

def search():
    closed = []
    heuristic = len(grid) * len(grid[0])
    neighborhood = []
    root = [0, 0, 0]
    neighborhood.append(root)
    max = 0
    found_end = []
    while(max < heuristic):
        if (len(found_end) > 0):
            print found_end[0]
            break

        if (len(neighborhood) == 0):
            print "fail"
            break
        max = max_cost(neighborhood)
        min = min_cost(neighborhood, heuristic)
        mins = min_list(neighborhood, min)
    
        for i in range(len(mins)):
            neighbors = get_neighbors(mins[i], closed)
            neighborhood.remove(mins[i])
            for j in range(len(neighbors)):
                neighbor = neighbors[j]
                position = cost_to_position(neighbor)
                if (position[0] == goal[1] and position[1] == goal[0]):
                    end = []
                    end.append(neighbor[0])
                    end.append(neighbor[2])
                    end.append(neighbor[1])
                    found_end.append(end)
                    break
                if (contains(neighborhood, neighbors[j]) == 0):
                    neighborhood.append(neighbors[j])

search()