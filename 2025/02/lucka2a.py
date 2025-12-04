FILENAME = "src/2025/02/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readline()

invalid_counter = 0
invalid_ids = []

ranges = INPUT.split(',')
for id_range in ranges:
    start = int(id_range.split('-')[0])
    stop = int(id_range.split('-')[1])

    for i in range(start, stop+1):
        current_id = str(i)
        id_length = int(len(current_id))

        if id_length % 2 != 0:
            continue
        #print(int(id_length/2))
        possible_pattern = current_id[0:id_length//2] #Double slash courtesy of Mattias
        if current_id.count(possible_pattern) == 2:
            invalid_counter += 1
            invalid_ids.append(int(current_id))

print(f"There are {invalid_counter} invalid IDs in the specified ranges")
print(f"Sum of all invalid IDs is {sum(invalid_ids)}")