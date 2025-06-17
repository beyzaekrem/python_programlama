#mayin tarlasi
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from game_window import OyunPenceresi

class AnaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mayın Tarlası - Ana Menü")
        self.setGeometry(100, 100, 300, 150)

        dikey_düzen = QVBoxLayout()

        yeni_oyun_butonu = QPushButton("Yeni Oyun")
        yeni_oyun_butonu.clicked.connect(self.oyunu_baslat)
        dikey_düzen.addWidget(yeni_oyun_butonu)

        cikis_butonu = QPushButton("Çıkış")
        cikis_butonu.clicked.connect(self.close)
        dikey_düzen.addWidget(cikis_butonu)

        self.setLayout(dikey_düzen)

    def oyunu_baslat(self):
        self.hide()  
        self.oyun_penceresi = OyunPenceresi()
        self.oyun_penceresi.show()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = AnaMenu()
    pencere.show()
    sys.exit(uygulama.exec_())
