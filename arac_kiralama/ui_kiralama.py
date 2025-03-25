# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiralama.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(532, 352)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 181, 21))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(0, 0, 255);")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 60, 341, 211))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 13pt \"Segoe UI\";\n"
"color:rgb(0, 170, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBoxTc = QComboBox(self.layoutWidget)
        self.comboBoxTc.setObjectName(u"comboBoxTc")

        self.verticalLayout.addWidget(self.comboBoxTc)

        self.comboBoxArac = QComboBox(self.layoutWidget)
        self.comboBoxArac.setObjectName(u"comboBoxArac")

        self.verticalLayout.addWidget(self.comboBoxArac)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout.addWidget(self.dateEdit)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout.addWidget(self.spinBox)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 290, 141, 41))
        self.pushButton.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kiralama Ekle", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"M\u00fc\u015fteri", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Ara\u00e7 Model", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Kiralama Tarihi", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ka\u00e7 G\u00fcn", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Yolculuk Yeri", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Kaydet", None))
    # retranslateUi

