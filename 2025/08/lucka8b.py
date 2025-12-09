import math as Math
import time

start_time = time.time()

FILENAME = "2025/08/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

class JunctionBox:
    i:int
    x:int
    y:int
    z:int
    distances:dict #(boxId:int,dist:long)

    def __init__(self, i, x, y, z):
        self.i = int(i)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.distances = dict()

    def __str__(self):
        return f"[id={self.i}, coords={self.x},{self.y},{self.z}]"
    def __repr__(self):
        return f"[id={self.i}, coords={self.x},{self.y},{self.z}]"

all_boxes = []
for i,row in enumerate(INPUT):
    row = row.strip()
    coords = row.split(',')
    box = JunctionBox(i=i,x=coords[0],y=coords[1],z=coords[2])
    all_boxes.append(box)

for j,box1 in enumerate(all_boxes):
    for box2 in all_boxes[j:]:
        if box1.i == box2.i:
            continue
        dist = Math.sqrt(Math.pow(box2.x-box1.x,2) + Math.pow(box2.y-box1.y,2) + Math.pow(box2.z-box1.z,2))
        box1.distances[dist] = box2
        box2.distances[dist] = box1
        # I have ensured that all distances will be unique in both example and input

circuits = []
lastx_1 = 0
lastx_2 = 0
while True:
    min_dist = -1
    min_box1 = None
    min_box2 = None

    for box in all_boxes:
        try:
            local_min = min(box.distances)
        except ValueError:
            # Antar att det beror på att box.distances är tom
            # vilket innebär att boxen redan kopplats till alla andra
            # boxar
            all_boxes.remove(box)
            continue

        if local_min < min_dist or min_dist == -1:
            min_dist = local_min
            min_box1 = box
            min_box2 = box.distances[local_min]
    if min_box1 == None or min_box2 == None:
        break
    
    min_box1.distances.pop(min_dist)
    min_box2.distances.pop(min_dist)

    box1 = min_box1
    box2 = min_box2

    box1_is_in = -1
    box2_is_in = -1
    for i,c in enumerate(circuits):
        if box1.i in c:
            box1_is_in = i
        if box2.i in c:
            box2_is_in = i

    # No box had a prior connection to a circuit
    if box1_is_in == box2_is_in == -1:
        circuits.append([box1.i,box2.i])

    # Boxes are already connected to the same circuit
    elif box1_is_in == box2_is_in:
        pass
    
    # We know that both boxes can't be -1, so if one is, it can be added to the other box's circuit
    elif box1_is_in == -1:
        circuits[box2_is_in].append(box1.i)
    elif box2_is_in == -1:
        circuits[box1_is_in].append(box2.i)
    
    # In the final case, the boxes are each connected to a different circuit
    elif box1_is_in != box2_is_in:
        circuits[box1_is_in].extend(circuits[box2_is_in])
        circuits.remove(circuits[box2_is_in])
    
    #print([len(c) for c in circuits])
    if len(circuits) > 0 and len(circuits[0]) == len(INPUT):
        lastx_1 = box1.x
        lastx_2 = box2.x
        break

print(f"The product of the X-coordinates of the last junction boxes to be connected is {lastx_1*lastx_2}")
print(f"This process took {time.time()-start_time} seconds to perform...")