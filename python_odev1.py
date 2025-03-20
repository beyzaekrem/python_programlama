#asal sayı kontrollü kutu oyunu
import random

def asal_kontrolu(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

oyuncular = {
    "Asli": 0,
    "Baris": 0,
    "Ceyda": 0,
    "Deniz": 0
}

oyun_devam_ediyor = True

while oyun_devam_ediyor:
    for oyuncu in oyuncular:
        if oyuncular[oyuncu] >= 100:
            continue
        
        zar = random.randint(1, 6)
        eski_pozisyon = oyuncular[oyuncu]
        yeni_pozisyon = eski_pozisyon + zar

        print(f"\n{oyuncu}’nin sirasi: {oyuncu} {zar} atti. {eski_pozisyon}. kareden {yeni_pozisyon}. kareye ilerledi.")

        if yeni_pozisyon % 5 == 0:
            yeni_pozisyon -= 3
            print(f"ilerledigi kare 5’in kati oldugu icin {oyuncu} 3 kare geriye gidecek. {yeni_pozisyon + 3}. kareden {yeni_pozisyon}. kareye geriledi.")

        oyuncular[oyuncu] = yeni_pozisyon

        if yeni_pozisyon >= 100:
            print(f"\n\nOYUNUN KAZANANI: {oyuncu} ")
            oyun_devam_ediyor = False
            break

        while asal_kontrolu(yeni_pozisyon):
            zar = random.randint(1, 6)
            eski_pozisyon = yeni_pozisyon
            yeni_pozisyon += zar
            print(f"{oyuncu} asal olan {yeni_pozisyon - zar}. kareye denk geldi. tekrar zar atti.  {oyuncu} {zar} attı. {eski_pozisyon}. kareden {yeni_pozisyon}. kareye ilerledi.")
            
            if yeni_pozisyon % 5 == 0:
                yeni_pozisyon -= 3
                print(f"ilerlediği kare 5’in katı oldugu icin {oyuncu} 3 kare geriye gidecek. {yeni_pozisyon + 3}. kareden {yeni_pozisyon}. kareye geriledi.")

            oyuncular[oyuncu] = yeni_pozisyon

            if yeni_pozisyon >= 100:
                print(f"\n\nOYUNUN KAZANANIIII : {oyuncu}")
                oyun_devam_ediyor = False
                break
