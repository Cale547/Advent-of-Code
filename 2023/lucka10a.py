import math

pipes = ['|','-','L','J','7','F']
def find_neighbor(row,col, exclude):
    # neighborN should be '|' or '7' or 'F'
    # neighborE should be '-' or '7' or 'J'
    # neighborW should be '-' or 'L' or 'F'
    # neighborS should be '|' or 'L' or 'J'

    # if INPUT[row][col] in goNorth = ['|','L','J'], we can go North
    # if INPUT[row][col] in goWest = ['-','7','J'], we can go West
    # if INPUT[row][col] in goEast = ['-','L','F'], we can go East
    # if INPUT[row][col] in goSouth = ['|','7','F'], we can go South
    go_north = ['|','L','J','S']
    go_west = ['-','7','J','S']
    go_east = ['-','L','F','S']
    go_south = ['|','7','F','S']

    currentpipe_local = INPUT[row][col]

    neighbors = []
    if currentpipe_local in go_north  and INPUT[row-1][col] in ['|','7','F','S']:
        neighbors.append('N')
    if currentpipe_local in go_east and INPUT[row][col+1] in ['-','7','J','S']:
        neighbors.append('E')
    if currentpipe_local in go_west and INPUT[row][col-1] in ['-','L','F','S']:
        neighbors.append('W')
    if currentpipe_local in go_south and INPUT[row+1][col] in ['|','L','J','S']:
        neighbors.append('S')



    #print("Before exclusion, we have",neighbors)
    if exclude in neighbors:
        neighbors.remove(exclude)
    return neighbors[0]


INPUT = open("L10.txt").readlines()                   ##################################START###############################
for i,line in enumerate(INPUT):
    INPUT[i] = line.strip()

S_ROW = 0
S_COL = 0
for i,ROW in enumerate(INPUT):
    for j,CHAR in enumerate(ROW):
        if CHAR == 'S':
            print("S_ROW =",i)
            S_ROW = i
            print("S_COL =",j)
            S_COL = j
            break
    if S_ROW != 0:
        break

currentPipe = INPUT[S_ROW][S_COL]
C_ROW = S_ROW
C_COL = S_COL
STEP_COUNT = 0
LAST_NEIGHBOR = 'W'
print(currentPipe)
while True:
    nextNeighbor = find_neighbor(C_ROW, C_COL, LAST_NEIGHBOR)
    match nextNeighbor:
        case 'N':
            C_ROW -= 1
            LAST_NEIGHBOR = 'S'
        case 'E':
            C_COL += 1
            LAST_NEIGHBOR = 'W'
        case 'W':
            C_COL -= 1
            LAST_NEIGHBOR = 'E'
        case 'S':
            C_ROW += 1
            LAST_NEIGHBOR = 'N'
    currentPipe = INPUT[C_ROW][C_COL]

    STEP_COUNT += 1
    if currentPipe == 'S':
        break


print("Final step-count is",STEP_COUNT)
print("Furthest tile is half those steps, resulting in",math.floor(STEP_COUNT/2))
