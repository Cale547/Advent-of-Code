FILENAME = "2024/L5ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

def sortList(updates, rules):
    dict_list = [{}]*3
    dict_points = {}
    print(dict_list)
    for page in updates:
        dict_points[page] = 0

    for start,prevTemp in enumerate(updates):
        for currentTemp in updates[start+1:]:
            #print(prevTemp,currentTemp)
            for rTemp in rules:
                if prevTemp in rTemp and currentTemp in rTemp:
                    #print(prevTemp,currentTemp,rTemp)
                    if rTemp.index(currentTemp) < rTemp.index(prevTemp):
                        dict_points[currentTemp] += 1
                    else:
                        dict_points[prevTemp] += 1
        
    print(dict_points)

    new_list = []
    return

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
                    #print("Wrong order for",prev,current,"in update",i)
                    sortList(u,rules)
                    update_okay = False
                    break
        if not update_okay:
            break
        prev = current
    if update_okay:
        answer += int(u.pop(int(len(u)/2)))
print("Sum of middle page numbers of all correctly-ordered updates:",answer)




