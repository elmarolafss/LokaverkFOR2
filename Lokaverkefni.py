import random
from ast import literal_eval
import sys
import time

spil = []
with open("hrutar.txt") as hrutarnir:
    for line in hrutarnir:
        line = line.strip('\r\n')
        spil.append(literal_eval(line))
valmynd = 1
while valmynd == 1:
    print("1. Sjá alla hrúta\n"
          "2. Spila\n")
    val = int(input("Vinsamlegast veldu lið: "))
    if val == 1:
        print("Hrútar:\n")
        for line in spil:
            print("Nafn, Þyngd, Mjólkurlagnir, Ull, Afkvæmi, Einkunn Læris, Frjósemi, Gerð/þykkt bakvöðva, Einkun fyrir malir ")
            print(line)
    if val == 2:
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
        byrjun = random.randint(1, 2)
        svar = 1
        while svar == 1:

            templistjafnt = []
            templistwin = []
            if byrjun == 1:
                print("\nNotandi á leik")
                print("Þinn Hrútur:\n"
                      "Nafn: %s\n"
                      "1. Þyngd = %s\n"
                      "2. Mjolkurlagning = %s\n"
                      "3. Ull = %s\n"
                      "4. Afkvæmi = %s\n"
                      "5. Einkun Læris = %s\n"
                      "6. Frjósemi = %s\n"
                      "7. Gerð/Þykkt Bakvöðva = %s\n"
                      "8. Einkunn fyrir malir = %s" % (notandi[0][0],notandi[0][1], notandi[0][2], notandi[0][3], notandi[0][4], notandi[0][5], notandi[0][6], notandi[0][7], notandi[0][8]))
                val = int(input("Veldu flokk(1-8) til að keppst með: "))


                while val:
                    print("\nNotandinn: %s" % notandi[0])
                    print("Tölva: %s" % tolva[0])
                    print("Notandi: %s vs Tölva: %s" % (notandi[0][val], tolva[0][val]))
                    if notandi[0][val] > tolva[0][val]:
                        print("Spilið þitt vann")
                        templistwin.append(notandi[0])
                        templistwin.append(tolva[0])
                        tolva.remove(tolva[0])
                        notandi.remove(notandi[0])
                        for i in templistwin:
                            notandi.append(i)
                        for i in templistjafnt:
                            notandi.append(i)
                        templistjafnt.clear()
                        templistwin.clear()
                        teljariN = 0
                        teljariT = 0
                        for i in notandi:
                            teljariN += 1
                        for i in tolva:
                            teljariT += 1
                        print("Fjöldi spila Notanda: %s" % teljariN)
                        print("Fjöldi spila Tölvu: %s" % teljariT)
                        twin = 0
                        nwin = 0
                        for i in tolva:
                            twin += 1
                        for i in notandi:
                            nwin += 1
                        if twin == 0:
                            print("Þú vannst!")
                            svar = 0
                            break
                        if nwin == 0:
                            print("Tölvan vann!")
                            svar = 0
                            break
                        if twin > 0 and nwin > 0:
                            print("Ýttu á enter til að halda áfram")
                            input()
                            byrjun = 2
                    elif notandi[0][val] == tolva[0][val]:
                        print("Jafnt, sá sem vinnur næstu hönd fær spilin")
                        templistjafnt.append(notandi[0])
                        templistjafnt.append(tolva[0])
                        notandi.remove(notandi[0])
                        tolva.remove(tolva[0])
                        teljariN = 0
                        teljariT = 0
                        for i in notandi:
                            teljariN += 1
                        for i in tolva:
                            teljariT += 1
                        print("Fjöldi spila Notanda: %s" % teljariN)
                        print("Fjöldi spila Tölvu: %s" % teljariT)
                        twin = 0
                        nwin = 0
                        for i in tolva:
                            twin += 1
                        for i in notandi:
                            nwin += 1
                        if twin == 0:
                            print("Þú vannst!")
                            svar = 0
                            break
                        if nwin == 0:
                            print("Tölvan vann!")
                            svar = 0
                            break
                        if twin > 0 and nwin > 0:
                            print("Ýttu á enter til að halda áfram")
                            input()
                            byrjun = 2
                    else:
                        print("Spil Tölvunar vann")
                        templistwin.append(notandi[0])
                        templistwin.append(tolva[0])
                        notandi.remove(notandi[0])
                        tolva.remove(tolva[0])
                        for i in templistwin:
                            tolva.append(i)
                        for i in templistjafnt:
                            tolva.append(i)
                        templistjafnt.clear()
                        templistwin.clear()
                        teljariN = 0
                        teljariT = 0
                        for i in notandi:
                            teljariN += 1
                        for i in tolva:
                            teljariT += 1
                        print("Fjöldi spila Notanda: %s" % teljariN)
                        print("Fjöldi spila Tölvu: %s" % teljariT)
                        twin = 0
                        nwin = 0
                        for i in tolva:
                            twin += 1
                        for i in notandi:
                            nwin += 1
                        if twin == 0:
                            print("Þú vannst!")
                            svar = 0
                            break
                        if nwin == 0:
                            print("Tölvan vann!")
                            svar = 0
                            break
                        if twin > 0 and nwin > 0:
                            print("Ýttu á enter til að halda áfram")
                            input()
                            byrjun = 2
                    break
            if byrjun == 2:
                print("Tölvan á leik")
                print("Tölvan hugsar", end="")
                text = ("......")
                for char in text:
                    sys.stdout.flush()
                    print(char, end="")
                    time.sleep(1)
                tala = random.randint(1,8)
                print("\nTölvan hefur valið flokk %s" % tala)
                print("Notandinn: %s" % notandi[0])
                print("Tölva: %s" % tolva[0])
                print("Notandi: %s vs Tölva: %s" % (notandi[0][tala], tolva[0][tala]))
                if notandi[0][tala] > tolva[0][tala]:
                    print("Spilið þitt vann")
                    templistwin.append(notandi[0])
                    templistwin.append(tolva[0])
                    notandi.remove(notandi[0])
                    tolva.remove(tolva[0])
                    for i in templistwin:
                        notandi.append(i)
                    for i in templistjafnt:
                        notandi.append(i)
                    templistjafnt.clear()
                    templistwin.clear()
                    teljariN = 0
                    teljariT = 0
                    for i in notandi:
                        teljariN += 1
                    for i in tolva:
                        teljariT += 1
                    print("Fjöldi spila Notanda: %s" % teljariN)
                    print("Fjöldi spila Tölvu: %s" % teljariT)
                    twin = 0
                    nwin = 0
                    for i in tolva:
                        twin += 1
                    for i in notandi:
                        nwin += 1
                    if twin == 0:
                        print("Þú vannst!")
                        svar = 0
                        break
                    if nwin == 0:
                        print("Tölvan vann!")
                        svar = 0
                        break
                    if twin > 0 and nwin > 0:
                        print("Ýttu á enter til að halda áfram")
                        input()
                        byrjun = 1
                elif notandi[0][tala] == tolva[0][tala]:
                    print("Jafnt, sá sem vinnur næstu hönd fær spilin")
                    templistjafnt.append(notandi[0])
                    templistjafnt.append(tolva[0])
                    notandi.remove(notandi[0])
                    tolva.remove(tolva[0])
                    teljariN = 0
                    teljariT = 0
                    for i in notandi:
                        teljariN += 1
                    for i in tolva:
                        teljariT += 1
                    print("Fjöldi spila Notanda: %s" % teljariN)
                    print("Fjöldi spila Tölvu: %s" % teljariT)
                    twin = 0
                    nwin = 0
                    for i in tolva:
                        twin += 1
                    for i in notandi:
                        nwin += 1
                    if twin == 0:
                        print("Þú vannst!")
                        svar = 0
                        break
                    if nwin == 0:
                        print("Tölvan vann!")
                        svar = 0
                        break
                    if twin > 0 and nwin > 0:
                        print("Ýttu á enter til að halda áfram")
                        input()
                        byrjun = 1
                else:
                    print("Spil Tölvunar vann")
                    templistwin.append(notandi[0])
                    templistwin.append(templistwin[0])
                    notandi.remove(notandi[0])
                    tolva.remove(tolva[0])
                    for i in templistwin:
                        tolva.append(i)
                    for i in templistjafnt:
                        tolva.append(i)
                    templistwin.clear()
                    templistjafnt.clear()
                    teljariN = 0
                    teljariT = 0
                    for i in notandi:
                        teljariN += 1
                    for i in tolva:
                        teljariT += 1
                    print("Fjöldi spila Notanda: %s" % teljariN)
                    print("Fjöldi spila Tölvu: %s" % teljariT)
                    twin = 0
                    nwin = 0
                    for i in tolva:
                        twin += 1
                    for i in notandi:
                        nwin += 1
                    if twin == 0:
                        print("Þú vannst!")
                        svar = 0
                        break
                    if nwin == 0:
                        print("Tölvan vann!")
                        svar = 0
                        break
                    if twin > 0 and nwin > 0:
                        print("Ýttu á enter til að halda áfram")
                        input()
                        byrjun = 1

