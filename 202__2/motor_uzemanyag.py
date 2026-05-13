korok = int(input("Adja meg a teljesitendo korok szamat: "))
fogyasztas = float (input("Adja meg az átlag fogyasztást literben  egy körre:  "))
tartaly = int(input("Adja meg a tartály méreteét literben: "))
szukseges = korok*fogyasztas
print(f"A versenyhez szükséges üzemanyag {szukseges} liter")
if szukseges < tartaly:
    print("a tartály elegendő a versenyhez")
else:
    szukseges > tartaly
    kell = szukseges - tartaly
    print(f"Nem elegendő a tartály. Ennyi üzemanyag kell még {kell} liter")