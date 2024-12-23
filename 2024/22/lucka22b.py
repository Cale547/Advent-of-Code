import time

def mul64(secret: int):
    old = secret
    secret *= 64
    old = old^secret
    return old % 16777216

def div32(secret: int):
    old = secret
    secret = int(secret/32)
    old = old^secret
    return old % 16777216

def mul2048(secret: int):
    old = secret
    secret *= 2048
    old = old^secret
    return old % 16777216


start = time.time()
FILENAME = "22/L22.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

secrets = []
for i,s in enumerate(INPUT):
    secrets.append([int(s)])

for i in range(2000):
    for j,s in enumerate(secrets):
        #print("s[i]=",s[i])
        temp_s = mul64(s[i])
        temp_s = div32(temp_s)
        secrets[j].append(mul2048(temp_s))

# Correcting prices and adding diffs
for lista in secrets:
    lista[0] = (lista[0] % 10,'')
    for j,num in enumerate(lista[1:],1):
        new = num % 10
        lista[j] = (num % 10, new - lista[j-1][0])

# Extracting all possible price sequences and their banana count
sequences = {}
for price_diff in secrets:
    for j,pd in enumerate(price_diff[1:len(price_diff)-3],1):
        cool_tuple = (price_diff[j][1], price_diff[j+1][1], price_diff[j+2][1], price_diff[j+3][1])
        if cool_tuple not in sequences:
            sequences[cool_tuple] = 0

# Trying all possible price sequences and noting how many bananas they yield
for price_diff in secrets:
    currently_visited = set()
    for j,pd in enumerate(price_diff[1:len(price_diff)-3],1):
        cool_tuple = (price_diff[j][1], price_diff[j+1][1], price_diff[j+2][1], price_diff[j+3][1])
        if cool_tuple in currently_visited:
            continue
        if cool_tuple in sequences:
            sequences[cool_tuple] += price_diff[j+3][0]
            currently_visited.add(cool_tuple)

banana_gain = []
for key in sequences:
    banana_gain.append(sequences[key])
banana_gain.sort()
#print("Banana gains:",banana_gain)
max_banana_gain = max(banana_gain)
print("The maximum amount of bananas possible is",max_banana_gain)
# 1608 is too low

print("This took",time.time()-start,"seconds.")