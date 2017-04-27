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

byrjun = random.randint(1,2)


if byrjun == 1:
    print("\nNotandi Byrjar")
    print("Flokkar:"
          "1. Þyngd"
          "2. Mjolkurlagning"
          "3. Ull"
          "4. Afkvæmi"
          "5. Einkun Læris"
          "6. Frjósemi"
          "7. Gerð/Þykkt Bakvöðva"
          "8. Einkun fyrir malir")
    val = int(input("Veldu flokk(1-8) til að keppst með: "))

    while val:
        print("Notandinn: %s" % notandi[0])
        print("Tölva: %s" % tolva[0])
        if notandi[0][val] > tolva[0][val]:
            print("Spil notandanns vann")
            notandi.append(tolva[0])
            tolva.remove(tolva[0])
        else:
            print("Spil Tölvunar vann")
            tolva.append(notandi[0])
            notandi.remove(notandi[0])
        break
