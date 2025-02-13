def permutate_operations(ops):
    if 0 not in ops:
        return -1
    zero_found = False
    for k in range(len(ops)-1, 0, -1):
        if ops[k] == 1:
            ops[k] = 0
        elif ops[k] == 0:
            ops[k] = 1
            zero_found = True
            break

    if not zero_found and ops[0] == 0:
        ops[0] = 1
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
    factors = numbers[i]
    # number of permutations = 2^(len(factors) - 1)
    # largest potential number is 2^11 = 2048

    # 0 is +
    # 1 is *
    operations = [0]*(len(factors) - 1)
    while operations != -1:
        test_result = factors[0]
        for j,num in enumerate(factors[1:]):
            if operations[j] == 0:
                test_result += num
            else:
                test_result *= num
            
            if test_result > real_result:
                break

        if test_result == real_result:
            print(operations, "worked for", real_result, factors)
            total_calibration_result += real_result
            print("Total result is now", total_calibration_result)
            break
        
        operations = permutate_operations(operations)

print("Final result is",total_calibration_result)