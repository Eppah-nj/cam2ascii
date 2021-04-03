# cam2ascii
Cam2ascii is a POC app that convert the camera output to ascii from a specified string. Working on Windows and Linux.

##Installation 
First make sure python3 is installed, also install the package installer for python (`pip`).

###Python libs
Install opencv for the image capture: `pip install opencv-python`
Install Pyqt5 for the GUI: `pip install pyqt5` and `pip install pyqt5-tools`
And make sure PySide2 is installed : `pip install PySide2`

If you want to edit the GUI, install QT Designer: `pip install PyQt5Designer`
QT Designer will be installed "lib/QtDesigner/designer.exe"

##APP

###Methods
This drop down field allows you to choose a method of display:
 - Gray scale : get the picture's gray scaleand displays it in the app
 - Terminal : get the gray scale of the picture and displays it in the terminal
 - Red channel : gets the picture's red channel displays it in the app
 - Green channel : gets the picture's green channel displays it in the app
 - Blue channel : gets the picture's blue channel displays it in the app

###Char list
A char list represent the gradient of a gray scale
The drop down allows you to choose the list you want to render
You can also add your own list (min 3 characters)

###Options
You can change the resolution of the picture, the frame rate, activate the mirror effect.

All the edit while in the app will be saved (new list, resolution, mirror effect, selected methor or list)