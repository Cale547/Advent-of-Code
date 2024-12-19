import time

start = time.time()
FILENAME = "2024/19/L19.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

patterns = INPUT[0].strip().split(", ")

wanted_designs = []
for row in INPUT[2:]:
    wanted_designs.append(row.strip())

possible_designs = 0
for i,design in enumerate(wanted_designs):
    print(i)
    starts_with = {}
    for pat in patterns:
        if design.startswith(pat):
            starts_with[pat] = 1
    while len(starts_with) > 0:
        s = list(starts_with.keys())[0]
        starts_with.pop(s)
        if s == design:
            possible_designs += 1
            break
        for pat in patterns:
            if design.startswith(s+pat):# and s+pat not in starts_with:
                if s+pat in starts_with:
                    starts_with[s+pat] += 1
                else:
                    starts_with[s+pat] = 1
print("There are",possible_designs,"possible designs")
print("This took",time.time()-start,"to do")