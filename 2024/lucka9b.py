import time

startTime = time.time()

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

#print(''.join(frag_map))

tagged = []
from_index = len(frag_map)-1
while from_index > 0:
    frag_str = ''.join(frag_map)
    if frag_map[from_index] == '.':
        from_index -= 1
        continue
    if frag_map[from_index] in tagged:
        from_index -= frag_map.count(frag_map[from_index])
        continue

    file_to_move = frag_map[from_index]
    print(file_to_move)
    file_size = frag_map.count(file_to_move)

    try:
        insertion_index = frag_str.index('.'*file_size)
    except ValueError:
        from_index -= file_size
        continue
    
    if insertion_index > from_index:
        from_index -= file_size
        continue

    frag_map[insertion_index:insertion_index+file_size] = file_to_move
    frag_map[from_index-file_size+1:from_index+1] = '.'
    tagged.append(file_to_move)
    from_index -= file_size

multiplaya = 0
checksum = 0
for n in frag_map:
    if n == '.':
        multiplaya += 1
        continue
    checksum += int(n)*multiplaya
    multiplaya += 1
print("Final checksum:",checksum)
#print("De-fragmented drive:",''.join(frag_map))
stopTime = time.time()
print("This method took",int(stopTime-startTime),"seconds...")
# 125660055 too low jag orkar inte
# 3208331195935 also too low men går i alla fall fortare att komma fram till detta felaktiga svaret AAAAAAAAAAAAAAAAAAA