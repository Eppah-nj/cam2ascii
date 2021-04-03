# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appWindowBwlBcO.ui'
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


class Ui_Cam2ascii(object):
    def setupUi(self, Cam2ascii):
        if Cam2ascii.objectName():
            Cam2ascii.setObjectName(u"Cam2ascii")
        Cam2ascii.resize(1280, 720)
        Cam2ascii.setMinimumSize(QSize(1280, 720))
        Cam2ascii.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(Cam2ascii)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appFrame = QFrame(self.centralwidget)
        self.appFrame.setObjectName(u"appFrame")
        self.appFrame.setGeometry(QRect(0, 0, 480, 720))
        self.appFrame.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(47, 47, 47);\n"
"	color: white;\n"
"}")
        self.appFrame.setFrameShape(QFrame.NoFrame)
        self.appFrame.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.appFrame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 481, 51))
        font = QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setMargin(10)
        self.methodsComboBox = QComboBox(self.appFrame)
        self.methodsComboBox.setObjectName(u"methodsComboBox")
        self.methodsComboBox.setGeometry(QRect(65, 170, 350, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.methodsComboBox.setFont(font1)
        self.methodsComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.methodsComboBox.setMouseTracking(False)
        self.methodsComboBox.setStyleSheet(u"QComboBox {\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	text-align: center;\n"
"	padding: 0 15px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	width:20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"      border: 2px solid red;\n"
"      selection-background-color: blue;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"      border: 2px solid darkgray;\n"
"}\n"
"")
        self.methodsComboBox.setEditable(False)
        self.methodsComboBox.setFrame(True)
        self.methodsLabel = QLabel(self.appFrame)
        self.methodsLabel.setObjectName(u"methodsLabel")
        self.methodsLabel.setGeometry(QRect(0, 120, 181, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.methodsLabel.setFont(font2)
        self.methodsLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.methodsLabel.setAlignment(Qt.AlignCenter)
        self.methodsLabel.setMargin(2)
        self.charListLabel = QLabel(self.appFrame)
        self.charListLabel.setObjectName(u"charListLabel")
        self.charListLabel.setGeometry(QRect(0, 230, 181, 31))
        self.charListLabel.setFont(font2)
        self.charListLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.charListLabel.setAlignment(Qt.AlignCenter)
        self.charListLabel.setMargin(2)
        self.charListComboBox = QComboBox(self.appFrame)
        self.charListComboBox.setObjectName(u"charListComboBox")
        self.charListComboBox.setGeometry(QRect(65, 280, 350, 40))
        self.charListComboBox.setFont(font1)
        self.charListComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.charListComboBox.setMouseTracking(False)
        self.charListComboBox.setStyleSheet(u"QComboBox {\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	text-align: center;\n"
"	padding: 0 15px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	width:20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"      border: 2px solid red;\n"
"      selection-background-color: blue;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"      border: 2px solid darkgray;\n"
"}\n"
"")
        self.charListComboBox.setEditable(False)
        self.charListComboBox.setCurrentText(u"")
        self.charListComboBox.setFrame(True)
        self.lineEditCharList = QLineEdit(self.appFrame)
        self.lineEditCharList.setObjectName(u"lineEditCharList")
        self.lineEditCharList.setGeometry(QRect(65, 340, 300, 40))
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEditCharList.setFont(font3)
        self.lineEditCharList.setStyleSheet(u"QLineEdit{\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	text-align: center;\n"
"	padding: 0 15px;\n"
"}")
        self.addCharList = QPushButton(self.appFrame)
        self.addCharList.setObjectName(u"addCharList")
        self.addCharList.setGeometry(QRect(375, 340, 40, 40))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.addCharList.setFont(font4)
        self.addCharList.setCursor(QCursor(Qt.PointingHandCursor))
        self.addCharList.setStyleSheet(u"QPushButton {\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	text-align: center;\n"
"	border-radius:4px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	\n"
"	\n"
"	background-color: rgb(98, 98, 98);\n"
"}")
        self.optionsLabel = QLabel(self.appFrame)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setGeometry(QRect(0, 400, 181, 31))
        self.optionsLabel.setFont(font2)
        self.optionsLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.optionsLabel.setAlignment(Qt.AlignCenter)
        self.optionsLabel.setMargin(2)
        self.horRezSlider = QSlider(self.appFrame)
        self.horRezSlider.setObjectName(u"horRezSlider")
        self.horRezSlider.setGeometry(QRect(170, 450, 245, 20))
        font5 = QFont()
        font5.setPointSize(8)
        self.horRezSlider.setFont(font5)
        self.horRezSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horRezSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color:rgb(80, 80, 80);\n"
"	height: 10px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(135, 135, 135);\n"
"	width: 8px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 4px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	background-color: white;\n"
"}")
        self.horRezSlider.setMinimum(1)
        self.horRezSlider.setMaximum(266)
        self.horRezSlider.setSliderPosition(80)
        self.horRezSlider.setOrientation(Qt.Horizontal)
        self.horRezLabel = QLabel(self.appFrame)
        self.horRezLabel.setObjectName(u"horRezLabel")
        self.horRezLabel.setGeometry(QRect(50, 450, 110, 20))
        font6 = QFont()
        font6.setPointSize(12)
        self.horRezLabel.setFont(font6)
        self.horRezLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.horRezLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horRezLabel.setMargin(2)
        self.fpsSpinBox = QSpinBox(self.appFrame)
        self.fpsSpinBox.setObjectName(u"fpsSpinBox")
        self.fpsSpinBox.setGeometry(QRect(170, 490, 71, 20))
        self.fpsSpinBox.setStyleSheet(u"QSpinBox{\n"
"	border-style: none;\n"
"	background-color: rgb(80, 80, 80);\n"
"	color:white;\n"
"	padding:0 5px;\n"
"	\n"
"}")
        self.fpsSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.fpsSpinBox.setValue(20)
        self.fpsLabel = QLabel(self.appFrame)
        self.fpsLabel.setObjectName(u"fpsLabel")
        self.fpsLabel.setGeometry(QRect(50, 490, 110, 20))
        self.fpsLabel.setFont(font6)
        self.fpsLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.fpsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fpsLabel.setMargin(2)
        self.mirrorCheckBox = QCheckBox(self.appFrame)
        self.mirrorCheckBox.setObjectName(u"mirrorCheckBox")
        self.mirrorCheckBox.setGeometry(QRect(170, 530, 70, 20))
        self.mirrorLabel = QLabel(self.appFrame)
        self.mirrorLabel.setObjectName(u"mirrorLabel")
        self.mirrorLabel.setGeometry(QRect(50, 528, 110, 23))
        self.mirrorLabel.setFont(font6)
        self.mirrorLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.mirrorLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mirrorLabel.setMargin(2)
        self.screenAreaFrame = QFrame(self.centralwidget)
        self.screenAreaFrame.setObjectName(u"screenAreaFrame")
        self.screenAreaFrame.setGeometry(QRect(480, 0, 800, 720))
        self.screenAreaFrame.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"	color:white;\n"
"}")
        self.screenAreaFrame.setFrameShape(QFrame.StyledPanel)
        self.screenAreaFrame.setFrameShadow(QFrame.Raised)
        self.screenArea = QLabel(self.screenAreaFrame)
        self.screenArea.setObjectName(u"screenArea")
        self.screenArea.setGeometry(QRect(0, 0, 800, 720))
        self.screenArea.setFont(font5)
        self.screenArea.setAlignment(Qt.AlignCenter)
        self.screenArea.setMargin(2)
        self.printInfoLabel = QLabel(self.screenAreaFrame)
        self.printInfoLabel.setObjectName(u"printInfoLabel")
        self.printInfoLabel.setGeometry(QRect(0, 700, 800, 20))
        self.printInfoLabel.setFont(font3)
        self.printInfoLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        Cam2ascii.setCentralWidget(self.centralwidget)
        self.screenAreaFrame.raise_()
        self.appFrame.raise_()

        self.retranslateUi(Cam2ascii)

        QMetaObject.connectSlotsByName(Cam2ascii)
    # setupUi

    def retranslateUi(self, Cam2ascii):
        Cam2ascii.setWindowTitle(QCoreApplication.translate("Cam2ascii", u"Cam2ascii", None))
        self.title.setText(QCoreApplication.translate("Cam2ascii", u"$> <strong>CAM</strong>2ascii", None))
        self.methodsComboBox.setCurrentText("")
        self.methodsLabel.setText(QCoreApplication.translate("Cam2ascii", u"<html><head/><body><p>$&gt; Methods_</p></body></html>", None))
        self.charListLabel.setText(QCoreApplication.translate("Cam2ascii", u"<html><head/><body><p>$&gt; Char list_</p></body></html>", None))
        self.addCharList.setText(QCoreApplication.translate("Cam2ascii", u"ADD", None))
        self.optionsLabel.setText(QCoreApplication.translate("Cam2ascii", u"$> Options_", None))
        self.horRezLabel.setText(QCoreApplication.translate("Cam2ascii", u"Resolution", None))
        self.fpsLabel.setText(QCoreApplication.translate("Cam2ascii", u"Frame rate", None))
        self.mirrorCheckBox.setText("")
        self.mirrorLabel.setText(QCoreApplication.translate("Cam2ascii", u"Mirror image", None))
        self.screenArea.setText("")
        self.printInfoLabel.setText("")
    # retranslateUi

