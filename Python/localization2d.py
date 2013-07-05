#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[]

colors_3_3=[['green', 'green', 'green'],
            ['green', 'red', 'red'],
            ['green', 'green', 'green']]

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

test_positions=[[0,   0, 0, 0, 0.5],
                [0,   0, 0, 0, 0],
                [0.5, 0, 0, 0, 0],
                [0,   0, 0, 0, 0]]

expected=[[0.011, 0.0246, 0.06799, 0.044, 0.02464],
          [0.007, 0.01017, 0.08697, 0.07988, 0.00935],
          [0.0074, 0.0089, 0.113, 0.3535, 0.0406],
          [0.009, 0.007, 0.0143, 0.043, 0.036]]
# Moves
# [0, 0] = no move
# [0, 1] = right
# [0,-1] = left
# [1, 0] = down
# [-1,0] = up

def show(p):
    for i in range(len(p)):
        print p[i]

def world_height():
    return len(colors)

def world_width():
    size = 0
    for i in range(len(colors)):
        c = colors[i]
        return len(c)

def world_size(world):
    size = 0
    for i in range(len(world)):
        c = colors[i]
        for j in range(len(c)):
            size = size + 1
    return size

def init_position(world, default):
    p = []
    for i in range(len(world)):
        row = []
        for j in range(len(world[i])):
            row.append(default)
        p.append(row)
    return p

def show_world():
    print colors

def show_location():
    print p

def sense(p, world, Z):
    q=p[:]
    s = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (Z==world[i][j])
            q[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right))
            s = s+ q[i][j]
    if (s > 0):
        q = normalize(q, s)
    return q

def normalize(p, N):
    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] = p[i][j]/N
    return p                

def move_x(p, U):
    print 'move x...'
    q=[]
    for i in range(len(p)):
        q.append(move(p[i], U))
    return q

def move_y(p, U):
    print 'move y...'
    columns = []
    print "rows to transpose %s" % (len(p[0]))
    for i in range(len(p[0])):
        c = transpose_column(p, i)
        columns.append(move(c, U))

    for i in range(len(columns)):
        for j in range(len(columns[i])):
            p[j][i] = columns[i][j]

    return p

def transpose_row(p, row):
    column = []
    for i in range(len(p)):
        if (i == row):
            for j in range(len(p[i])):
                element = []
                element.append(p[i][j])
                column.append(element)
    return column

def transpose_column(p, column):
    print "transpose column %s" % (column)
    row = []
    for i in range(len(p)):
        for j in range(len(p[i])):
            if (j == column):
                print "appending from %s, %s value: %s..." % (i, j, p[i][j])
                row.append(p[i][j])
    return row

def move(p, U):
    q = []
    print 'moving %s...' % (p)
    for i in range(len(p)):
        undershoot = (i-U+1) % len(p)
        exact = (i-U) % len(p)
        s = p_move * p[exact]
        s = s + (1-p_move) * p[undershoot]
        q.append(s)

    return q

def shift(i, distance, max):
    return (i-distance)%max

def run(colors):
    p = init_position(colors, 1.0 / world_size(colors))

    for i in range(len(measurements)):
        print 'step %s...' % (i)
        show(p)
        measurement = measurements[i]
        x = motions[i][1]
        y = motions[i][0]
        
        if (x != 0):
            p = move_x(p, x)
            show(p)
        if (y != 0):
            p = move_y(p, y)            
            show(p)
        print 'sense %s...' % (measurement)
        p = sense(p, colors, measurement)
    print 'localized'
    show(p)
    return p

def test_movement_wrap():
    world = colors_3_3
    p = init_position(world, 1.0/9)
    p = sense(p, world, 'red')
    p = move_x(p, 1)
    p = sense(p, world, 'green')
    print p

def test_movement_wrap_y():
    world = colors_3_3
    p = init_position(world, 1.0/9)
    p = sense(p, world, 'green')
    p = move_y(p, 1)
    p = sense(p, world, 'green')
    p = move_y(p, 1)
    p = sense(p, world, 'red')
    print p

def test_noisy_sensor():
    world = colors_3_3
    p = init_position(world, 1.0/9)
    p = sense(p, world, 'red')
    print p

def test_noisy_sensor_with_movement():
    world = colors_3_3
    p = init_position(world, 1.0/9)
    p = sense(p, world, 'red')
    p = move_x(p, 1)
    p = sense(p, world, 'red')
    print p

def test_noisy_sensor_with_movement_y():
    world = colors_3_3
    p = init_position(world, 1.0/9)
    p = sense(p, world, 'red')
    p = move_y(p, 1)
    print p
    p = sense(p, world, 'green')
    print p

def show_move_x():
    for i in range(len(test_positions)):
        print test_positions[i]
    print 'move'
    x = move_x(test_positions, 1)
    for i in range(len(x)):
        print x[i]

def show_move_y():
    for i in range(len(test_positions)):
        print test_positions[i]
    print 'move'
    x = move_y(test_positions, 1)
    for i in range(len(x)):
        print x[i]

run(colors)