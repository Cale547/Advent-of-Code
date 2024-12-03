import re

FILENAME = "2024/L3ex.txt"
with open(FILENAME, encoding="UTF8") as f:
    temp_input = f.readlines()

my_input = ""
for line in temp_input:
    my_input += line.strip()

operations = re.findall("mul\([0-9]+?,[0-9]+?\)", my_input)
print(operations)


mul_result = 0
for op in operations:
    temp = op.split(",")
    num1 = re.findall("[0-9]+",temp[0])[0]
    num2 = re.findall("[0-9]+",temp[1])[0]
    mul_result += int(num1)*int(num2)
print("Result of all mul operations:",mul_result)
