import time

start = time.time()

FILENAME = "2024/L9ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

temp_map = []
for line in INPUT:
    for s in line.strip():
        temp_map.append(s)

block_map = []
file_index = 0
for i,b in enumerate(temp_map):
    if i % 2 == 0:
        block_map.append((int(temp_map[i]),file_index))
        file_index += 1
    else:
        block_map.append((int(temp_map[i]), -1))
print(block_map)


# files are evens (0, 2, 4, 6)
# spaces are odds (and ends but they'll be stumbling away...)
# block_map example 2333133121414131402
for i in range(len(block_map)-1, 0, -2):
    file_size = block_map[i][1]
    print(i,block_map[i])

frag_map = []
file_index = 0
for i,block in enumerate(block_map):
    if i % 2 == 0:
        for j in range(int(block)):
            frag_map.append(str(file_index))
        file_index += 1
    else:
        frag_map += "."*int(block)

from_index = len(frag_map)-1
to_index = frag_map.index('.')
while from_index > to_index:
    while frag_map[from_index] == '.' and from_index > to_index:
        from_index -= 1
    frag_map[to_index] = frag_map[from_index]
    frag_map[from_index] = '.'
    to_index = frag_map.index('.')

multiplaya = 0
checksum = 0
for n in frag_map:
    if n == '.':
        break
    checksum += int(n)*multiplaya
    multiplaya += 1
print("Final checksum:",checksum)

stop = time.time()
print("This took",stop-start,"seconds to do.")