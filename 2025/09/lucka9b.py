import time

OUTSIDE_BORDER = 1
BORDER = 2
DOT = 0


start_time = time.time()
FILENAME = "2025/09/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

tile_map = []
my_range = 100000 #100000
for i in range(my_range):
    row = []
    for j in range(my_range):
        row.append(DOT)
    tile_map.append(row)
    if i % 1000 == 0:
        print(i)

red_tiles = []
for i in range(-1,len(INPUT)-1):
    print(i)
    row1 = INPUT[i].strip()
    row2 = INPUT[i+1 ].strip()
    #print(f"{row1} and {row2}")

    coords1 = row1.split(',')
    x1 = int(coords1[0])
    y1 = int(coords1[1])

    coords2 = row2.split(',')
    x2 = int(coords2[0])
    y2 = int(coords2[1])
    red_tiles.append((x2,y2))
    #print(f"x1:{x1},y1:{y1}, x2:{x2},y2:{y2}")


    # Same row
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            tile_map[y][x1] = BORDER
    # Same column
    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            tile_map[y1][x] = BORDER
print("Gjorde en fin slinga")

is_green = []
for i in range(my_range):
    is_green.append(False)

for i,row in enumerate(tile_map):
    for j,col in enumerate(row):
        if is_green[j]:
            tile_map[j][i] = BORDER


# tile_map border is done

print("Filling the tilemap with A")
#approaching from above
stop = [False]*my_range
for i in range(len(tile_map)):
    row = tile_map[i]
    for j in range(len(row)):
        col = row[j]
        if stop[j]:
            continue
        if col == BORDER:
            stop[j] = True
        elif col == DOT:
            tile_map[i][j] = OUTSIDE_BORDER

#approaching from below
stop = [False]*my_range
for i in range(len(tile_map)-1,-1,-1):
    row = tile_map[i]
    for j in range(len(row)):
        col = row[j]
        if stop[j]:
            continue
        if col == BORDER:
            stop[j] = True
        elif col == DOT:
            tile_map[i][j] = OUTSIDE_BORDER

#approaching from the left
stop = [False]*my_range
for j in range(len(tile_map[0])):
    #col = tile_map[0][j]
    for i in range(len(tile_map)):
        row = tile_map[i]
        if stop[i]:
            continue
        if row[j] == BORDER:
            stop[i] = True
        elif row[j] == DOT:
            tile_map[i][j] = OUTSIDE_BORDER

#approaching from the right
stop = [False]*my_range
for j in range(len(tile_map[0])-1, -1,-1):
    #col = tile_map[0][j]
    for i in range(len(tile_map)):
        row = tile_map[i]
        if stop[i]:
            continue
        if row[j] == BORDER:
            stop[i] = True
        elif row[j] == DOT:
            tile_map[i][j] = OUTSIDE_BORDER


# for row in tile_map:
#     print(row)


#print(red_tiles)
max_area = 0
print("Looking for max area")
for i,r1 in enumerate(red_tiles):
    for r2 in red_tiles[i:]:
        # rectangle has corner min(x1,y1), max(x1,y1)
        x1 = r1[0]
        y1 = r1[1]

        x2 = r2[0]
        y2 = r2[1]

        #print(f"Checking legality for r1={x1},{y1} and r2={x2},{y2}")
        legal_area = True
        for i in range(min(x1,x2), max(x1,x2)+1):
            row = tile_map[i]
            for j in range(min(y1,y2), max(y1,y2)+1):
                if tile_map[j][i] == OUTSIDE_BORDER:
            #if row.count(OUTSIDE_BORDER) > 0:
                    #print(f"Failed at i={i}, j={j}")
                    legal_area = False
                    break
            if not legal_area:
                break
        if not legal_area:
            continue


        area = abs(r1[0]-r2[0]+1)*abs(r1[1]-r2[1]+1)
        if area > max_area:
            max_area = area

print(f"Maximum area with two red tiles as corners is {max_area} area units")
print(f"This process took {time.time()-start_time} seconds...")