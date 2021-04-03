# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowWYIqrE.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CAM2ascii(object):
    def setupUi(self, CAM2ascii):
        if CAM2ascii.objectName():
            CAM2ascii.setObjectName(u"CAM2ascii")
        CAM2ascii.resize(1280, 720)
        CAM2ascii.setMinimumSize(QSize(1280, 720))
        CAM2ascii.setMaximumSize(QSize(1280, 720))
        CAM2ascii.setWindowTitle(u"CAM2ascii")
        self.centralwidget = QWidget(CAM2ascii)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadingMenuFrame = QFrame(self.centralwidget)
        self.loadingMenuFrame.setObjectName(u"loadingMenuFrame")
        self.loadingMenuFrame.setGeometry(QRect(-1, -1, 1281, 721))
        self.loadingMenuFrame.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(47, 47, 47);\n"
"	color: white\n"
"}")
        self.loadingMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.loadingMenuFrame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.loadingMenuFrame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 150, 1281, 121))
        font = QFont()
        font.setPointSize(40)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.loadingMenuFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(280, 460, 720, 31))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border-radius : 10px;\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius : 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.512, x2:1, y2:0.579227, stop:0 rgba(0, 153, 102, 255), stop:1 rgba(0, 104, 69, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.author = QLabel(self.loadingMenuFrame)
        self.author.setObjectName(u"author")
        self.author.setGeometry(QRect(1130, 700, 151, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.author.setFont(font1)
        self.author.setStyleSheet(u"QLabel {\n"
"	color:white\n"
"}")
        self.author.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.author.setMargin(2)
        CAM2ascii.setCentralWidget(self.centralwidget)

        self.retranslateUi(CAM2ascii)

        QMetaObject.connectSlotsByName(CAM2ascii)
    # setupUi

    def retranslateUi(self, CAM2ascii):
        self.title.setText(QCoreApplication.translate("CAM2ascii", u"$> _", None))
        self.author.setText(QCoreApplication.translate("CAM2ascii", u"Made by Eppah", None))
    # retranslateUi

