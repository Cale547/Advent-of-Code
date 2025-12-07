FILENAME = "2025/07/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

lazer_map = []
columns_with_lasers = [0]*len(INPUT[0].strip())
for row in INPUT:
    lazer_map.append(list(row.strip()))

for i,row in enumerate(lazer_map):
    for j,col in enumerate(row):
        if col == '^' and columns_with_lasers[j]:
            # Bounds checking is redundant because no splitter sits on the edge of the map but whatever
            if j < len(row)-1:
                columns_with_lasers[j+1] += columns_with_lasers[j]
            if j > 0:
                columns_with_lasers[j-1] += columns_with_lasers[j]
            columns_with_lasers[j] = 0
        if col == 'S':
            columns_with_lasers[j] = True

print(f"Total amount of timelines is {sum(columns_with_lasers)}")
