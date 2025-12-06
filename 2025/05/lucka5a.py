FILENAME = "2025/05/input.txt"

fresh_id_ranges = []
with open(FILENAME, encoding="UTF8") as f:
    line = f.readline().strip()
    while line.strip() != "":
        start = int(line.split('-')[0])
        stop = int(line.split('-')[1])
        fresh_id_ranges.append((start,stop))
        line = f.readline().strip()
    
    # Merging fresh_id_ranges:
    stuff_left_to_do = True
    next_outer_iteration = True
    while stuff_left_to_do:
        stuff_left_to_do = False
        next_outer_iteration = False
        for i,r1 in enumerate(fresh_id_ranges):
            for j,r2 in enumerate(fresh_id_ranges):
                if i == j:
                    continue

                if r1[0] <= r2[0] and r1[1] >= r2[1]:
                    fresh_id_ranges.remove(r2)
                    next_outer_iteration = True
                    stuff_left_to_do = True
                    break
                if r2[0] <= r1[0] and r2[1] >= r1[1]:
                    fresh_id_ranges.remove(r1)
                    next_outer_iteration = True
                    stuff_left_to_do = True
                    break

                if r1[0] <= r2[0] <= r1[1]: #r1 can be extended to the right by adopting r2's upper limit
                    fresh_id_ranges.remove(r2)
                    fresh_id_ranges[i] = (r1[0],r2[1])
                    next_outer_iteration = True
                    stuff_left_to_do = True
                    break

                if r1[0] <= r2[1] <= r1[1]: #r1 can be extended to the left by adopting r2's lower limit
                    fresh_id_ranges.remove(r2)
                    try:
                        fresh_id_ranges[i] = (r2[0],r1[1])
                    except IndexError:
                        print(f"r1: {r1}, r2: {r2}")
                        print(f"i: {i}, j: {j}")
                    next_outer_iteration = True
                    stuff_left_to_do = True
                    break

            if next_outer_iteration:                
                break

    ingredients = f.readlines()

fresh_count = 0
for ingredient in ingredients:
    ingredient = int(ingredient.strip())
    for range in fresh_id_ranges:
        if range[0] <= ingredient <= range[1]:
            fresh_count += 1
            break
        else:
            pass

print(f"{fresh_count} of the available ingredient IDs are fresh: ")
