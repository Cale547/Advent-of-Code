FILENAME = "2025/04/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

accessible_rolls = 0

roll_map = []
for row in INPUT:
    roll_map.append(row)

for i,row in enumerate(roll_map):
    for j,col in enumerate(row):
        if roll_map[i][j] != '@':
            continue

        adjacent_rolls = 0
        for i2 in range(-1,2):
            for j2 in range(-1,2):
                if i2 == 0 and j2 == 0:
                    continue
                if 0 <= i+i2 <= (len(roll_map)-1) and 0 <= j+j2 <= (len(row)-1):
                    if roll_map[i+i2][j+j2] == '@':
                        adjacent_rolls += 1
        if adjacent_rolls < 4:
            accessible_rolls += 1
print(f"There are {accessible_rolls} accessible paper rolls")