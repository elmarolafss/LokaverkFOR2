import random
from ast import literal_eval
import sys
import time

spil = []
with open("hrutar.txt") as hrutarnir:
    for line in hrutarnir:
        line = line.strip('\r\n')
        spil.append(literal_eval(line))#appenda öll spilin  í txt skránni í spil listann
byrja = 1
while byrja == 1:#lykkja undir allan leikinn
    print("1. Sjá alla hrúta\n"
        "2. Spila\n")
    bval = int(input("Veldu lið: "))
    if bval == 1:
        print("Hrútar:\n")
        for line in spil:
            print("Nafn, Þyngd, Mjólkurlagnir, Ull, Afkvæmi, Einkunn Læris, Frjósemi, Gerð/þykkt bakvöðva, Einkun fyrir malir ")
            print(line)#sýni alla hrúta
    if bval == 2:
        notandi = []
        tolva = []
        random.shuffle(spil)#random shuffla bunkann
        counter = 0
        for item in spil:
            notandi.append(item)
            spil.remove(item)
            counter += 1
            if counter == 26:#notandi fær 26 spil
                break
        counter = 0
        for item in spil:
            tolva.append(item)

            counter += 1
            if counter == 26:#tölva fær 26 spil
                break
        print("\nSpilunum hefur verið skipt í tvennt")
        byrjun = random.randint(1, 2)#random hver byrjar
        svar = 1
        while svar == 1:

            templistjafnt = []
            templistwin = []#2 listar undir vinning og jafntefli
            if byrjun == 1:
                print("\nÞú á leik")
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
                val = int(input("Veldu flokk(1-8) til að keppst með: "))#notandi getur valið sinn eigin flokk


                while val:
                    print("\nÞitt spil: %s" % notandi[0])
                    print("Tölva: %s" % tolva[0])
                    print("Þitt spil: %s vs Tölva: %s" % (notandi[0][val], tolva[0][val]))#sýni spil beggja spilara og flokka sem keppa
                    if notandi[0][val] > tolva[0][val]:
                        print("Spilið þitt vann")#ef að spilið sem notandinn á er hærra
                        templistwin.append(notandi[0])
                        templistwin.append(tolva[0])#vinnigs listinn tekur bæði spilin
                        tolva.remove(tolva[0])
                        notandi.remove(notandi[0])#og ég eyði báðum spilunum
                        for i in templistwin:
                            notandi.append(i)#notandi fær spil úr vinnings flokknum
                        for i in templistjafnt:
                            notandi.append(i)#og jafnt flokknum, ef það eru einhver
                        templistjafnt.clear()
                        templistwin.clear()#tæmi báða listana
                        teljariN = 0
                        teljariT = 0
                        for i in notandi:
                            teljariN += 1
                        for i in tolva:
                            teljariT += 1
                        print("Fjöldi þína spila: %s" % teljariN)
                        print("Fjöldi spila Tölvu: %s" % teljariT)#birti stöður
                        twin = 0
                        nwin = 0
                        for i in tolva:
                            twin += 1
                        for i in notandi:
                            nwin += 1#tjekka hvort einhver sé búinn að vinna
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
                        print("Jafnt, sá sem vinnur næstu hönd fær spilin")#jafnt
                        templistjafnt.append(notandi[0])
                        templistjafnt.append(tolva[0])#jafnt listinn fær bæði spilin
                        notandi.remove(notandi[0])
                        tolva.remove(tolva[0])
                        teljariN = 0
                        teljariT = 0
                        for i in notandi:
                            teljariN += 1
                        for i in tolva:
                            teljariT += 1
                        print("Fjöldi þína spila: %s" % teljariN)
                        print("Fjöldi spila Tölvu: %s" % teljariT)#birti stöðu
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
                        print("Spil Tölvunar vann")#tölvan vinnur
                        templistwin.append(notandi[0])
                        templistwin.append(tolva[0])#sama er að gerast hér og uppi
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
                        print("Fjöldi þína spila: %s" % teljariN)
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
                print("Tölvan hugsar", end="")#tölvan á kleik og ég byrja að láta hana hugsa(fékk kóða hjá sigfúsi)
                text = (".....")

                for char in text:
                    sys.stdout.flush()
                    print(char, end="")
                    time.sleep(0.2)
                print("\nTölvan á leik")
                tala = random.randint(1,8)#tölvan velur random flokk
                print("Tölvan hefur valið flokk %s" % tala)
                print("Notandinn: %s" % notandi[0])
                print("Tölva: %s" % tolva[0])
                print("Þitt spil: %s vs Tölva: %s" % (notandi[0][tala], tolva[0][tala]))#prenta allar upplýsingar sem þarf
                if notandi[0][tala] > tolva[0][tala]:
                    print("Spilið þitt vann")
                    templistwin.append(notandi[0])
                    templistwin.append(tolva[0])
                    notandi.remove(notandi[0])
                    tolva.remove(tolva[0])#endurteknigar á kóða frá því að notandinn átti að gera
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
                    print("Fjöldi þína spila: %s" % teljariN)
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
                    print("Fjöldi þína spila: %s" % teljariN)
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
                    templistwin.append(tolva[0])
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
                    print("Fjöldi þína spila: %s" % teljariN)
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
    aftur = input("Spila Aftur?Y/N: ")#notandinn getur spilað aftur
    if aftur == "Y" or aftur == "y":
        bval = 2
    else:
        bval = 0
        break


