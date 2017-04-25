spil = []
with open("hrutar.txt", "r") as hrutarnir:
    for line in hrutarnir:
        spil.append(line)
print("Hrútar:\n")
for line in spil:
    print("Nafn, Þyngd, Mjólkurlagnir, Ull, Afkvæmi, Einkunn Læris, Frjósemi, Gerð/þykkt bakvöðva, Einkun fyrir malir ")
    print(line)
