FILENAME = "2025/09/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

red_tiles = []
for row in INPUT:
    row = row.strip()
    x = int(row.split(',')[0])
    y = int(row.split(',')[1])
    red_tiles.append((x,y))

max_area = 0
for i,r1 in enumerate(red_tiles):
    for r2 in red_tiles[i:]:
        area = abs(r1[0]-r2[0]+1)*abs(r1[1]-r2[1]+1)
        if area > max_area:
            max_area = area

print(f"Maximum area with two red tiles as corners is {max_area} area units")
