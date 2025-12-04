import re

FILENAME = "2024/L14.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

time_limit = 100 # seconds
room_x = 101
room_y = 103

# room_xample = 11
# room_yample = 7

q1 = 0 # up right
q2 = 0 # up left
q3 = 0 # down left
q4 = 0 # down right
for row in INPUT:
    nums = list(map(int,(re.findall(r'-\d+|\d+',row))))
    x = nums[0]
    y = nums[1]
    x_v = nums[2]
    y_v =  nums[3]

    x_mid = int(room_x/2)
    y_mid = int(room_y/2)

    x_stop = (x+x_v*time_limit) % room_x
    if x_stop == x_mid:
        continue
    
    y_stop = (y+y_v*time_limit) % room_y
    if y_stop == y_mid:
        continue

    
    if x_stop > x_mid:
        if y_stop < y_mid:
            q1 += 1
        else:
            q4 += 1
    else:
        if y_stop < y_mid:
            q2 += 1
        else:
            q3 += 1

    print(x_stop,y_stop)
print("Q1:",q1,"Q2:",q2,"Q3:",q3,"Q4:",q4)
print("Safety factor:",q1*q2*q3*q4)