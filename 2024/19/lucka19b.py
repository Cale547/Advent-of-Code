import time

start = time.time()

FILENAME = "2024/19/L19.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

patterns = INPUT[0].strip().split(", ")
wanted_designs = []
for row in INPUT[2:]:
    wanted_designs.append(row.strip())

possible_patterns = {}
for p1 in patterns: # p1 is the thing we try to create
    starts_with = {}
    for p2 in patterns:
        if p1.startswith(p2):
            starts_with[p2] = 1
    while len(starts_with) > 0:
        s = list(starts_with.keys())[0]
        score = starts_with[s]
        starts_with.pop(s)
        if s == p1:
            if p1 in possible_patterns:
                possible_patterns[p1] += score
            else:
                possible_patterns[p1] = score
        for p3 in patterns:
            if p1.startswith(s+p3):
                if s+p3 in starts_with:
                    starts_with[s+p3] += score
                else:
                    starts_with[s+p3] = score


for i,design in enumerate(wanted_designs):
    print(i)
    starts_with = {}
    for p2 in patterns:
        if design.startswith(p2):
            starts_with[p2] = 1
    while len(starts_with) > 0:
        s = list(starts_with.keys())[0]
        score = starts_with[s]
        starts_with.pop(s)
        if s == design:
            if design in possible_patterns:
                possible_patterns[design] += score
            else:
                possible_patterns[design] = score
        for p3 in patterns:
            if design.startswith(s+p3):
                if s+p3 in starts_with:
                    starts_with[s+p3] += score
                else:
                    starts_with[s+p3] = score

number_of_different_ways_you_could_make_each_design = 0
for d in wanted_designs:
    if d in possible_patterns:
        number_of_different_ways_you_could_make_each_design += possible_patterns[d]

print("Number of different ways you could make each design:",number_of_different_ways_you_could_make_each_design)
stop = time.time()
print("This took",stop-start,"seconds.")
