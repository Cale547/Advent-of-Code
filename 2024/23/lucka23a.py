import time

start = time.time()
FILENAME = "23/L23.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

connections = {}
for con in INPUT:
    c1 = con.strip().split('-')[0]
    c2 = con.strip().split('-')[1]
    if c1 in connections:
        connections[c1].append(c2)
    else:
        connections[c1] = [c2]
    if c2 in connections:
        connections[c2].append(c1)
    else:
        connections[c2] = [c1]
print(connections)

lan_parties = 0
pc_id = list(connections.keys())
for i,pc1 in enumerate(pc_id):
    for j,pc2 in enumerate(pc_id[i:],i):
        for k,pc3 in enumerate(pc_id[j:],j):
            if pc1 in connections[pc2] and pc2 in connections[pc3] and pc3 in connections[pc1]:
                if pc1.startswith('t') or pc2.startswith('t') or pc3.startswith('t'):
                    lan_parties += 1
print("There are",lan_parties,"lan parties where one pc starts with 't'.")
print("This took",time.time()-start,"seconds.")
