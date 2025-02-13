import numpy as np

my_input = open("L6.txt")

times = (my_input.readline().split())
times = [int(num) for num in times[1:5]]
dists = my_input.readline().split()
dists = [int(num) for num in dists[1:5]]

waysToBeat = []
for i in range(4):
    newWaysToBeat = 0
    for j in range(int(np.floor(times[i]/2))):
        if (j*(times[i]-j) > dists[i]):
            newWaysToBeat += 2
    
    if (times[i] % 2 != 0):
        k = np.round(times[i]/2)
        if (k*(times[i]-k) > dists[i]):
            print("1 more for i =",i)
            newWaysToBeat += 2

    waysToBeat.append(newWaysToBeat)
print("Number of ways to beat each record:",waysToBeat)
ans = 1
for num in waysToBeat:
    ans *= num
print("Multiply those together and we get:",ans)



"""ANSWER:::
Number of ways to beat each record: [34, 36, 10, 18]
Multiply those together and we get: 220320"""
