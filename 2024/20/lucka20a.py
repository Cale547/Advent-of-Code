FILENAME = "20/L20.txt"
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


queue = [(s_x,s_y,0)]
visited = {(s_x,s_y):0}
while len(queue) != 0:
    current = queue.pop(0)
    x = current[0]
    y = current[1]
    steps = current[2]

    if (x,y) == (e_x,e_y):
        break
    
    if x > 0 and track_map[y][x-1] != '#' and (x-1,y) not in visited:
        visited[(x-1,y)] = steps+1
        queue.append((x-1,y,steps+1))
    if x < map_width - 1 and track_map[y][x+1] != '#' and (x+1,y) not in visited:
        visited[(x+1,y)] = steps+1
        queue.append((x+1,y,steps+1))
    if y > 0 and track_map[y-1][x] != '#' and (x,y-1) not in visited:
        visited[(x,y-1)] = steps+1
        queue.append((x,y-1,steps+1))
    if y < map_heigth - 1 and track_map[y+1][x] != '#' and (x,y+1) not in visited:
        visited[(x,y+1)] = steps+1
        queue.append((x,y+1,steps+1))
# visited is now filled with the steps taken so far at (x,y)

# time saved = visited[(cheat_end_x, cheat_end_y)] - visited[(cheat_start_x, cheat_start_y)] - 2
time_saves = {}
for spot in visited:
    x = spot[0] #cheat_start
    y = spot[1]
    if (x+2,y) in visited and visited[(x,y)]+2 < visited[(x+2,y)]:
        saved = visited[(x+2, y)] - visited[(x, y)] - 2
        if saved in time_saves:
            time_saves[saved] += 1
        else:
            time_saves[saved] = 1
    if (x-2,y) in visited and visited[(x,y)]+2 < visited[(x-2,y)]:
        saved = visited[(x-2, y)] - visited[(x, y)] - 2
        if saved in time_saves:
            time_saves[saved] += 1
        else:
            time_saves[saved] = 1
    if (x,y+2) in visited and visited[(x,y)]+2 < visited[(x,y+2)]:
        saved = visited[(x, y+2)] - visited[(x, y)] - 2
        if saved in time_saves:
            time_saves[saved] += 1
        else:
            time_saves[saved] = 1
    if (x,y-2) in visited and visited[(x,y)]+2 < visited[(x,y-2)]:
        saved = visited[(x, y-2)] - visited[(x, y)] - 2
        if saved in time_saves:
            time_saves[saved] += 1
        else:
            time_saves[saved] = 1

good_cheats = 0
keys = list(time_saves.keys())
keys.sort()
for k in keys:
    if k < 100:
        continue
    good_cheats += time_saves[k]
print("There are",good_cheats,"cheats that save at least 100 picoseconds.")