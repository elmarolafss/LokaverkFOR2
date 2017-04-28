import random
from ast import literal_eval

spil = []
with open("hrutar.txt") as hrutarnir:
    for line in hrutarnir:
        line = line.strip('\r\n')
        spil.append(literal_eval(line))

print("Hrútar:\n")
for line in spil:
    print("Nafn, Þyngd, Mjólkurlagnir, Ull, Afkvæmi, Einkunn Læris, Frjósemi, Gerð/þykkt bakvöðva, Einkun fyrir malir ")
    print(line)

notandi = []
tolva = []
random.shuffle(spil)
counter = 0
for item in spil:
    notandi.append(item)
    spil.remove(item)
    counter += 1
    if counter == 26:
        break
counter = 0
for item in spil:
    tolva.append(item)

    counter += 1
    if counter == 26:
        break
print("\nSpiunum hafa verið skipt í tvennt")

svar = 1
while svar == 1:

    byrjun = random.randint(1, 2)
    print(byrjun)
    if byrjun == 1:
        print("\nNotandi á leik")
        print("Flokkar:\n"
              "1. Þyngd\n"
              "2. Mjolkurlagning\n"
              "3. Ull\n"
              "4. Afkvæmi\n"
              "5. Einkun Læris\n"
              "6. Frjósemi\n"
              "7. Gerð/Þykkt Bakvöðva\n"
              "8. Einkun fyrir malir\n")
        val = int(input("Veldu flokk(1-8) til að keppst með: "))
        skiptaN = 26
        skiptaT = 26
        while val:
            print("Notandinn: %s" % notandi[0])
            print("Tölva: %s" % tolva[0])
            if notandi[0][val] > tolva[0][val]:
                print("Spil notandanns vann")
                notandi.append(tolva[0])
                tolva.remove(tolva[0])
                skiptaN += 1
                skiptaT -= 1
            else:
                print("Spil Tölvunar vann")
                tolva.append(notandi[0])
                notandi.remove(notandi[0])
            break
        if skiptaN == 0:
            svar = 0
            break
        elif skiptaT == 0:
            svar = 0
            break

    if byrjun == 2:
        print("\nTölvan byrjar")
        break