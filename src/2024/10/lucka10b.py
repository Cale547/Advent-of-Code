def number_of_trails(a_map, a_row, a_col):
    current = int(a_map[a_row][a_col])
    if current == 9:
        return 1
    #print(a_row,a_col,current,counter)
    counter = 0
    if 0 < a_row < len(a_map) and int(a_map[a_row-1][a_col]) == current+1:
        #print("Go up")
        counter += number_of_trails(a_map, a_row-1, a_col)
    if 0 <= a_col < len(a_map)-1 and int(a_map[a_row][a_col+1]) == current+1:
        #print("Go right")
        counter += number_of_trails(a_map, a_row, a_col+1)
    if 0 <= a_row < len(a_map)-1 and int(a_map[a_row+1][a_col]) == current+1:
        #print("Go down")
        counter += number_of_trails(a_map, a_row+1, a_col)
    if 0 < a_col < len(a_map) and int(a_map[a_row][a_col-1]) == current+1:
        #print("Go left")
        counter += number_of_trails(a_map, a_row, a_col-1)
    #print("counter is",counter)

    return counter



FILENAME = "2024/L10ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

top_map = []
for i,row in enumerate(INPUT):
    current_row = []
    for j,col in enumerate(row.strip()):
        current_row.append(col)
    top_map.append(current_row)

trail_score_sum = 0
for i,row in enumerate(top_map):
    for j,col in enumerate(row):
        if col == '0':
            trail_score_sum += number_of_trails(top_map, i, j)

print("Total number of trails:",trail_score_sum)