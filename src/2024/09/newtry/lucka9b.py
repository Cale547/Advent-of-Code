import time
start_time = time.time()

FREE = -1
FILENAME = "src/2024/09/L9.txt"
with open(FILENAME) as f:
    original_disk = f.readline().strip()

disk = []
index = 0
for i, size in enumerate(original_disk):
    size = int(size)
    if i % 2 == 0:
        disk.extend([index]*size)
        index += 1
    else:
        disk.extend([FREE]*size)
#print(disk)

index = len(disk)-1
file_ID = -1
for i in range(index,0,-1):
    if disk[i] == FREE or disk[i] == file_ID:
        continue
    file_stop = i
    while disk[i] == disk[file_stop]:
        i -= 1 # Dangerous to alter index inside loop that depends on it but it is the same direction so idk good to have this note here iallafall
    i += 1
    file_start = i
    file_size = file_stop - file_start + 1
    file_ID = disk[file_start]

    start_index = 0
    swapped = False
    while not swapped:
        free_start = disk.index(-1, start_index)
        if free_start >= file_start:
            break # No more possible moves

        free_size = 1
        for j in range(free_start+1, file_start+1): # Changing the start index from 0 to the first occurrence of -1 greatly improved performance.
            if free_size == file_size:
                free_stop = j-1
                for k in range(free_start,free_stop+1):
                    disk[k] = file_ID
                for k in range(file_start,file_stop+1):
                    disk[k] = FREE
                #print(disk)
                swapped = True
                break

            if disk[j] == FREE:
                free_size += 1
                continue

            if disk[j] != FREE:
                start_index = j
                break


        if j >= file_start: # Not adding this added about 25 seconds of backtracking through all the files that had already been moved.
            break  # Being 25 seconds of checking whether each one of those blocks were free or not.

checksum = 0
for index, file in enumerate(disk):
    if file == FREE:
        continue
    checksum += file*index
print(f"Final checksum is {checksum}.")
print(f"Completed in {round(time.time()-start_time)} seconds")