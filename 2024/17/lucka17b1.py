program = [2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0]

a_start = 0
index = len(program)-1
while index > -1:
    for a in range(a_start,a_start+8):
        print(a)
        b = (a % 8)^1
        c = int(a/pow(2,b))
        b = (b^5)^c
        out = (b%8)
        if out == program[index]:
            print("When a is",a,"out is",out)
            a_start = a*8
            index -= 1
            break
            #print(a_start)
    
#Fakta: a är 4 sista iterationen
# sedan blir int(4/8)=0 och vi är klara
