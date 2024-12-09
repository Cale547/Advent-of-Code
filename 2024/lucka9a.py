FILENAME = "2024/L9.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

block_map = []
for line in INPUT:
    for s in line.strip():
        block_map.append(s)

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