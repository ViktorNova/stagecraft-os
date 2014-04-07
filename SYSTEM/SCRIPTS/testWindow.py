#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore
from subprocess import call
cmd = 'echo you pressed it yo'
cmd2 = 'aj-snapshot -f ~/SYSTEM/GLOBAL/GLOBAL-MIDI-ROUTING.xml'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def buttonClicked(self):
        os.system(cmd)
        os.system(cmd2)
        QtCore.QCoreApplication.instance().quit()

    def initUI(self):


	btn = QtGui.QPushButton('Save global MIDI routing', self)     
	btn.clicked.connect(self.buttonClicked)
        btn.resize(280, 60)
        btn.move(0, 0) 

        qbtn = QtGui.QPushButton('CANCEL', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(280, 60)
        qbtn.move(300, 0)

        self.setWindowTitle('GLOBAL MIDI ROUTING')    
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

