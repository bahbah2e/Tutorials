# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    goal_x = goal[0]
    goal_y = goal[1]

    value[goal_x][goal_y] = 0
    print print_value(value)
    return value, policy

def print_value(value):
    for i in range(len(value)):
        print value[i]

def search():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    touched = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    goal_x = goal[0]
    goal_y = goal[1]

    value[goal_x][goal_y] = 0
    touched[goal_x][goal_y] = 1
    for i in range(1000):
        search_from(goal, value, touched)
        touched = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
        touched[goal_x][goal_y] = 1

def been_touched(start, touched):
    return touched[start[0]][start[1]]

def untouched_exist(touched):
    for i in range(len(touched)):
        for j in range(len(touched[i])):
            if (touched[i][j] == 0):
                return True
    return False

def next_untouched(start, value, touched):
    if (untouched_exist(touched) == False):
        return []

    neighbors = map_neighbors(start)
    print "Map neighbors: ", neighbors
    print_value(neighbors)
    for i in range(len(neighbors)):
        neighbor = neighbors[i]
        x = neighbor[0]
        y = neighbor[1]
        if (touched[x][y] == 0):
            print "Found x:", x, "y:", y
            return [x,y]
    neighbors.reverse
    for i in range(len(neighbors)):
        return next_untouched(neighbor, value, touched)

    return []

def test_touched():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    touched = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    touched[0][3] = 1
    touched[0][2] = 1
    print "Checking: ", touched
    found = next_untouched([0,3], value, touched)
    print touched[found[0]][found[1]]

def search_from(start, value, touched):
    if (untouched_exist(touched) == False):
        return

    if (been_touched(start, touched)):
        print "Touched: ", start
        node = next_untouched(start, value, touched)
        print "Next: ", node
        search_from(node, value, touched)
    else:
        print "Touching: ", start
        touch(start, value, touched)    
        search_from(next_untouched(start, value, touched), value, touched)

def touch(node, value, touched):
    print "Finding optimal neighbor of: ", node
    best_destination = find_optimal_neighbor(node, value)
    print "Best destination: ", best_destination
    path_x = best_destination[0] - node[1]
    path_y = best_destination[1] - node[0]
    path = [path_x, path_y]
    print "Happy Path: ", path
    tangent_paths = path_tangents(path)
    print "Sad Path: ", tangent_paths
        
    print "Start Cost: ", path_cost(best_destination, value)
    cost = cost_step + (success_prob * path_cost(best_destination, value))
        
    for i in range(len(tangent_paths)):
        tangent_x = tangent_paths[i][0]
        tangent_y = tangent_paths[i][1]
        tangent_cost = failure_prob * path_cost(tangent_paths[i], value)
        print "Tangent Cost: ", tangent_cost
        cost = cost + tangent_cost
        
    value[node[0]][node[1]] = cost
    touched[node[0]][node[1]] = 1
    print_value(value)
    print_value(touched)
    print ""

def path_cost(path, value):
    path_x = path[0]
    path_y = path[1]
    if (path_x >= 0 and path_y >= 0):
        if (grid[path_x][path_y] == 0):
            return value[path_x][path_y]

    return collision_cost

def path_tangents(path):
    if (path == delta[0] or path==delta[2]):
        return [delta[1], delta[3]]
    return [delta[0], delta[2]]

def find_optimal_neighbor(node_in, value):
    neighbors_all = get_neighbors_valid(node_in, value)
    optimal_position = [-1,-1]
    for i in range(len(neighbors_all)):
        if (i == 0):
            optimal_position = neighbors_all[i]
        else:
            neighbor = neighbors_all[i]
            test = value[neighbor[0]][neighbor[1]]
            optimal = value[optimal_position[0]][optimal_position[1]]
            
            if (test < optimal):
                optimal_position = neighbors_all[i]
    return optimal_position

def get_neighbors_valid(node_in, value):
    neighbor_nodes = []
    
    for i in range(len(delta)):
        neighbor = []

        neighbor.append(node_in[1] + delta[i][0])
        neighbor.append(node_in[0] + delta[i][1])

        x = neighbor[0]
        y = neighbor[1]

        if (in_map(neighbor) == 0):
            print "Neighbor: ", neighbor, " off map"
            continue

        if (value[x][y] == 0):
            print "Neighbor ", neighbor, " is goal"
            continue

        if (grid[x][y]== 1):
            print "Neighbor: ", neighbor, " is wall"
            continue

        print "Valid Neighbor: ", neighbor
        neighbor_nodes.append(neighbor)

    return neighbor_nodes

def map_neighbors(node_in):
    all_neighbors = get_neighbors_all(node_in)
    in_map_neighbors = []

    for i in range(len(all_neighbors)):
        neighbor = all_neighbors[i]
        if (neighbor[0] >= 0 and neighbor[1] >=0) and (neighbor[0] < len(grid[0]) and neighbor[1] < len(grid)):
            in_map_neighbors.append(neighbor)
    return in_map_neighbors

def get_neighbors_all(node_in):
    neighbor_nodes = []
    
    for i in range(len(delta)):
        neighbor = []

        neighbor.append(node_in[0] + delta[i][0])
        neighbor.append(node_in[1] + delta[i][1])

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

search()

