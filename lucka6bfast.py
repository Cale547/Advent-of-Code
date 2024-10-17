
import time as t
import numpy as np
start = t.time()
my_input = open("L6.txt")

time = (my_input.readline().split())
time = int("".join(time[1:5]))
dist = my_input.readline().split()
dist = int("".join(dist[1:5]))
print(time)
print(dist)

waysToBeat = 0
for j in range(int(np.floor(time/2))):
    if (j*(time-j) > dist):
        waysToBeat += 2

if (time % 2 != 0):
    k = np.round(time/2)
    if (k*(time-k) > dist):
        waysToBeat += 2

print("Number of ways to beat the record:",waysToBeat)
stop = t.time()

print("This took ", stop-start,"seconds")