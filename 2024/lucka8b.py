def myCopy(fromList):
    toList = []
    for k,localRow in enumerate(fromList):
        row_copy = []
        for l,localCol in enumerate(localRow):
            row_copy.append(localCol)
        toList.append(row_copy)
    return toList


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


clone_map = myCopy(ant_map)
antinodes = 0
tagged = []
for i in range(len(ant_rows)-1):
    row1 = ant_rows[i]
    col1 = ant_cols[i]
    for j in range(i+1,len(ant_rows)):
        row2 = ant_rows[j]
        col2 = ant_cols[j]
        if ant_map[row1][col1] != ant_map[row2][col2]:
            continue
        row_diff = row1-row2
        col_diff = col1-col2

        match_found = True
        extender = 0
        while match_found:
            match_found = False
            pot_row1 = row1 + row_diff*extender
            pot_col1 = col1 + col_diff*extender
            
            pot_row2 = row2 - row_diff*extender
            pot_col2 = col2 - col_diff*extender

            """ if row1 == 2 and col1 == 5:
                print(antinodes)
                print(pot_row1,row1,pot_col1,col1)
                print(pot_row2,row2,pot_col2,col2) """

            if 0 <= pot_row1 < len(ant_map) and 0 <= pot_col1 < len(ant_map[0]):
                match_found = True
                if str(pot_row1)+str(pot_col1) not in tagged:
                    if clone_map[pot_row1][pot_col1] == '.':clone_map[pot_row1][pot_col1] = '#'
                    #print("Antinode found at[",pot_row1,pot_col1,"] from antennas",row1,col1,"+",row2,col2)
                    antinodes += 1
                tagged.append(str(pot_row1)+str(pot_col1))
            if 0 <= pot_row2 < len(ant_map) and 0 <= pot_col2 < len(ant_map[0]):
                match_found = True
                if str(pot_row2)+str(pot_col2) not in tagged:
                    if clone_map[pot_row2][pot_col2] == '.':clone_map[pot_row2][pot_col2] = '#'
                    #print("Antinode found at[",pot_row2,pot_col2,"] from antennas",row1,col1,"+",row2,col2)
                    antinodes += 1
                tagged.append(str(pot_row2)+str(pot_col2))
            extender += 1

print("Total number of antinodes:",antinodes)
# 1011 is too low


with open("2024/testMap.txt","w",encoding="UTF8") as f:
    for r in clone_map:
        toWrite = ''.join(r)+'\n'
        f.write(toWrite)
print(ant_rows)
print(ant_cols)