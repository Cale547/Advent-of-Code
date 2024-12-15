import keyboard

def go_up(row, col):
    global rob_row
    global rob_col

    is_box = ware_map[row][col] == '[' # moving functions will always be called on the left half of the box
    if row == 1 or ware_map[row-1][col] == '#' or (is_box and ware_map[row-1][col+1] == '#'):
        return

    if is_box:
        if ware_map[row-1][col] == '[':
            go_up(row-1, col)

        elif ware_map[row-1][col] == ']' and ware_map[row-1][col+1] == '.':
            go_up(row-1, col-1)

        elif ware_map[row-1][col] == '.' and ware_map[row-1][col+1] == '[':
            go_up(row-1, col+1)

        elif ware_map[row-1][col] == ']' and ware_map[row-1][col+1] == '[': # moving double boxes
            above_two_boxes = [ware_map[row-2][col-1], ware_map[row-2][col], ware_map[row-2][col+1], ware_map[row-2][col+2]]
            if '#' in above_two_boxes:
                return
            go_up(row-1, col-1)
            go_up(row-1, col+1)

        if ware_map[row-1][col] == '.' and ware_map[row-1][col+1] == '.':
            ware_map[row-1][col],ware_map[row][col] = ware_map[row][col], ware_map[row-1][col] # swaps the content of box' left half
            ware_map[row-1][col+1],ware_map[row][col+1] = ware_map[row][col+1], ware_map[row-1][col+1] # swaps the content of box' right half

    else: # is robot
        if ware_map[row-1][col] == '[':
            go_up(row-1, col)
        elif ware_map[row-1][col] == ']':
            go_up(row-1, col-1)
        if ware_map[row-1][col] == '.':
            ware_map[row-1][col],ware_map[row][col] = ware_map[row][col], ware_map[row-1][col] # swaps the content
            rob_row -= 1

def go_right(row, col):
    global rob_row
    global rob_col

    is_box = ware_map[row][col] == '[' # moving functions will always be called on the left half of the box
    if is_box and (col == len(ware_map[0])-3 or ware_map[row][col+2] == '#'):
            return

    if not is_box and (col == len(ware_map[0])-2 or ware_map[row][col+1] == '#'):
        return
    
    if is_box:
        if ware_map[row][col+2] == '[':
            go_right(row, col+2)

        if ware_map[row][col+2] == '.':
            ware_map[row][col+2],ware_map[row][col+1] = ware_map[row][col+1], ware_map[row][col+2] # swaps the content of box' right half
            ware_map[row][col+1],ware_map[row][col] = ware_map[row][col], ware_map[row][col+1] # swaps the content of box' left half
    
    else: # is robot
        if ware_map[row][col+1] == '[':
                go_right(row, col+1)

        if ware_map[row][col+1] == '.':
            ware_map[row][col+1],ware_map[row][col] = ware_map[row][col], ware_map[row][col+1] # swaps the content
            rob_col += 1

def go_down(row, col):
    global rob_row
    global rob_col

    is_box = ware_map[row][col] == '[' # moving functions will always be called on the left half of the box
    if row == len(ware_map)-2 or ware_map[row+1][col] == '#' or (is_box and ware_map[row+1][col+1] == '#'):
        return

    if is_box:
        if ware_map[row+1][col] == '[':
            go_down(row+1, col)

        elif ware_map[row+1][col] == ']' and ware_map[row+1][col+1] == '.':
            go_down(row+1, col-1)

        elif ware_map[row+1][col] == '.' and ware_map[row+1][col+1] == '[':
            go_down(row+1, col+1)

        elif ware_map[row+1][col] == ']' and ware_map[row+1][col+1] == '[': # moving double boxes
            below_two_boxes = [ware_map[row+2][col-1], ware_map[row+2][col], ware_map[row+2][col+1], ware_map[row+2][col+2]]
            if '#' in below_two_boxes:
                return
            go_down(row+1, col-1)
            go_down(row+1, col+1)

        if ware_map[row+1][col] == '.' and ware_map[row+1][col+1] == '.':
            ware_map[row+1][col],ware_map[row][col] = ware_map[row][col], ware_map[row+1][col] # swaps the content
            ware_map[row+1][col+1],ware_map[row][col+1] = ware_map[row][col+1], ware_map[row+1][col+1] # swaps the content
    else: # is robot
        if ware_map[row+1][col] == '[':
            go_down(row+1, col)
        elif ware_map[row+1][col] == ']':
            go_down(row+1, col-1)
        if ware_map[row+1][col] == '.':
            ware_map[row+1][col],ware_map[row][col] = ware_map[row][col], ware_map[row+1][col] # swaps the content of left
            rob_row += 1

