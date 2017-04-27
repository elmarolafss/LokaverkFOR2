import random
import csv
from copy import *
listoflists = []
spil = []
with open("hrutar.txt", "r") as hrutarnir:
    for line in csv.reader(hrutarnir):
        spil.append(line)
        listoflists.append((spil[:], spil[0]))
print(spil)
print(listoflists)
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
    val = int(input("Veldu flokk(1-8) til að keppst með: "))

    while val:
        print("Notandinn: %s" % notandi[0][val])
        print("Tölva: %s" % tolva[0])
        if notandi[0][val] > tolva[0][val]:
            print("Spil notandanns vann")
        else:
            print("Spil Tölvunar vann")
        break
