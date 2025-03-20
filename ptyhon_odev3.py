#kalıtım ve try-exception örneği
class Ogrenci:
    def __init__(ogr,isim):
        ogr.isim = isim

class lisans_ogrencisi(Ogrenci):
    def __init__(ogr, isim, odevler, vize, final):
        super().__init__(isim)
        ogr.odevler = odevler
        ogr.vize = vize
        ogr.final = final

    def not_hesabi(ogr):
        odev_ort = sum(ogr.odevler) / len(ogr.odevler) 
        return (odev_ort * 0.3) + (ogr.vize * 0.3) + (ogr.final * 0.4)

class lisansustu_ogrencisi(Ogrenci):
    def __init__(ogr, isim, odevler, proje):
        super().__init__(isim)
        ogr.odevler = odevler
        ogr.proje = proje
        
    def not_hesabi(ogr):
        odev_ort = sum(ogr.odevler) / len(ogr.odevler)  # Ödev ortalaması
        return (odev_ort * 0.4) + (ogr.proje * 0.6)
    
def harf_notu_hesabi(not_ortalama):
    if 90 <= not_ortalama <= 100:
        return "AA"
    elif 80 <= not_ortalama < 90:
        return "BA"
    elif 70 <= not_ortalama < 80:
        return "BB"
    elif 60 <= not_ortalama < 70:
        return "CB"
    elif 50 <= not_ortalama < 60:
        return "CC"
    elif 40 <= not_ortalama < 50:
        return "DC"
    elif 30 <= not_ortalama < 40:
        return "DD"
    else:
        return "FF"
            
ogrenciler = []

while True:
    try:
        print("\n-----Ogrenci Bilgi Sistemi-----")
        secim = int(input("\nLisans öğrencisi iseniz 1'e, lisansüstü öğrencisi iseniz 2'ye basınız! Çıkmak için 0'a basınız. "))

        if secim == 1:
            print("\nlisans öğrencisi girişine hoş geldiniz!")
            print("\nlütfen istenilen bilgileri giriniz:")
            isim = input("\nisim: ")
            
            odevler = []
            for i in range(6):
                while True:
                    try:
                        odev = int(input(f"\n{i+1}. Ödev Notu (0-100): "))
                        if 0 <= odev <= 100:
                            odevler.append(odev)
                            break
                        else:
                            print("not degeri 0-100 araliginda olmalidir! ")
                    except ValueError:
                        print("\ngecersiz sayi girisi !!")

            while True:
                try:
                    vize = int(input("\nvize notu: "))
                    if 0 <= vize <= 100:
                        break
                    else:
                        print("not degeri 0-100 araliginda olmalidir! ")
                except ValueError:
                        print("\ngecersiz sayi girisi !!")
            while True:
                try:
                    final = int(input("\nfinal notu: "))
                    if 0 <= final <= 100:
                        break
                    else:
                        print("not degeri 0-100 araliginda olmalidir! ")
                except ValueError:
                    print("\ngecersiz sayi girisi !!")
            
            ogrenci = lisans_ogrencisi(isim, odevler, vize, final)
            ogrenciler.append(ogrenci)
        
        elif secim == 2:
            print("\nlisansüstü öğrencisi girişine hoş geldiniz!")
            print("\nlütfen istenilen bilgileri giriniz:")
            isim = input("\nisim: ")

            odevler = []
            for i in range(2):
                while True:
                    try:
                        odev = int(input(f"\n{i+1}. ödev notu (0-100): "))
                        if 0 <= odev <= 100:
                            odevler.append(odev)
                            break
                        else:
                            print("not degeri 0-100 araliginda olmalidir! ")
                    except ValueError:
                        print("\ngecersiz sayi girisi !!")

            while True:
                try:
                    proje = int(input("\nproje notu: "))
                    if 0 <= proje <= 100:
                        break 
                    else:
                        print("not degeri 0-100 araliginda olmalidir! ")
                except ValueError:
                    print("\ngecersiz sayi girisi !!")
            ogrenci = lisansustu_ogrencisi(isim, odevler, proje)
            ogrenciler.append(ogrenci)

        elif secim == 0:
            print("\nÖğrenci giriş işlemi tamamlandı. Kayıt edilen öğrenciler listeleniyor...\n")
            break
        
        else:
            print("\nislem yapmak icin 1 veya 2 girmeniz gerekiyor ! cikmak icin 0 giriniz.")

    except ValueError:
        print("gecersiz bir sayi girdiniz! lütfen geçerli bir sayi giriniz: ")

print("\n girilen bilgilere göre ögrencilerin not hesabı şu şekildedir: ")

for ogrenci in ogrenciler:
    ortalama = ogrenci.not_hesabi()
    harf_notu = harf_notu_hesabi(ortalama)

    print(f"\nogrencinin adi: {ogrenci.isim}")
    
    if isinstance(ogrenci, lisans_ogrencisi): 
        print(f"\nvize notu: {ogrenci.vize}")
        print(f"\nfinal notu: {ogrenci.final}")
    
    else: 
        print(f"\nproje notu: {ogrenci.proje}")

    print(f"\ngenel not ortalaması: {ortalama:.2f}")
    print(f"\nharf notu: {harf_notu}\n")