def go_left(row, col):
    global rob_row
    global rob_col

    is_box = ware_map[row][col] == '[' # moving functions will always be called on the left half of the box
    if col == 1 or ware_map[row][col-1] == '#':
        return

    if ware_map[row][col-1] == ']':
        go_left(row, col-2)

    if ware_map[row][col-1] == '.':
        if is_box:
            ware_map[row][col-1],ware_map[row][col] = ware_map[row][col], ware_map[row][col-1] # swaps the content of box' left half
            ware_map[row][col],ware_map[row][col+1] = ware_map[row][col+1], ware_map[row][col] # swaps the content of box' right half
        else:
            ware_map[row][col-1],ware_map[row][col] = ware_map[row][col], ware_map[row][col-1] # swaps the content
            rob_col -= 1

# wall = '#'
# box = 'O' (big O)
# robot = '@'
FILENAME = "15/L15.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

ware_map = []
instructions = []
rob_row = 0
rob_col = 0
map_stop = 0
for i,row in enumerate(INPUT):
    if row == '\n':
        map_stop = i
        break
    current_row = []
    for j,col in enumerate(row.strip()):
        match col:
            case '@':
                current_row.append('@')
                current_row.append('.')
            case '#':
                current_row.append('#')
                current_row.append('#')
            case 'O':
                current_row.append('[')
                current_row.append(']')
            case '.':
                current_row.append('.')
                current_row.append('.')
    ware_map.append(current_row)

for i,row in enumerate(ware_map):
    for j,col in enumerate(row):
        if col == '@':
            rob_row = i
            rob_col = j

for i,row in enumerate(INPUT[map_stop:]):
    for j,col in enumerate(row.strip()):
        instructions.append(col)

print("Start state:")
for r in ware_map:
    print(''.join(r))

# Normal iteration
for i,op in enumerate(instructions):
    match op:
        case '^':
            go_up(rob_row, rob_col)
        case '>':
            go_right(rob_row, rob_col)
        case 'v':
            go_down(rob_row, rob_col)
        case '<':
            go_left(rob_row, rob_col)

# Iterate through instructions with space
""" i = 0
while i < len(instructions):
    if keyboard.is_pressed('space'):
        op = instructions[i]

        #for i,op in enumerate(instructions):
        match op:
            case '^':
                go_up(rob_row, rob_col)
            case '>':
                go_right(rob_row, rob_col)
            case 'v':
                go_down(rob_row, rob_col)
            case '<':
                go_left(rob_row, rob_col)
        print("Move",str(i), '('+op+') :')
        for r in ware_map:
            print(''.join(r))
        i += 1
        while keyboard.is_pressed('space'):
            pass """

# Control the robot with keyboard
"""i = 0
while True:
    op = ''
    if keyboard.is_pressed('up'):
        op = '^'
        go_up(rob_row,rob_col)
        while keyboard.is_pressed('up'):
            pass
    elif keyboard.is_pressed('right'):
        op = '>'
        go_right(rob_row,rob_col)
        while keyboard.is_pressed('right'):
            pass
    elif keyboard.is_pressed('down'):
        op = 'v'
        go_down(rob_row,rob_col)
        while keyboard.is_pressed('down'):
            pass
    elif keyboard.is_pressed('left'):
        op = '<'
        go_left(rob_row,rob_col)
        while keyboard.is_pressed('left'):
            pass
    if op != '':
        print("Move",str(i), '('+op+') :')
        for r in ware_map:
            print(''.join(r))
        i += 1
"""

""" GPS_sum = 0
for i,row in enumerate(ware_map[1:len(ware_map)-1], 1):
    for j,col in enumerate(row[1:len(ware_map[0])-1],1):
        if col == '[':
            GPS_sum += 100*i+j """


GPS_sum = 0
for i,row in enumerate(ware_map):
    for j,col in enumerate(row):
        if col == '[':
            GPS_sum += 100*i+j
print()
print("End state:")
for r in ware_map:
    print(''.join(r))
print("Sum of all boxes' GPS coordinates:",GPS_sum)
# 1574861 is too low
# 606 boxes in the end and at the start
print(len(instructions))