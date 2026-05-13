class Pilotak:
    def __init__(self, nev, csapat, nemz, rajtsz, osszpont):
        self.nev = nev
        self.csapat = csapat
        self.nemz = nemz
        self.rajtszam = int(rajtsz)
        self.osszpont =  int(osszpont)

fajl = open("202__2/pilottak.txt" , "r", encoding="utf-8")
for sor in fajl:
    adatok = sor.strip().split(";")
    uj = Pilotak(
        adatok[0],


    )