import time
start = time.time()

FREE = -1
FILENAME = "src/2024/09/L9.txt"
with open(FILENAME) as f:
    original_disk = f.readline().strip()
#print(original_disk)

disk = []
index = 0
for i, size in enumerate(original_disk):
    size = int(size)
    if i % 2 == 0:
        disk.extend([index]*size)
        index += 1
    else:
        disk.extend([FREE]*size)

index = len(disk)-1
for i in range(index,0,-1):
    if disk[i] == FREE:
        continue
 # i is at rightmost file
    j = disk.index(-1)
    if j > i:
        break
    disk[i],disk[j] = disk[j],disk[i]

    # I just rewrote this stuff without loop cause it was unnecessary LOL
    # for j in range(disk.index(-1),i+1): # Changing the start index from 0 to the first occurrence of -1 greatly improved performance.
    #     if disk[j] != FREE:
    #         continue
    #     # j is at rightmost free block
    #     disk[i],disk[j] = disk[j],disk[i]
    #     break
    # if i == j: # Not adding this added about 25 seconds of backtracking through all the files that had already been moved.
    #     break  # Being 25 seconds of checking whether each one of those blocks were free or not.

checksum = 0
for index, file in enumerate(disk):
    if file == FREE:
        break
    checksum += file*index
print(f"Final checksum is {checksum}.")
print(f"Completed in {round(time.time()-start)} seconds")