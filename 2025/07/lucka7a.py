FILENAME = "2025/07/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

lazer_map = []
columns_with_lasers = [False]*len(INPUT[0].strip())
for row in INPUT:
    lazer_map.append(list(row.strip()))

split_counter = 0
for i,row in enumerate(lazer_map):
    for j,col in enumerate(row):
        if col == '^' and columns_with_lasers[j]:
            split_counter += 1
            
            # Bounds checking is redundant because no splitter sits on the edge of the map but whatever
            if j < len(row)-1:
                columns_with_lasers[j+1] = True
            if j > 0:
                columns_with_lasers[j-1] = True
            columns_with_lasers[j] = False 
        if col == 'S':
            columns_with_lasers[j] = True
print(f"Total amount of splits is {split_counter}")