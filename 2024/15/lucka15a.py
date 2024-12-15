def go_up(row, col):
    global rob_row
    global rob_col

    if row == 1 or ware_map[row-1][col] == '#':
        return
    
    if ware_map[row-1][col] == 'O':
        go_up(row-1, col)

    if ware_map[row-1][col] == '.':
        ware_map[row-1][col],ware_map[row][col] = ware_map[row][col], ware_map[row-1][col] # swaps the content
        if row == rob_row and col == rob_col:
            rob_row -= 1

def go_right(row, col):
    global rob_row
    global rob_col

    if col == len(ware_map[0])-2 or ware_map[row][col+1] == '#':
        return
    
    if ware_map[row][col+1] == 'O':
        go_right(row, col+1)

    if ware_map[row][col+1] == '.':
        ware_map[row][col+1],ware_map[row][col] = ware_map[row][col], ware_map[row][col+1] # swaps the content
        if row == rob_row and col == rob_col:
            rob_col += 1

def go_down(row, col):
    global rob_row
    global rob_col

    if row == len(ware_map)-2 or ware_map[row+1][col] == '#':
        return
    
    if ware_map[row+1][col] == 'O':
        go_down(row+1, col)

    if ware_map[row+1][col] == '.':
        ware_map[row+1][col],ware_map[row][col] = ware_map[row][col], ware_map[row+1][col] # swaps the content
        if row == rob_row and col == rob_col:
            rob_row += 1

def go_left(row, col):
    global rob_row
    global rob_col

    if col == 1 or ware_map[row][col-1] == '#':
        return
    
    if ware_map[row][col-1] == 'O':
        go_left(row, col-1)

    if ware_map[row][col-1] == '.':
        ware_map[row][col-1],ware_map[row][col] = ware_map[row][col], ware_map[row][col-1] # swaps the content
        if row == rob_row and col == rob_col:
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
        if col == '@':
            rob_row = i
            rob_col = j
        current_row.append(col)
    ware_map.append(current_row)


for i,row in enumerate(INPUT[map_stop:]):
    for j,col in enumerate(row.strip()):
        instructions.append(col)


print("Start state:")
for r in ware_map:
    print(''.join(r))

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
    #print("Move",str(i), '('+op+') :')
    #for r in ware_map:
    #    print(''.join(r))

GPS_sum = 0
for i,row in enumerate(ware_map[1:], 1):
    for j,col in enumerate(row[1:],1):
        if col == 'O':
            GPS_sum += 100*i+j

print()
print("End state:")
for r in ware_map:
    print(''.join(r))
print("Sum of all boxes' GPS coordinates:",GPS_sum)