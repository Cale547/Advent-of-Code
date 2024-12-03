import re

FILENAME = "2024/L3.txt"
with open(FILENAME, encoding="UTF8") as f:
    temp_input = f.readlines()

#temp_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

my_input = ""
for line in temp_input:
    my_input += line.strip()
print(my_input)


#hoppas denna pseudonoden funkar😄
operations = re.findall("mul\([0-9]+?,[0-9]+?\)|do\(\)|don't\(\)", my_input)
#operations = re.findall("mul\([0-9]+?,[0-9]+?\)", my_input)
print(operations)


mul_result = 0
do_mul = True
for op in operations:
    if op == "do()":
        do_mul = True 
        continue
    if op == "don't()":
        do_mul = False
        continue
    
    
    if do_mul:
        temp = op.split(",")
        num1 = re.findall("[0-9]+", temp[0])[0]
        num2 = re.findall("[0-9]+", temp[1])[0]
        mul_result += int(num1)*int(num2)
print("Result of all mul operations:",mul_result)