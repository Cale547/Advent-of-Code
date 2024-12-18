FILENAME = "2024/18/L18ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

byte_list = []
for byte in INPUT:
    byte = byte.strip().split(',')
    byte_list.append((int(byte[0]),int(byte[1])))


map_width = 7 # exempel = 7 // riktig = 71
map_height = 7
mem_map = []
for i in range(map_height):
    row  = []
    for j in range(map_width):
        row.append('.')
    mem_map.append(row)

bytes_to_fall = 12 # exempel = 12 // riktig = 1024
for i in range(bytes_to_fall):
    mem_map[byte_list[i][0]][byte_list[i][1]] = '#'

for r in mem_map:
    print(''.join(r))
#print(byte_list)


s_x = s_y = 0
e_x = map_width - 1
e_y = map_height - 1
queue = [(s_x,s_y)]
visited = [(s_x,s_y)]
while len(queue) != 0:
    current = queue.pop(0)
    x = current[0]
    y = current[1]
    if x > 0 and mem_map[x-1][y] != '#' and (x-1,y) not in visited:
        visited.append((x-1,y))
        queue.append((x-1,y))
        