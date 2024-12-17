import re
import time
import keyboard

def lit_to_combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            return "no"

# The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
# The denominator is found by raising 2 to the power of the instruction's combo operand.
# The result of the division operation is truncated to an integer and then written to the A register.
def adv(operand):
    global a
    operand = lit_to_combo(operand)
    a = int(a/pow(2,operand))
    return a

# The bdv instruction (opcode 6) works exactly like the adv instruction
# except that the result is stored in the B register. (The numerator is still read from the A register.)
def bdv(operand):
    global a; global b
    operand = lit_to_combo(operand)
    b = int(a/pow(2,operand))
    return b

# The cdv instruction (opcode 7) works exactly like the adv instruction
# except that the result is stored in the C register. (The numerator is still read from the A register.)
def cdv(operand):
    global a; global c
    operand = lit_to_combo(operand)
    c = int(a/pow(2,operand))
    return c

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's 
# literal operand, then stores the result in register B.
def bxl(operand):
    global b
    b = b^operand
    return b

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), 
# then writes that value to the B register.
# Jag struntar i "lowest 3 bit"-grejen och kör bara vanlig mod men det kanske biter mig i del 2
def bst(operand):
    global b
    operand = lit_to_combo(operand)
    b = operand % 8
    return b

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero,
# it jumps by setting the instruction pointer to the value of its literal operand; 
# if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
def jnz(operand):
    global a; global pointer
    if a == 0:
        return -1
    #print("In jnz, sets pointer to",operand)
    pointer = operand
    return pointer

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. 
# (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(operand):
    global b; global c
    b = b^c
    return b

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. 
# (If a program outputs multiple values, they are separated by commas.)
def out(operand):
    global result
    operand = lit_to_combo(operand)
    result.append(operand % 8)

start = time.time()
FILENAME = "17/L17.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

b = int(re.findall(r"\d+",INPUT[1])[0])
c = int(re.findall(r"\d+",INPUT[2])[0])

program = list(map(int,(re.findall(r"\d+",INPUT[4]))))
print(program)

start_a = 164278899142274 #pow(8,14)
# 35000005127958 gives 15 numbers idek
# 35184372080000
# 119137648299999 ger nästan rätt svar om man letar efter inputens output men tar exemplets operationer SKJUT MIG
# start is over 5424195
# start is over 16571082
# start is over 16816652
# start is over 20295965 
# start is over 25576196
# start is over 100000000036255
result = []
while start_a < pow(8,17) and not keyboard.is_pressed('§'):
    #print(start_a)
    a = start_a
    # My guess is that a is 0 through the entire last program run which
    # turns b and c to 0 as well 
    result = []
    pointer = 0
    while pointer < len(program):
        #print(a,b,c)
        #print("Opcode:",program[pointer])
        #print("Pointer:",pointer)
        #print("a:",a)
        did_jump = False
        match program[pointer]:
            case 0:
                adv(program[pointer+1])
            case 1:
                bxl(program[pointer+1])
            case 2:
                bst(program[pointer+1])
            case 3:
                did_jump = jnz(program[pointer+1]) != -1
            case 4:
                bxc(program[pointer+1])
            case 5:
                out(program[pointer+1])
            case 6:
                bdv(program[pointer+1])
            case 7:
                cdv(program[pointer+1])

        if not did_jump:
            pointer += 2
    #print(program)
    #print(result)
    samesies = True
    for q,p in zip(result, program):
        if q != p:
            samesies = False
    
    if result == program or samesies:
        break

    #if result[5] == 5 and result[4] == 7 and result[3] == 1 and result[2] == 1 and result[1] == 4:
    #    print(result,start_a)

    output = "["
    for elem in reversed(result):
        output += str(elem)+", "
    print(output+"]"+str(len(result)))
    #print(len(result))
    start_a += 1

#print("§ pressed at start_a=",start_a)


print("Lowest value for A to make output match input:",start_a)
stop = time.time()
print("This took",stop-start,"seconds!")