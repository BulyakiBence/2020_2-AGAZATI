korok = int(input("Köröki száma: "))
fogyasztas = float (input("Átlagos fogyasztás körönént (literben):  "))
tartaly = int(input("tartály méret (liter): "))
szukseges = korok*fogyasztas
print(f"A versenyhez szükséges üzemanyag {szukseges} liter")
if szukseges < tartaly:
    print("A tartály elegendő a versenyhez!")
else:
    szukseges > tartaly
    kell = szukseges - tartaly
    print(f"A tartály NEM elegend. Ennyi üzemanyag kell még {kell} liter")