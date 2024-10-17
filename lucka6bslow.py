
import time as t
start = t.time()
my_input = open("L6.txt")

time = (my_input.readline().split())
time = int("".join(time[1:5]))
dist = my_input.readline().split()
dist = int("".join(dist[1:5]))

waysToBeat = 0
for j in range(time):
    if (j*(time-j) > dist):
        waysToBeat += 1

print("Number of ways to beat the record:",waysToBeat)
stop = t.time()

print("This took ", stop-start,"seconds")