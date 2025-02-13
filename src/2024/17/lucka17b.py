import time
import re

start = time.time()
FILENAME = "17/L17.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

program = list(map(int,(re.findall(r"\d+",INPUT[4]))))
a_start = 0
index = len(program)-1
while index > 0:
    for a in range(a_start,a_start+9):
        b = (a % 8)^1
        c = int(a/pow(2,b))
        b = (b^5)^c
        out = (b%8)
        if out == program[index]:
            print("When a is",str(a)+',',"out is",out)
            a_start = a*8
            index -= 1
            break

a_start = a*8
while True:
    result = []
    a = a_start
    while a != 0:
        b = (a % 8)^1
        c = int(a/pow(2,b))
        b = (b^5)^c
        result.append(b%8)
        a = int(a/8)
    if program == result:
        break
    a_start += 1
print("Programt:",program)
print("Resultat:",result)
print("Lowest A init:",a_start)

stop = time.time()
print("\nThis took",stop-start,"seconds.")