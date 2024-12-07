import time

startTime = time.time()

def permutate_operations(ops):
    if 0 not in ops and 1 not in ops:
        #print("All permutations tried")
        return -1
    over_flow = True
    for k in range(len(ops)-1, 0, -1):
        if ops[k] == 2:
            ops[k] = 0
        elif ops[k] == 1:
            ops[k] = 2
            over_flow = False
        elif ops[k] == 0:
            ops[k] = 1
            over_flow = False
            break

    if over_flow:
        if ops[0] == 0:
            ops[0] = 1
        elif ops[0] == 1:
            ops[0] = 2
    return ops


FILENAME = "2024/L7.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

test_values = []
numbers = []
for i,row in enumerate(INPUT):
    temp = row.split(":")
    test_values.append(int(temp[0]))

    new_numbers = []
    for num in temp[1].strip().split():
        new_numbers.append(int(num))
    numbers.append(new_numbers)

total_calibration_result = 0
for i,real_result in enumerate(test_values):
    print(i)
    factors = numbers[i]
    # number of permutations = 3^(len(factors) - 1)
    # largest potential number is 3^11 = 177147...

    # 0 is +
    # 1 is *
    # 2 is ||
    operations = [0]*(len(factors) - 1)
    while operations != -1:
        test_result = factors[0]
        for j,num in enumerate(factors[1:]):
            if operations[j] == 0:
                test_result += num
            elif operations[j] == 1:
                test_result *= num
            else:
                test_result = int(str(test_result) + str(num))

        if test_result == real_result:
            total_calibration_result += real_result
            break
        
        operations = permutate_operations(operations)

print("Final result is",total_calibration_result)
stopTime = time.time()
print("This method took",int(stopTime-startTime),"seconds...")