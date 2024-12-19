FILENAME = "2024/18/L18.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

byte_list = []
for byte in INPUT:
    byte = byte.strip().split(',')
    byte_list.append((int(byte[0]),int(byte[1])))


map_width = 71 # exempel = 7 // riktig = 71
map_height = 71
mem_map = []
for i in range(map_height):
    row  = []
    for j in range(map_width):
        row.append('.')
    mem_map.append(row)

init_bytes = 2800
# 3450 is max
for byte in byte_list[:init_bytes]:
    mem_map[byte[0]][byte[1]] = '#'

s_x = s_y = 0

e_x = map_width - 1
e_y = map_height - 1
for byte in byte_list[init_bytes:]:
    path_exists = False
    print(byte[0],byte[1])
    mem_map[byte[0]][byte[1]] = '#'
    queue = [(s_x,s_y,0)]
    visited = [(s_x,s_y)]
    while len(queue) != 0:
        current = queue.pop(0)
        x = current[0]
        y = current[1]
        steps = current[2]
        if (x,y) == (e_x,e_y):
            path_exists = True
            break
        
        if x > 0 and mem_map[x-1][y] != '#' and (x-1,y) not in visited:
            visited.append((x-1,y))
            queue.append((x-1,y,steps+1))
        if x < map_width - 1 and mem_map[x+1][y] != '#' and (x+1,y) not in visited:
            visited.append((x+1,y))
            queue.append((x+1,y,steps+1))
        if y > 0 and mem_map[x][y-1] != '#' and (x,y-1) not in visited:
            visited.append((x,y-1))
            queue.append((x,y-1,steps+1))
        if y < map_height - 1 and mem_map[x][y+1] != '#' and (x,y+1) not in visited:
            visited.append((x,y+1))
            queue.append((x,y+1,steps+1))
    if not path_exists:
        print("Byte with coordinates",byte[0],byte[1],"blocked the exit of!")
        break
    print("Path with",steps,"steps found.")
