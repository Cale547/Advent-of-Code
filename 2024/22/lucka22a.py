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



FILENAME = "22/L22.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()

secrets = list(map(str.strip,INPUT))
for i,s in enumerate(secrets):
    secrets[i] = int(s)
print(secrets)

for i in range(2000):
    for j,s in enumerate(secrets):
        s = mul64(s)
        s = div32(s)
        secrets[j] = mul2048(s)
answer = sum(secrets)
print("The sum of all buyers' 2000th number is",answer)