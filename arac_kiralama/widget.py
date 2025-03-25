import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from ui_form import Ui_Widget
from ui_musteri import Ui_musteri
from ui_araclar import Ui_Form as Ui_Araclar
from ui_kiralama import Ui_Form as Ui_Kiralama
from ui_kiradaolanlar import Ui_Form as Ui_KiradaOlanlar

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Araç Kiralama Sistemi")
        self.setBackgroundImage("resim4.png")
        self.sql_baglan()
        self.db_check()

        self.ui.pushButton.clicked.connect(self.open_musteri)
        self.ui.pushButton_2.clicked.connect(self.open_araclar)
        self.ui.pushButton_3.clicked.connect(self.open_kiralama)
        self.ui.pushButton_4.clicked.connect(self.open_kirada_olanlar)

    def setBackgroundImage(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.width() * 0.8,
            self.height() * 0.5,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)
        self.setPalette(palette)

        label = QLabel(self)
        label.setPixmap(scaled_pixmap)
        label.setGeometry(
            (self.width() - scaled_pixmap.width()) // 2,
            (self.height() - scaled_pixmap.height()) // 2,
            scaled_pixmap.width(),
            scaled_pixmap.height()
        )
        label.setScaledContents(True)
        label.setStyleSheet("background-color: transparent;")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setBackgroundImage("resim4.png")

    def sql_baglan(self):
        try:
            self.db_conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="deneme",
                port=3306
            )
            self.cursor = self.db_conn.cursor()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"MySQL bağlantı hatası: {err}")
            sys.exit()

    def db_check(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS db90230000260")
        self.cursor.execute("USE db90230000260")

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS musteri (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ad VARCHAR(50),
                soyad VARCHAR(50),
                tc_kimlik VARCHAR(11),
                dogum_tarihi DATE,
                adres TEXT,
                telefon VARCHAR(15),
                meslek VARCHAR(50),
                ehliyet_sinifi VARCHAR(5),
                medeni_durum VARCHAR(10),
                egitim_durumu VARCHAR(20)
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS arac (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tur VARCHAR(20),
                marka VARCHAR(50),
                model VARCHAR(50),
                uretim_yili YEAR,
                yakit_turu VARCHAR(20),
                vites VARCHAR(20),
                motor_gucu VARCHAR(20),
                kasa_tipi VARCHAR(20),
                motor_hacmi VARCHAR(20),
                cekis VARCHAR(20),
                kapi INT,
                renk VARCHAR(20),
                motor_no VARCHAR(50),
                sasi_no VARCHAR(50),
                gunluk_kiralama_bedeli DECIMAL(10,2),
                kirada_mi BOOLEAN DEFAULT FALSE,
                kullanim_disi BOOLEAN DEFAULT FALSE
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS kiralama (
                id INT AUTO_INCREMENT PRIMARY KEY,
                musteri_id INT,  -- Müşteri ile ilişkilendirme
                arac_id INT,     -- Araç ile ilişkilendirme
                ad VARCHAR(11),  -- Müşterinin TC Kimlik Numarası
                arac_model VARCHAR(20),  -- Araç şasi numarası
                kiralama_tarihi DATE,  -- Kiralama tarihi
                kiralama_gun INT,      -- Kiralanan gün sayısı
                yolculuk_yeri TEXT,    -- Yolculuk yeri
                FOREIGN KEY (musteri_id) REFERENCES musteri(id),
                FOREIGN KEY (arac_id) REFERENCES arac(id)
            )
            """
        )


    def open_musteri(self):
        self.musteri_window = Musteri(self)
        self.musteri_window.show()

    def open_araclar(self):
        self.araclar_window = Araclar(self)
        self.araclar_window.show()

    def open_kiralama(self):
        self.kiralama_window = Kiralama(self)
        self.kiralama_window.show()

    def open_kirada_olanlar(self):
        self.kirada_olanlar_window = KiradaOlanlar(self)
        self.kirada_olanlar_window.show()

class Musteri(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_musteri()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow
        self.ui.pushButton.clicked.connect(self.save_musteri)

    def save_musteri(self):
        ad = self.ui.lineEditAd.text()
        soyad = self.ui.lineEditSoyad.text()
        tc_kimlik = self.ui.lineEditTc.text()
        dogum_tarihi = self.ui.dateEditDogum.date().toString("yyyy-MM-dd")
        adres = self.ui.lineEditAdres.text()
        telefon = self.ui.lineEditTelefon.text()
        meslek = self.ui.lineEditMeslek.text()
        ehliyet_sinifi = self.ui.lineEditEhliyet.text()
        medeni_durum = self.ui.lineEditMedeni.text()
        egitim_durumu = self.ui.lineEditEgitim.text()

        try:
            cursor = self.mainWindow.db_conn.cursor()
            cursor.execute(
                "INSERT INTO musteri (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu)
            )
            self.mainWindow.db_conn.commit()
            QMessageBox.information(self, "Başarılı", "Müşteri kaydı başarıyla eklendi.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"MySQL Hatası: {err}")

class Araclar(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_Araclar()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow
        self.ui.pushButton.clicked.connect(self.save_arac)

    def save_arac(self):
        tur = self.ui.lineEditTur.text()
        marka = self.ui.lineEditMarka.text()
        model = self.ui.lineEditModel.text()
        uretim_yili = self.ui.lineEditUretimYili.text()
        yakit_turu = self.ui.lineEditYakit.text()
        vites = self.ui.lineEditVites.text()
        motor_gucu = self.ui.lineEditMotorGucu.text()
        kasa_tipi = self.ui.lineEditKasaTipi.text()
        motor_hacmi = self.ui.lineEditMotorHacmi.text()
        kapi = self.ui.lineEditKapi.text()
        renk = self.ui.lineEditRenk.text()
        motor_no = self.ui.lineEditMotorNo.text()
        sasi_no = self.ui.lineEditSasiNo.text()
        gunluk_kiralama_bedeli = self.ui.lineEditGunlukBedel.text()

        try:
            cursor = self.mainWindow.db_conn.cursor()
            cursor.execute(
                """
                INSERT INTO arac
                (tur, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, kasa_tipi, motor_hacmi, kapi, renk, motor_no, sasi_no, gunluk_kiralama_bedeli)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (tur, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, kasa_tipi, motor_hacmi, kapi, renk, motor_no, sasi_no, gunluk_kiralama_bedeli)
            )
            self.mainWindow.db_conn.commit()
            QMessageBox.information(self, "Başarılı", "Araç kaydı başarıyla eklendi.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"MySQL Hatası: {err}")

class Kiralama(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_Kiralama()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow
        self.load_musteri_data()
        self.load_arac_data()
        self.ui.pushButton.clicked.connect(self.save_kiralama)

    def load_musteri_data(self):
        cursor = self.mainWindow.db_conn.cursor()
        cursor.execute("SELECT id, ad, soyad FROM musteri")
        musteri_data = cursor.fetchall()

        for musteri in musteri_data:
            self.ui.comboBoxTc.addItem(f"{musteri[1]} {musteri[2]}", musteri[0])

    def load_arac_data(self):
        cursor = self.mainWindow.db_conn.cursor()
        cursor.execute("SELECT id, marka, model FROM arac WHERE kirada_mi = FALSE AND kullanim_disi = FALSE")
        arac_data = cursor.fetchall()

        for arac in arac_data:
            self.ui.comboBoxArac.addItem(f"{arac[1]} {arac[2]}", arac[0])

    def save_kiralama(self):

        musteri_id = self.ui.comboBoxTc.currentData()
        arac_id = self.ui.comboBoxArac.currentData()

        kiralama_gun = self.ui.spinBox.value()
        gidis_yeri = self.ui.lineEdit.text()
        baslangic_tarihi = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        try:
            cursor = self.mainWindow.db_conn.cursor()
            cursor.execute(
                """
                INSERT INTO kiralama (musteri_id, arac_id, kiralama_gun, yolculuk_yeri, kiralama_tarihi)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (musteri_id, arac_id, kiralama_gun, gidis_yeri, baslangic_tarihi)
            )

            cursor.execute(
                """
                UPDATE arac
                SET kirada_mi = TRUE
                WHERE id = %s
                """,
                (arac_id,)
            )

            self.mainWindow.db_conn.commit()

            QMessageBox.information(self, "Başarılı", "Kiralama işlemi başarıyla kaydedildi.")
            self.close()  # Kiralama formunu kapat

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"MySQL Hatası: {err}")


class KiradaOlanlar(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_KiradaOlanlar()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow


        self.load_kirada_olanlar()

    def load_kirada_olanlar(self):
        try:
            cursor = self.mainWindow.db_conn.cursor()
            cursor.execute(
                """
                SELECT
                    kiralama.id,
                    musteri.ad,
                    musteri.soyad,
                    arac.marka,
                    arac.model,
                    kiralama.kiralama_tarihi,
                    DATE_ADD(kiralama.kiralama_tarihi, INTERVAL kiralama.kiralama_gun DAY) AS kira_bitis_tarihi
                FROM kiralama
                JOIN musteri ON kiralama.musteri_id = musteri.id
                JOIN arac ON kiralama.arac_id = arac.id
                WHERE arac.kirada_mi = TRUE
                """
            )

            kirada_olanlar = cursor.fetchall()


            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(len(kirada_olanlar))


            for row_index, row_data in enumerate(kirada_olanlar):
                for column_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row_index, column_index, item)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"MySQL Hatası: {err}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
