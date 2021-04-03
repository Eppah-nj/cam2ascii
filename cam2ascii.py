# -*- coding: utf-8 -*-
import math
import cv2
import numpy as np
import json
import os

import unicodedata

SETUPFILE = "setup.json"


class ParsingError(Exception):
    def __init__(self, value, message="Erro while parsing the setup json file"):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'

class Cam2ascii:
    def __init__(self, camera=0):
        super().__init__()
        self.camera = camera
        self.parseJson()
        self.startCaptupe()
    
    def getValueFromDict(self, dict, toGet, message):
        if toGet in dict:
            return dict[toGet]
        else :
            raise ParsingError(toGet, message)

    def parseJson(self):
        global SETUPFILE
        if os.path.isfile(SETUPFILE):
            with open(SETUPFILE) as jsonFile:
                data = json.load(jsonFile)
                self.asciiScale = self.getValueFromDict(data, 'asciiScale', "Value not found in json")
                self.selector = self.getValueFromDict(data, 'baseSelector', "Value not found in json")
                self.constScale = 256 / (len(self.asciiScale[self.selector]) - 1)
                reso = self.getValueFromDict(data, 'resolution', "Value not found in json")
                self.horizontalResolution = self.getValueFromDict(reso, 'hor', "Value not found in json")
                self.verticalResolution = self.getValueFromDict(reso, 'ver', "Value not found in json")
                self.displayMode = self.getValueFromDict(data, 'defaultMethod', "Value not found in json")
                self.methods = self.getValueFromDict(data, 'methods', "Value not found in json")
                self.mirror = self.getValueFromDict(data, 'mirror', "Value not found in json")
        else:
            raise FileNotFoundError("setupfile not found")

    def startCaptupe(self):
        self.camCapture = cv2.VideoCapture(self.camera)
        self.refreshFrame()

    def refreshFrame(self):
        
        if self.camCapture.isOpened():
            self.status, self.frame = self.camCapture.read()
            if self.mirror:
                self.frame = cv2.flip(self.frame, 1)
        else:
            self.status = False

    def getGrayScale(self):
        return cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def methodGrayScale(self, displayMethod):
        self.frame = self.getGrayScale()
        self.basicDisplay()
        txt = self.encodeToHtml(self.frameTxt).replace("\n", "<br>")
        displayMethod("<tt>" + str(txt) + "</tt>")

    def methodTerminal(self, displayMethod):
        self.frame = self.getGrayScale()
        self.basicDisplay()
        print(self.frameTxt)

    def methodGreenChannel(self, displayMethod):
        self.frame = self.frame[:, :, 1]
        self.basicDisplay()
        txt = self.encodeToHtml(self.frameTxt).replace("\n", "<br>")
        displayMethod("<tt style='color:green'>" + str(txt) + "</tt>")

    def methodRedChannel(self, displayMethod):
        self.frame = self.frame[:, :, 2]
        self.basicDisplay()
        txt = self.encodeToHtml(self.frameTxt).replace("\n", "<br>")
        displayMethod("<tt style='color:red'>" + str(txt) + "</tt>")

    def methodBlueChannel(self, displayMethod):
        self.frame = self.frame[:, :, 0]
        self.basicDisplay()
        txt = self.encodeToHtml(self.frameTxt).replace("\n", "<br>")
        displayMethod("<tt style='color:blue'>" + str(txt) + "</tt>")

    def encodeToHtml(self, txt):
        txt = txt.replace("&", "&amp;")
        txt = txt.replace("<", "&lt;")
        txt = txt.replace(">", "&gt;")
        txt = txt.replace(" ", "&nbsp;")
        return txt

    def displayFrame(self, displayMethod):
        if self.displayMode == "Gray scale":
            self.methodGrayScale(displayMethod)
        elif self.displayMode == "Terminal":
            self.methodTerminal(displayMethod)
        elif self.displayMode == "Red channel":
            self.methodRedChannel(displayMethod)
        elif self.displayMode == "Blue channel":
            self.methodBlueChannel(displayMethod)
        elif self.displayMode == "Green channel":
            self.methodGreenChannel(displayMethod)
        else :
            self.methodTerminal(displayMethod)

    def basicDisplay(self):
        height, width = self.frame.shape
        nbcol = self.horizontalResolution
        cellWidth = width / self.horizontalResolution
        cellheight = cellWidth * 2
        nbrow = int(height / cellheight)
        res = ""
        for y in range(nbrow):
            for x in range(nbcol):
                pix = np.mean(self.frame[int(y * cellheight):min(int((y + 1) * cellheight), height), int(x * cellWidth):min(int((x + 1) * cellWidth), width)])
                res += self.asciiScale[self.selector][int(round(pix / self.constScale))]
            res += "\n"
        self.frameTxt = res

    def changeHorizontalResolution(self, value):
        self.horizontalResolution = int(value)

    def changeVerticalResolution(self, value):
        self.verticalResolution = int(value)

    def changeMethod(self, value):
        self.displayMode = str(value)

    def changeSelector(self, value):
        self.selector = int(value)
        self.constScale = 256 / (len(self.asciiScale[self.selector]) - 1)

    def addAsciiScale(self, value):
        self.asciiScale.append(str(value))

    def saveJson(self):
        global SETUPFILE
        data = {}
        data["asciiScale"] = self.asciiScale
        data["baseSelector"] = self.selector
        data["resolution"] = {"hor":self.horizontalResolution, "ver":self.verticalResolution}
        data["methods"] = self.methods
        data["defaultMethod"] = self.displayMode
        data["mirror"] = self.mirror

        with open(SETUPFILE, "w") as f:
            f.write(json.dumps(data, indent=4, sort_keys=True))

    def __del__(self):
        try :
            self.camCapture.release()
            self.saveJson()
        except:
            pass
        cv2.destroyAllWindows()


if __name__ == "__main__":
    cam = Cam2ascii()
    try:
        while cam.status:
            cam.refreshFrame()
            cam.displayFrame()
            key = cv2.waitKey(50)
            if key == 27:
                break

    except KeyboardInterrupt: 
        pass