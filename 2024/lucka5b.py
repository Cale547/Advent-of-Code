FILENAME = "2024/L5.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

def sortList(updates, rules):
    dict_points = {}
    for page in updates:
        dict_points[page] = 0

    for start,prevTemp in enumerate(updates):
        for currentTemp in updates[start+1:]:
            for rTemp in rules:
                if prevTemp in rTemp and currentTemp in rTemp:
                    if rTemp.index(currentTemp) < rTemp.index(prevTemp):
                        dict_points[currentTemp] += 1
                    else:
                        dict_points[prevTemp] += 1
        
    for elem in dict_points:
        if dict_points[elem] == int(len(dict_points)/2): #spottar ut mitten på den sorterade listan
            return int(elem)

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
                    answer += sortList(u,rules)
                    update_okay = False
                    break
        if not update_okay:
            break
        prev = current
print("Sum of middle page numbers of all incorrectly-ordered updates:",answer)




