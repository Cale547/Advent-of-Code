FILENAME = "2025/11/input.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

connections = {}
for row in INPUT:
    row = row.strip().split(':')
    device = row[0]
    outputs = row[1].split(' ')
    outputs.remove('')
    connections[device] = outputs
# for elem in connections:
#     print(f"{elem} : {connections[elem]}")


what_we_know = {}
def howManyPathsToOutQuestionMark(device:str,fft:bool,dac:bool):
    outputs = connections[device]
    if outputs[0] == "out" and not (fft and dac):
        key = f"{device},{fft},{dac}"
        what_we_know[key] = 0
        return 0
    
    if outputs[0] == "out" and fft and dac:
        key = f"{device},{fft},{dac}"
        what_we_know[key] = 1
        return 1
    
    new_fft = fft or device=="fft"
    new_dac = dac or device=="dac"
    sum_of_outputs = 0
    for output in outputs:
        key = f"{output},{new_fft},{new_dac}"
        if key in what_we_know:
            sum_of_outputs += what_we_know[key]
        else:
            sum_of_outputs += howManyPathsToOutQuestionMark(output,new_fft,new_dac)
    
    if sum_of_outputs == 0:
        key = f"{device},{fft},{dac}"
        what_we_know[key] = 0
        return 0
    else:
        key = f"{device},{fft},{dac}"
        what_we_know[key] = sum_of_outputs
        return sum_of_outputs

print("Answer: ",howManyPathsToOutQuestionMark("svr",False,False))
