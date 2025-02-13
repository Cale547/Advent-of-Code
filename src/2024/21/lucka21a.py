FILENAME = "21/L21.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()


track_map = []
s_x = s_y = e_x = e_y = 0
for y,row in enumerate(INPUT):
    current = []
    for x,col in enumerate(row.strip()):
        if col == 'S':
            s_x = x
            s_y = y
        if col == 'E':
            e_x = x
            e_y = y
        current.append(col)
    track_map.append(current)
for r in track_map:
    print(''.join(r))
map_heigth = len(track_map)
map_width = len(track_map[0])