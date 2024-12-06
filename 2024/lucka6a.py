FILENAME = "2024/L6.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

lab_map = []
guardRow = 0
guardCol = 0
for i,row in enumerate(INPUT):
    current_row = []
    for j,col in enumerate(row.strip()):
        if col == '^':
            guardRow = i
            guardCol = j
        current_row.append(col)
    lab_map.append(current_row)


direction = 0
visited = 0
while 0 < guardRow < len(lab_map)-1 and 0 < guardCol < len(lab_map[0])-1:
    if direction == 0:
        if lab_map[guardRow-1][guardCol] != '#':
            if lab_map[guardRow][guardCol] != "X":
                lab_map[guardRow][guardCol] = "X"
                visited += 1
            guardRow -= 1
        else:
            direction = (direction + 1) % 4

    if direction == 1:
        if lab_map[guardRow][guardCol+1] != '#':
            if lab_map[guardRow][guardCol] != "X":
                lab_map[guardRow][guardCol] = "X"
                visited += 1
            guardCol += 1
        else:
            direction = (direction + 1) % 4
    
    if direction == 2:
        if lab_map[guardRow+1][guardCol] != '#':
            if lab_map[guardRow][guardCol] != "X":
                lab_map[guardRow][guardCol] = "X"
                visited += 1
            guardRow += 1
        else:
            direction = (direction + 1) % 4
    
    if direction == 3:
        if lab_map[guardRow][guardCol-1] != '#':
            if lab_map[guardRow][guardCol] != "X":
                lab_map[guardRow][guardCol] = "X"
                visited += 1
            guardCol -= 1
        else:
            direction = (direction + 1) % 4
visited += 1 # the one square the guard exited on
for r in lab_map:
    print(r)

print(visited)