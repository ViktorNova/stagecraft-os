#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore
from subprocess import call
cmd = 'echo you pressed it yo'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

def buttonClicked(self):
    os.system(cmd)
    QtCore.QCoreApplication.instance().quit()
    def initUI(self):

	btn = QtGui.QPushButton('SAVE GLOBAL MIDI CONFIG', self)     
	btn.clicked.connect(self.buttonClicked)
	btn.resize(180, 40)
        btn.move(20, 35)       

        qbtn = QtGui.QPushButton('CANCEL', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(180, 40)
        qbtn.move(20, 80) 

        self.setWindowTitle('Test')    
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

