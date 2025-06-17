from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QGridLayout
import random

class OyunPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mayın Tarlası")
        self.setGeometry(100, 100, 600, 600)

        self.butonlar = []  
        self.acilan_kutular = set()
        self.mayinlar = random.sample(range(100), 10)  

        duzen = QGridLayout()

        for satir in range(10):
            for sutun in range(10):
                indeks = satir * 10 + sutun
                buton = QPushButton("")
                buton.setFixedSize(50, 50)
                buton.clicked.connect(lambda _, i=indeks: self.kutuya_tiklandi(i))
                duzen.addWidget(buton, satir, sutun)
                self.butonlar.append(buton)

        self.setLayout(duzen)

    def kutuya_tiklandi(self, indeks):
        if indeks in self.mayinlar:
            self.tum_mayinlari_goster()
            QMessageBox.critical(self, "Kaybettiniz", "Oyunu kaybettiniz.")
            self.close()
        elif indeks not in self.acilan_kutular:
            self.kutu_ac(indeks)
            self.rastgele_guvenli_ac(4)
            if len(self.acilan_kutular) == 90:
                QMessageBox.information(self, "Kazandınız", "Tebrikler oyunu kazandınız!")
                self.close()

    def kutu_ac(self, indeks):
        self.acilan_kutular.add(indeks)
        buton = self.butonlar[indeks]
        buton.setStyleSheet("background-color: green")
        buton.setEnabled(False)

    def rastgele_guvenli_ac(self, adet):
        kalan_kutular = list(set(range(100)) - set(self.mayinlar) - self.acilan_kutular)
        for i in random.sample(kalan_kutular, min(adet, len(kalan_kutular))):
            self.kutu_ac(i)

    def tum_mayinlari_goster(self):
        for indeks in self.mayinlar:
            self.butonlar[indeks].setStyleSheet("background-color: red")
