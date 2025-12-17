FILENAME = "2025/11/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

connections = {}
for row in INPUT:
    row = row.strip().split(':')
    device = row[0]
    outputs = row[1].split(' ')
    outputs.remove('')
    connections[device] = outputs
#for elem in connections:
#    print(f"{elem} : {connections[elem]}")

visited = {"you":1}
visited_list = list(visited)

index = 0
while True:
    device = visited_list[index]
    if device == "out":
        break
    
    outputs = connections[device]
    for output in outputs:
        if output in visited:
            #print(f"{device} adds {visited[device]} to {output}")
            visited[output] += visited[device]
        else:
            #print(f"{device} creates {output} with value {visited[device]}")
            visited[output] = visited[device]
    
    visited_list = list(visited)
    index += 1

print(visited)