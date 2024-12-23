import time

def is_connected(all_pcs: list,connections: dict):
    for i,pc1 in enumerate(all_pcs):
        for pc2 in all_pcs[i+1:]:
            if pc1 not in connections[pc2] or pc2 not in connections[pc1]:
                return False
    return True

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
#for c in connections:
#    print(c,connections[c])

# each computer is connected to 13 other computers
pc_id = list(connections.keys())
largest_network = []
for i,pc_main in enumerate(pc_id):
    for j,pc_sub in enumerate(connections[pc_main]):
        lan_attenders = connections[pc_main].copy()
        lan_attenders.remove(pc_sub)
        #print(connections[pc_main])
        if is_connected(lan_attenders,connections):
            lan_attenders.append(pc_main)
            largest_network = lan_attenders.copy()
            print("I found 13 computers that talk")
            break
    if len(largest_network) > 0:
        break
    # add maximum amount of the pc:s in connections[pc_main]
largest_network.sort()
print("Lan-party alphabetically:",','.join(largest_network))
