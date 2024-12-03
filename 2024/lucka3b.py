import re


my_input = ...

hoppas denna pseudonoden funkar😄
operations = re.findall("mul..." och "do()" och "don't()")



mul_sum = 0
do_mul = true
for op in operations:
    if (!do_mul and op == "do()") or (do_mul and op == "don't()")
        do_mul = !do_mul
        continue
    
    
    
    temp = op.split(",")
    num1 = re.findall([0-9]+, temp[0])[0]
    num2 = re.findall([0-9]+, temp[1])[0]
    mul_sum += int(num1)*int(num2)