colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

def init_position(world, default):
    p = []
    for i in range(len(world)):
        row = []
        for j in range(len(world[i])):
            row.append(default)
        p.append(row)
    return p

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
    q=[]
    for i in range(len(p)):
        q.append(move(p[i], U))
    return q

def move_y(p, U):
    columns = []
    for i in range(len(p[0])):
        c = transpose_column(p, i)
        columns.append(move(c, U))
    for i in range(len(columns)):
        for j in range(len(columns[i])):
            p[j][i] = columns[i][j]
    return p

def transpose_column(p, column):
    row = []
    for i in range(len(p)):
        for j in range(len(p[i])):
            if (j == column):
                row.append(p[i][j])
    return row

def move(p, U):
    q = []
    for i in range(len(p)):
        undershoot = (i-U+1) % len(p)
        exact = (i-U) % len(p)
        s = p_move * p[exact]
        s = s + (1-p_move) * p[undershoot]
        q.append(s)

    return q

def run(colors):
    p = init_position(colors, 1.0)

    for i in range(len(measurements)):
        measurement = measurements[i]
        x = motions[i][1]
        y = motions[i][0]
        
        if (x != 0):
            p = move_x(p, x)
        if (y != 0):
            p = move_y(p, y)
        p = sense(p, colors, measurement)

    return p
    
p = run(colors)

#Your probability array must be printed 
#with the following code.

show(p)