'''1-1000 aralığında seçilen rastgele 4 sayı x1,y1,x2 ve y2 sütunlarına yerleştirilir. 
Bu işlem 100 defa yapılır. Bu sayılar iki boyutlu uzaydaki bir dikdörtgenin 2 köşe noktasının x ve y koordinatlarını temsil etmektedir.
Bu sayılar iki köşe noktasının x ve y koordinatlarını temsil edeceği için x1 x2'den büyük olamaz aynı şekilde y1 de y2'den büyük olamaz.
Ayrıca bir dikdörtgenin herhangi bir kenar uzunluğu 100'den büyük olamaz.
Daha sonra veritabanından bu değerleri okuyarak üç durum için kontroller yapılır. 
Bu üç durum; iki dikdörtgenin kesişmesi, bir dikdörtgenin diğerini kapsaması ve bir dikdörtgenin uzaydaki hiçbir dikdörtgen ile kesişmemesi.
Hiçbir dikdörtgen ile temas etmeyen dikdörtgenleri, birbiriyle kesişen dikdörtgenleri ve bir dikdörtgen tarafından kapsanmış dikdörtgenleri açıklamalı bir şekilde ekrana yazdırılır. '''
import sqlite3
import random
import os

veritabani_yolu = os.path.expanduser("~/Desktop/python_odev4/dikdortgenler.db")

if os.path.exists(veritabani_yolu):
    os.remove(veritabani_yolu)

baglanti = sqlite3.connect(veritabani_yolu)
komut_araci = baglanti.cursor() 

komut_araci.execute("""
CREATE TABLE dikdortgenler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x1 INTEGER, y1 INTEGER, x2 INTEGER, y2 INTEGER
)
""")

def dikdortgen_uret():
    x1 = random.randint(1, 900)
    y1 = random.randint(1, 900)
    genislik = min(100, 1000 - x1)
    yukseklik = min(100, 1000 - y1)
    x2 = x1 + random.randint(1, genislik)
    y2 = y1 + random.randint(1, yukseklik)
    return (x1, y1, x2, y2)

for _ in range(100):
    x1, y1, x2, y2 = dikdortgen_uret()
    komut_araci.execute("INSERT INTO dikdortgenler (x1, y1, x2, y2) VALUES (?, ?, ?, ?)", (x1, y1, x2, y2))
baglanti.commit()

komut_araci.execute("SELECT * FROM dikdortgenler")
tum_dikdortgenler = komut_araci.fetchall()

def kesisiyor_mu(d1, d2):
    return not (d1[2] < d2[0] or d1[0] > d2[2] or d1[3] < d2[1] or d1[1] > d2[3])

def kapsiyor_mu(d1, d2):
    return d1[0] <= d2[0] and d1[1] <= d2[1] and d1[2] >= d2[2] and d1[3] >= d2[3]

kesisenler = set()
kapsananlar = []
temassizlar = []

for i, d1 in enumerate(tum_dikdortgenler):
    id1, x1, y1, x2, y2 = d1
    dikdortgen1 = (x1, y1, x2, y2)
    temas_var_mi = False

    for j, d2 in enumerate(tum_dikdortgenler):
        if i == j:
            continue
        id2, a1, b1, a2, b2 = d2
        dikdortgen2 = (a1, b1, a2, b2)

        if kesisiyor_mu(dikdortgen1, dikdortgen2):
            temas_var_mi = True
            kesisenler.add(frozenset({id1, id2}))
        if kapsiyor_mu(dikdortgen2, dikdortgen1) and dikdortgen1 != dikdortgen2:
            kapsananlar.append((id1, dikdortgen1, id2, dikdortgen2))

    if not temas_var_mi:
        temassizlar.append((id1, dikdortgen1))

print("\nKapsanan Dikdörtgenler:\n")
for id1, d1, id2, d2 in kapsananlar:
    print(f"{id1} id'li({d1[0]},{d1[1]})-({d1[2]},{d1[3]}) dikdörtgeni, "
          f"{id2} id'li({d2[0]},{d2[1]})-({d2[2]},{d2[3]}) dikdörtgeni tarafından kapsanmaktadır.")

print("\nKesişen Dikdörtgen Çiftleri:\n")
for cift in sorted(kesisenler): 
    id1, id2 = sorted(cift)
    print(f"{id1} id'li dikdörtgen ile {id2} id'li dikdörtgen kesişmektedir.")

print("\nTemas Etmeyen Dikdörtgenler:\n")
for id1, d1 in temassizlar:
    print(f"{id1} id'li({d1[0]},{d1[1]})-({d1[2]},{d1[3]}) dikdörtgeni hiçbir dikdörtgen ile temas etmemektedir.")

print("\n Genel Sonuç:\n")
print(f"-Toplam dikdörtgen: {len(tum_dikdortgenler)}")
print(f"-Kesişen çift sayısı: {len(kesisenler)}")
print(f"-Kapsanan dikdörtgen sayısı: {len(kapsananlar)}")
print(f"-Temas etmeyen dikdörtgen sayısı: {len(temassizlar)}")

print("\n\nKontrol için ilk 5 kayıt:\n")
komut_araci.execute("SELECT * FROM dikdortgenler LIMIT 5")
for satir in komut_araci.fetchall():
    print(satir)

baglanti.close()
