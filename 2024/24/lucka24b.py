import time

start = time.time()
FILENAME = "24/L24ex2.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

wires = {}
for init in INPUT:
    if init == '\n':
        break
    init = list(map(str.strip,init.split(':')))
    wires[init[0]] = int(init[1])
wire_keys = sorted(wires.keys(),reverse=True)
#print(wires)

x_res = ''
y_res = ''
for w in wire_keys:
    if w.startswith('x'):
        x_res += str(wires[w])
    elif w.startswith('y'):
        y_res += str(wires[w])
x = int(x_res,2)
y =  int(y_res,2)
#print(x_res)
#print(y_res)
print("x in binary is", x)
print("y in binary is", y)
expected_z = bin(x+y)
print("Expected z result is", expected_z[2:], x+y)



gates = set()
for gate in INPUT[len(wires)+1:]:
    gate = gate.strip().split()
    gates.add((gate[0],gate[1],gate[2],gate[4]))

# gates[0] = in1, gates[1] = operation, gates[2] = in2, gates[3] = out
while len(gates) > 0:
    gates_copy = gates.copy()
    for g in gates:
        in1 = g[0]
        in2 = g[2]
        op = g[1]
        out = g[3]

        if in1 in wires and in2 in wires:
            in1 = wires[g[0]]
            in2 = wires[g[2]]
            match op:
                case 'AND':
                    wires[out] = in1 and in2
                case 'OR':
                    wires[out] = in1 or in2
                case 'XOR':
                    wires[out] = in1^in2
            gates_copy.remove(g)
    gates = gates_copy.copy()
wire_keys = sorted(wires.keys(),reverse=True)
#print(wires)

result = ''
for w in wire_keys:
    if not w.startswith('z'):
        break
    #print(w,wires[w])
    result += str(wires[w])
print("The binary number converts to",int(result,2))
