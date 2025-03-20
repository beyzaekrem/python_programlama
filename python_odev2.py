#blok şifreleme ile şifrelenmiş metin çözümü
import string

sifreli_metin = """Aupf zrjelg trzfhtl vz nibbg vs Ybnhlypxl thzlf Ybnhlypxl vz n zgfyl bm evyl csnfvut nntr aehqpgpbunsyf
ponynjglepmlq il h qbanrva jehjs goevhnu wevplqbehysl nrurynark ylilyz gbeu ohflq nntrwyhl nepq inzrk
zvilzlaa nuq wryzhalaa qlnau vs aul csnfry ponynjgle Tbzg ybnhlypxlf hel ohflq va h upto shaanzl unyehgpil
elssrjgpan gor pamybrupl bm ghosrabw evyl csnfvut nntrz fbpo nz Qbanrvaz nuq Kehtvaz Evtbr duppo vz nu
NZPPV inzrk thzl gona ebaz vu gletvuns by gletvuns rthsnaby vz pvazvkryrk gor mbyryhuale hak gor untrznrr
vs aul tlayr dvau kryvcnavcr nntrz zpeybyvut aul ponynjgle vs Ybnhl by fwepgl ohflq nehcovjf"""

def harfin_alfabe_sirasi(harf):
    return ord(harf.lower()) - ord('a') + 1

def metni_cozumle(metin,anahtar):
    cozulen_karakterler_listesi = [] 
    anahtar_uzunluk = len(anahtar) 
    anahtar_indeks = 0 

    for karakter in metin: 
        if karakter.isalpha(): 
            kaydirma = harfin_alfabe_sirasi(anahtar[anahtar_indeks % anahtar_uzunluk])
            if karakter.isupper():
                temel = ord('A') 
                yeni_karakter = chr((ord(karakter) - temel - kaydirma) % 26 + temel)
            else:                     
                temel = ord('a')
                yeni_karakter = chr((ord(karakter) - temel - kaydirma) % 26 + temel)
            cozulen_karakterler_listesi.append(yeni_karakter)  
            anahtar_indeks += 1    
        else:
            cozulen_karakterler_listesi.append(karakter)
    return ''.join(cozulen_karakterler_listesi) 

def mantikli_mi(duz_metin):
    yaygin_kelimeler = [" the "," and "," that "," have "," for "," with "," this "]
    metnin_kucukharfli_hali = duz_metin.lower()  
    return any(kelime in metnin_kucukharfli_hali for kelime in yaygin_kelimeler)

alfabe = string.ascii_lowercase
dogru_sonuc_listesi = [] 

for ilk in alfabe:
    for ikinci in alfabe:
        anahtar = ilk + ikinci  
        duz_metin = metni_cozumle(sifreli_metin,anahtar) 
        if mantikli_mi(duz_metin): 
            dogru_sonuc_listesi.append((anahtar,duz_metin)) 

for anahtar,metin in dogru_sonuc_listesi:
    print(f"\nanahtar: {anahtar}\n\nmetnimizin cozulmus hali :\n\n{metin}\n")