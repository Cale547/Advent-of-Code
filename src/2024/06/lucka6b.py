import time

startTime = time.time()

FILENAME = "2024/L6.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

def myCopy(fromList):
    toList = []
    for i,row in enumerate(fromList):
        row_copy = []
        for j,col in enumerate(row):
            row_copy.append(col)
        toList.append(row_copy)
    return toList




start_map = []
startGuardRow = 0
startGuardCol = 0
for i,row in enumerate(INPUT):
    current_row = []
    for j,col in enumerate(row.strip()):
        if col == '^':
            startGuardRow = i
            startGuardCol = j
        current_row.append(col)
    start_map.append(current_row)

loop_map = 0
# guardRow = 6
# guardCol = 4

for i,row in enumerate(start_map):
    for j,col in enumerate(row):
        lab_map = myCopy(start_map)
        if start_map[i][j] == '.':
            lab_map[i][j] = '#'
        else:
            pass
            #print(i,j,lab_map[i][j])

        guardRow = startGuardRow
        guardCol = startGuardCol
        direction = 0
        is_loop = False
        visit_directions = {}

        while 0 < guardRow < len(lab_map)-1 and 0 < guardCol < len(lab_map[0])-1:
            if direction == 0:
                if lab_map[guardRow-1][guardCol] != '#':
                    if lab_map[guardRow][guardCol] != "X":
                        lab_map[guardRow][guardCol] = "X"
                        visit_directions[str(guardRow)+str(guardCol)] = 0
                    elif visit_directions[str(guardRow)+str(guardCol)] == 0:
                        is_loop = True
                    guardRow -= 1
                else:
                    direction = (direction + 1) % 4

            if direction == 1:
                if lab_map[guardRow][guardCol+1] != '#':
                    if lab_map[guardRow][guardCol] != "X":
                        lab_map[guardRow][guardCol] = "X"
                        visit_directions[str(guardRow)+str(guardCol)] = 1
                    elif visit_directions[str(guardRow)+str(guardCol)] == 1:
                        is_loop = True
                    guardCol += 1
                else:
                    direction = (direction + 1) % 4
            
            if direction == 2:
                if lab_map[guardRow+1][guardCol] != '#':
                    if lab_map[guardRow][guardCol] != "X":
                        lab_map[guardRow][guardCol] = "X"
                        visit_directions[str(guardRow)+str(guardCol)] = 2
                    elif visit_directions[str(guardRow)+str(guardCol)] == 2:
                        is_loop = True
                    guardRow += 1
                else:
                    direction = (direction + 1) % 4
            
            if direction == 3:
                if lab_map[guardRow][guardCol-1] != '#':
                    if lab_map[guardRow][guardCol] != "X":
                        lab_map[guardRow][guardCol] = "X"
                        visit_directions[str(guardRow)+str(guardCol)] = 3
                    elif visit_directions[str(guardRow)+str(guardCol)] == 3:
                        is_loop = True
                    guardCol -= 1
                else:
                    direction = (direction + 1) % 4
            if is_loop:
                loop_map += 1
                break
        lab_map[i][j] = '.'

print("Possible loop maps:",loop_map)

stopTime = time.time()
print("This method took",int(stopTime-startTime),"seconds...")