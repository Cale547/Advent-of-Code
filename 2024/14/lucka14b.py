from PIL import Image
import re
import keyboard

FILENAME = "2024/14/L14.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

time_limit = 100 # seconds
room_x = 101
room_y = 103
x_mid = int(room_x/2)
y_mid = int(room_y/2)
# room_xample = 11
# room_yample = 7

robots = []
for row in INPUT:
    nums = list(map(int,(re.findall(r'-\d+|\d+',row))))
    x = nums[0]
    y = nums[1]
    x_v = nums[2]
    y_v =  nums[3]

    robots.append((x,y,x_v,y_v))

for seconds in range(0, 10000):
    q1 = q2 = q3 = q4 = 0
    print(seconds)
    img = Image.new('1',(101,103))
    for rob in robots:
        x_stop = (rob[0]+rob[2]*seconds) % room_x
        y_stop = (rob[1]+rob[3]*seconds) % room_y

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
        safety_score = q1*q2*q3*q4
        #print(safety_score)
        img.putpixel((x_stop,y_stop), 1)
    filename = '2024/14/maps/'+str(safety_score)+'.'+str(seconds)+'.jpg'
    img.save(filename)
