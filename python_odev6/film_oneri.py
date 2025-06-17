#film secim uygulamasi
import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTableWidget, QTableWidgetItem,
    QCheckBox, QGridLayout, QScrollArea, QGroupBox,
    QMessageBox
)

veri = pd.read_csv("HBO_MAX_Content.csv")
veri.columns = veri.columns.str.strip()
veri = veri.dropna(subset=["year", "imdb_score"])

tur_sutunlari = [sutun for sutun in veri.columns if sutun.startswith("genres_") and veri[sutun].sum() > 0]
tur_listesi = sorted([sutun.replace("genres_", "") for sutun in tur_sutunlari])

class FilmOneriUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Film Öneri Uygulaması")
        self.setGeometry(100, 100, 900, 650)
        self.arayuz_olustur()

    def arayuz_olustur(self):
        self.giris_yil = QLineEdit()
        self.giris_puan = QLineEdit()

        self.tur_kutulari = []
        tur_dizilimi = QGridLayout()
        for i, tur in enumerate(tur_listesi):
            kutu = QCheckBox(tur)
            self.tur_kutulari.append(kutu)
            satir, sutun = divmod(i, 3)
            tur_dizilimi.addWidget(kutu, satir, sutun)

        grup_kutu = QGroupBox("Tür Seçimi :")
        grup_kutu.setLayout(tur_dizilimi)

        kaydirma = QScrollArea()
        kaydirma.setWidgetResizable(True)
        kaydirma.setWidget(grup_kutu)
        kaydirma.setFixedHeight(180)

        self.buton_listele = QPushButton("Filmleri Listele")
        self.buton_listele.clicked.connect(self.filmleri_listele)

        self.tablo = QTableWidget()
        self.tablo.setColumnCount(3)
        self.tablo.setHorizontalHeaderLabels(["Film Adı", "Yıl", "IMDB"])

        self.etiket_ortalama = QLabel("Ortalama IMDB: -")
        self.etiket_medyan = QLabel("Medyan IMDB: -")

        duzen = QVBoxLayout()
        duzen.addWidget(QLabel("Minimum Yıl:"))
        duzen.addWidget(self.giris_yil)
        duzen.addWidget(QLabel("Minimum IMDB:"))
        duzen.addWidget(self.giris_puan)
        duzen.addWidget(kaydirma)
        duzen.addWidget(self.buton_listele)
        duzen.addWidget(self.tablo)
        duzen.addWidget(self.etiket_ortalama)
        duzen.addWidget(self.etiket_medyan)

        self.setLayout(duzen)

    def filmleri_listele(self):
        try:
            yil = int(self.giris_yil.text())
            puan = float(self.giris_puan.text())
        except ValueError:
            self.etiket_ortalama.setText("Ortalama IMDB: -")
            self.etiket_medyan.setText("Medyan IMDB: -")
            self.tablo.setRowCount(0)
            QMessageBox.warning(self, "Geçersiz Giriş", "Lütfen geçerli bir yıl ve IMDB puanı girin.")
            return

        secilen_turler = [kutu.text() for kutu in self.tur_kutulari if kutu.isChecked()]
        if not secilen_turler:
            self.etiket_ortalama.setText("Ortalama IMDB: -")
            self.etiket_medyan.setText("Medyan IMDB: -")
            self.tablo.setRowCount(0)
            QMessageBox.information(self, "Tür Seçilmedi", "Lütfen en az bir tür seçiniz.")
            return

        filtrelenmis = veri[(veri["year"] >= yil) & (veri["imdb_score"] >= puan)]
        for tur in secilen_turler:
            sutun_adi = f"genres_{tur}"
            if sutun_adi in filtrelenmis.columns:
                filtrelenmis = filtrelenmis[filtrelenmis[sutun_adi] == 1]

        self.tablo.setRowCount(0)
        for _, satir in filtrelenmis.iterrows():
            sira = self.tablo.rowCount()
            self.tablo.insertRow(sira)
            self.tablo.setItem(sira, 0, QTableWidgetItem(str(satir["title"])))
            self.tablo.setItem(sira, 1, QTableWidgetItem(str(satir["year"])))
            self.tablo.setItem(sira, 2, QTableWidgetItem(str(satir["imdb_score"])))

        if not filtrelenmis.empty:
            ortalama = round(filtrelenmis["imdb_score"].mean(), 2)
            medyan = round(filtrelenmis["imdb_score"].median(), 2)
            self.etiket_ortalama.setText(f"Ortalama IMDB: {ortalama}")
            self.etiket_medyan.setText(f"Medyan IMDB: {medyan}")
        else:
            self.etiket_ortalama.setText("Ortalama IMDB: -")
            self.etiket_medyan.setText("Medyan IMDB: -")
            QMessageBox.information(self, "Sonuç Yok", "Filtreye uyan film bulunamadı.")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = FilmOneriUygulamasi()
    pencere.show()
    sys.exit(uygulama.exec_())
