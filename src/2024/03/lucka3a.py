import re

FILENAME = "2024/L3.txt"
with open(FILENAME, encoding="UTF8") as f:
    temp_input = f.readlines()

my_input = ""
for line in temp_input:
    my_input += line.strip()

operations = re.findall("mul\(\d+,\d+\)", my_input)
print(operations)


mul_result = 0
for op in operations:
    temp = op.split(",")
    num1 = re.findall("\d+",temp[0])[0]
    num2 = re.findall("\d+",temp[1])[0]
    mul_result += int(num1)*int(num2)
print("Result of all mul operations:",mul_result)
