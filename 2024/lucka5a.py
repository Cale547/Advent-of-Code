FILENAME = "2024/L5.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()


rules = []
updates = []
for line in INPUT:
    if "|" in line:
        rules.append(line.strip())
    elif line.strip() != '':
        updates.append(line.strip().split(","))

#print(type(rules))
#print((updates))


answer = 0
for i,u in enumerate(updates):
    update_okay = True
    prev = u[0]
    for current in u[1:]:
        for r in rules:
            if prev in r and current in r:
                if r.index(current) < r.index(prev):
                    print("Wrong order for",prev,current,"in update",i)
                    update_okay = False
                    break
        if not update_okay:
            break
        prev = current
    if update_okay:
        answer += int(u.pop(int(len(u)/2)))
print("Sum of middle page numbers of all correctly-ordered updates:",answer)