def text_to_num(number):
    if (number == "zero"):
        return "0"
    if (number == "one"):
        return "1"
    if (number == "two"):
        return "2"
    if (number == "three"):
        return "3"
    if (number == "four"):
        return "4"
    if (number == "five"):
        return "5"
    if (number == "six"):
        return "6"
    if (number == "seven"):
        return "7"
    if (number == "eight"):
        return "8"
    if (number == "nine"):
        return "9"


input = open("L1.txt")
#length = 0
#for entry in input:
#    length += 1
#print("Length is",length,".")

# använda .index? för att kolla förekomsten av samtliga siffror. vi letar tidigast och senast

resultat = 0

noll = "0"
ett = "1"
två = "2"
tre = "3"
fyra = "4"
fem = "5"
sex = "6"
sju = "7"
åtta = "8"
nio = "9"
siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
zero = "zero"
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"

# input is 1000 in length
for i in range(1000):
    entry = input.readline()
    siffra1 = -1
    siffra2 = -1
    hittadSiffra = False

    num_1_index = 100
    num_2_index = -100
    for j in range(len(siffror)):
        num = siffror[j]
        leftIndex = -1
        try:
            leftIndex = entry.index(num)
        except:
            leftIndex = 100
        if leftIndex < num_1_index:
            if j < 10:
                siffra1 = num
            else:
                siffra1 = text_to_num(num)
            num_1_index = leftIndex

        rightIndex = -1
        try:
            rightIndex = entry.rfind(num)
        except:
            rightIndex = -100
        if rightIndex > num_2_index:
            if j < 10:
                siffra2 = num
            else:
                siffra2 = text_to_num(num)
            num_2_index = rightIndex

    #print("Row:",i,"with siffra1 and siffra2 being",siffra1,"and",siffra2)
    
    if siffra2 == -1:
        #print(siffra1*11)
        resultat += int(siffra1*11)
    else:
        #print(siffra1*10+siffra2)
        resultat += int(siffra1)*10
        resultat += int(siffra2)
print("Resultat:",resultat)