def gyors_kor(szam):
    if szam < 105:
        return True
    else:
        return False
    
import random
gyorsabb = []
for i in range(120):
    szam = random.randint(95,120)
    if gyors_kor(szam):
        gyorsabb.append(szam)
print(f"A 120 körből {len(gyorsabb)} volt 105 másodpercnél gyorsabb")
szazalek = len(gyorsabb)/120 * 100
print(f"Ez az összes kör {szazalek:.2f} szazleka")
