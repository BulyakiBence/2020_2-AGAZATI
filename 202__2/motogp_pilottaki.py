class Pilota:
    def __init__(self, nev, csapat, nemz, rajtsz, osszpont):
        self.nev = nev
        self.csapat = csapat
        self.nemz = nemz
        self.rajtszam = int(rajtsz)
        self.osszpont =  int(osszpont)

fajl = open("202__2/pilottak.txt" , "r", encoding="utf-8")
pilotak = []
for sor in fajl:
    adatok = sor.strip().split(";")
    uj = Pilota(
        adatok[0],
        adatok[1],
        adatok[2],
        adatok[3],
        adatok[4]
    )
    pilotak.append(uj)
fajl.close()
print("3.2 feladat")
print(f"Az állományban {len(pilotak)} pilóta adatai szerepelnek")

legjobb = pilotak[0]
for p in pilotak:
    if p.osszpont > legjobb.osszpont:
        legjobb = p
print(" 3.3 feladat.A legtöbb pontot sze3rző pilóta:")
print(f"Név:{legjobb.nev}\n Csapat: {legjobb.csapat} \n Nemzetiség: {legjobb.nemz} \n Rajtszám {legjobb.rajtszam} \n Pontszám:{legjobb.osszpont}")


print("3.4 feladat")
csap = str(input("Mondj egy csapatot: "))
van = False
for p in pilotak:
    if p.csapat == csap:
        print(p.nev)
        van = True
if van == False:
    print("Nincsen ilyen csapat.")

#3.5 feladat
ossz = 0
darab = 0
for p in pilotak:
    if p.nemz == "spanyol":
        ossz += p.osszpont
        darab +=1
atlag = ossz/darab
print(f"A spanyol őpilóták átlagosan {atlag:.2f} pontot szereztek")    