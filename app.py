# -*- coding: utf-8 -*-
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QTime, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> UI windows
from GUIfiles.ui_mainWindow import Ui_CAM2ascii
from GUIfiles.ui_appWindow import Ui_Cam2ascii
from cam2ascii import Cam2ascii

## ==> GLOBALS
counter = 0
titleIndex = 0
title = "CAM2ascii"


# SPLASH SCREEN
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CAM2ascii()
        self.ui.setupUi(self)


        ## Start loading Timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.annimIdle = QtCore.QTimer()
        self.annimIdle.timeout.connect(self.annimTitleIdle)
        self.annimIdle.start(500)

        ## display Window
        self.show()

    def txtToString(self, txt):
        doc = QtGui.QTextDocument()
        doc.setHtml(txt)
        return doc.toPlainText()

    def annimTitleIdle(self):
        tmp = self.txtToString(self.ui.title.text())
        if len(tmp) >= 3:
            a = tmp.split("CAM")
            if len(a) == 2:
                tmp = a[0] + "<strong>CAM</strong>" + a[1]
            elif not tmp.endswith('_'):
                a = a[0].split('$> ')[1]
                tmp = "$> <strong>" + a + "</strong>"
        if tmp.endswith('_'):
            self.ui.title.setText(tmp[slice(len(tmp) - 1)])
        else :
            self.ui.title.setText(tmp + "_")

    def displayFullTitle(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.annimFullTitle)
        self.timer.start(35)

    def annimFullTitle(self):
        global titleIndex
        global title

        txt = ""

        if titleIndex >= len(title) + 1:
            self.timer.stop()
            QtCore.QTimer.singleShot(500, lambda:self.startApp())            

            return
        if titleIndex < len(title):
            txt = title[slice(titleIndex)]
        else :
            txt = title
        if titleIndex > 3:
            tmp = txt.split('2')
            txt = tmp[0] + "</strong>2" + tmp[1]
        elif titleIndex <= 3:
            txt += "</strong>"
        self.ui.title.setText("$> <strong>" + txt)
        titleIndex += 1

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.displayFullTitle()
        counter += 1
    
    def startApp(self):
        #stop last annims
        self.annimIdle.stop()

        # init new frame
        self.ui = Ui_Cam2ascii()
        self.ui.setupUi(self)
        self.show()
        #init app functions
        self.cam2ascii = Cam2ascii()

        #filling up fields
        self.fillMethods()
        self.fillCharList()
        self.refreshInfoLabel()

        self.ui.horRezSlider.setValue(self.cam2ascii.horizontalResolution)
        if self.cam2ascii.mirror:
            self.ui.mirrorCheckBox.setChecked(True)

        self.changeResolution(self.cam2ascii.horizontalResolution)

        #connect btn to data
        self.ui.methodsComboBox.currentTextChanged.connect(self.changeMethod)

        self.ui.charListComboBox.currentTextChanged.connect(self.changeCharlist)
        self.ui.fpsSpinBox.valueChanged.connect(self.refreshInfoLabel)

        self.ui.horRezSlider.valueChanged.connect(self.changeResolution)

        self.ui.addCharList.clicked.connect(self.addCharList)

        self.ui.mirrorCheckBox.stateChanged.connect(self.changeStateMirror)

        #start Main loop
        self.mainLoop()

    def mainLoop(self):
        self.refreshImage()
        if self.cam2ascii  and self.cam2ascii.status:
            QtCore.QTimer.singleShot(int(self.ui.fpsSpinBox.value()), lambda:self.mainLoop())

    def refreshImage(self):
        if self.cam2ascii :
            self.cam2ascii.refreshFrame()
            self.cam2ascii.displayFrame(self.ui.screenArea.setText)

    def fillMethods(self):
        for e in self.cam2ascii.methods:
            self.ui.methodsComboBox.addItem(e)
        index = self.ui.methodsComboBox.findText(self.cam2ascii.displayMode, QtCore.Qt.MatchFixedString)
        self.ui.methodsComboBox.setCurrentIndex(index)

    def changeMethod(self, value):
        self.cam2ascii.changeMethod(value)
        self.refreshInfoLabel()
        

    def changeResolution(self, value):
        font = QFont()
        if value >= 159:
            font.setPointSize(4)
        elif value < 159 and value > 113:
            font.setPointSize(7)
        elif value <= 113:
            font.setPointSize(8)
        self.ui.screenArea.setFont(font)
        self.cam2ascii.changeHorizontalResolution(value)
        self.refreshInfoLabel()

    def fillCharList(self):
        for e in self.cam2ascii.asciiScale:
            self.ui.charListComboBox.addItem(e)
        index = self.ui.charListComboBox.findText(self.cam2ascii.asciiScale[self.cam2ascii.selector], QtCore.Qt.MatchFixedString)
        self.ui.charListComboBox.setCurrentIndex(index)

    def changeCharlist(self, value):
        index = self.ui.charListComboBox.findText(value, QtCore.Qt.MatchFixedString)
        self.cam2ascii.changeSelector(index)

    def addCharList(self):
        charList = self.ui.lineEditCharList.text()
        if len(charList) > 2:
            self.ui.charListComboBox.addItem(charList)
            self.cam2ascii.addAsciiScale(charList)
            self.ui.lineEditCharList.clear()

    def refreshInfoLabel(self):
        mirror = ""
        if self.cam2ascii.mirror:
            mirror = "[Mirrored] - "
        method = self.cam2ascii.displayMode
        resolutionX = self.cam2ascii.horizontalResolution

        height = len(self.cam2ascii.frame)
        width = len(self.cam2ascii.frame[0])
        cellheight = (width / self.cam2ascii.horizontalResolution) * 2
        resolutionY = int(height / cellheight)
        fps = self.ui.fpsSpinBox.value()
        
        self.ui.printInfoLabel.setText(mirror + method + " - " + str(resolutionX) + " x " + str(resolutionY) + " (" + str(fps) + ")")
    
    def changeStateMirror(self, value):
        if value == 0:
            value = False
        elif value == 2:
            value = True
        self.cam2ascii.mirror = value
        self.refreshInfoLabel()
 
    def closeEvent(self, event):
        try:
            del self.cam2ascii
        except AttributeError:
            pass
        self.cam2ascii = ""
        self.close()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            try:
                del self.cam2ascii
            except AttributeError:
                pass
            self.cam2ascii = ""
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('imgs/icon.png'))
    window = MainWindow()
    sys.exit(app.exec_())