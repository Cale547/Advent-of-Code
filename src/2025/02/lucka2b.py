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

        divisors = []
        for j in range(2, id_length+1):
            if id_length % j == 0:
                divisors.append(j)
        
        if len(divisors) == 0:
            continue

        for divisor in divisors:
            possible_pattern = current_id[0: int(id_length/divisor)]

            if current_id.count(possible_pattern) == divisor:
                invalid_counter += 1
                invalid_ids.append(int(current_id))
                break

print(f"There are {invalid_counter} invalid IDs in the specified ranges")
print(f"Sum of all invalid IDs is {sum(invalid_ids)}")
print(invalid_ids)