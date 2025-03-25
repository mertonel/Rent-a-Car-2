# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musteri.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_musteri(object):
    def setupUi(self, musteri):
        if not musteri.objectName():
            musteri.setObjectName(u"musteri")
        musteri.resize(637, 431)
        self.pushButton = QPushButton(musteri)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 310, 181, 51))
        self.pushButton.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_11 = QLabel(musteri)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(230, 30, 151, 31))
        self.label_11.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(0, 0, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(musteri)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(330, 100, 234, 148))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditTelefon = QLineEdit(self.layoutWidget)
        self.lineEditTelefon.setObjectName(u"lineEditTelefon")

        self.verticalLayout_2.addWidget(self.lineEditTelefon)

        self.lineEditMeslek = QLineEdit(self.layoutWidget)
        self.lineEditMeslek.setObjectName(u"lineEditMeslek")

        self.verticalLayout_2.addWidget(self.lineEditMeslek)

        self.lineEditEhliyet = QLineEdit(self.layoutWidget)
        self.lineEditEhliyet.setObjectName(u"lineEditEhliyet")

        self.verticalLayout_2.addWidget(self.lineEditEhliyet)

        self.lineEditMedeni = QLineEdit(self.layoutWidget)
        self.lineEditMedeni.setObjectName(u"lineEditMedeni")

        self.verticalLayout_2.addWidget(self.lineEditMedeni)

        self.lineEditEgitim = QLineEdit(self.layoutWidget)
        self.lineEditEgitim.setObjectName(u"lineEditEgitim")

        self.verticalLayout_2.addWidget(self.lineEditEgitim)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.layoutWidget1 = QWidget(musteri)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(83, 103, 221, 149))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEditTc = QLineEdit(self.layoutWidget1)
        self.lineEditTc.setObjectName(u"lineEditTc")

        self.verticalLayout_3.addWidget(self.lineEditTc)

        self.lineEditAd = QLineEdit(self.layoutWidget1)
        self.lineEditAd.setObjectName(u"lineEditAd")

        self.verticalLayout_3.addWidget(self.lineEditAd)

        self.lineEditSoyad = QLineEdit(self.layoutWidget1)
        self.lineEditSoyad.setObjectName(u"lineEditSoyad")

        self.verticalLayout_3.addWidget(self.lineEditSoyad)

        self.dateEditDogum = QDateEdit(self.layoutWidget1)
        self.dateEditDogum.setObjectName(u"dateEditDogum")

        self.verticalLayout_3.addWidget(self.dateEditDogum)

        self.lineEditAdres = QLineEdit(self.layoutWidget1)
        self.lineEditAdres.setObjectName(u"lineEditAdres")

        self.verticalLayout_3.addWidget(self.lineEditAdres)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(musteri)

        QMetaObject.connectSlotsByName(musteri)
    # setupUi

    def retranslateUi(self, musteri):
        musteri.setWindowTitle(QCoreApplication.translate("musteri", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("musteri", u"Kaydet", None))
        self.label_11.setText(QCoreApplication.translate("musteri", u"M\u00fc\u015fteri Ekle", None))
        self.label_5.setText(QCoreApplication.translate("musteri", u"Telefon", None))
        self.label_7.setText(QCoreApplication.translate("musteri", u"Meslek", None))
        self.label_8.setText(QCoreApplication.translate("musteri", u"Ehliyet Bilgileri", None))
        self.label_9.setText(QCoreApplication.translate("musteri", u"Medeni Durum", None))
        self.label_10.setText(QCoreApplication.translate("musteri", u"E\u011fitim Durumu", None))
        self.label_3.setText(QCoreApplication.translate("musteri", u"TC kimlik no", None))
        self.label.setText(QCoreApplication.translate("musteri", u"Ad", None))
        self.label_2.setText(QCoreApplication.translate("musteri", u"Soyad", None))
        self.label_4.setText(QCoreApplication.translate("musteri", u"Do\u011fum Tarihi", None))
        self.label_6.setText(QCoreApplication.translate("musteri", u"Adres", None))
    # retranslateUi

