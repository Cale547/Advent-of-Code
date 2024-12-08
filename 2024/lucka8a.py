FILENAME = "2024/L8.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

ant_map = []
for i,row in enumerate(INPUT):
    current_row = []
    for j,col in enumerate(row.strip()):
        current_row.append(col)
    ant_map.append(current_row)

ant_rows = []
ant_cols = []
for i,row in enumerate(ant_map):
    for j,current in enumerate(row):
        if current == '.':
            continue

        antenna_type = current
        ant_rows.append(i)
        ant_cols.append(j)


antinodes = 0
pairs = 0
tagged = []
for i in range(len(ant_rows)-1):
    row1 = ant_rows[i]
    col1 = ant_cols[i]
    for j in range(i+1,len(ant_rows)):
        row2 = ant_rows[j]
        col2 = ant_cols[j]
        if ant_map[row1][col1] != ant_map[row2][col2]:
            continue
        pairs+=1
        row_diff = row1-row2
        col_diff = col1-col2

        pot_row1 = row1+row_diff
        pot_col1 = col1+col_diff
        
        pot_row2 = row2-row_diff
        pot_col2 = col2-col_diff

        if 0 <= pot_row1 < len(ant_map) and 0 <= pot_col1 < len(ant_map[0]) and str(pot_row1)+str(pot_col1) not in tagged:
            antinodes += 1
            tagged.append(str(pot_row1)+str(pot_col1))
        if 0 <= pot_row2 < len(ant_map) and 0 <= pot_col2 < len(ant_map[0]) and str(pot_row2)+str(pot_col2) not in tagged:
            antinodes += 1
            tagged.append(str(pot_row2)+str(pot_col2))

print("Total number of antinodes:",antinodes,"from",pairs,"pairs.")