# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/nasher/PycharmProjects/discodos/discodos/qt/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1432, 906)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitterVertical = QtWidgets.QSplitter(self.centralwidget)
        self.splitterVertical.setOrientation(QtCore.Qt.Horizontal)
        self.splitterVertical.setObjectName("splitterVertical")
        self.groupBoxMix = QtWidgets.QGroupBox(self.splitterVertical)
        self.groupBoxMix.setObjectName("groupBoxMix")
        self.splitterHorizontal = QtWidgets.QSplitter(self.splitterVertical)
        self.splitterHorizontal.setOrientation(QtCore.Qt.Vertical)
        self.splitterHorizontal.setObjectName("splitterHorizontal")
        self.groupBoxTracks = QtWidgets.QGroupBox(self.splitterHorizontal)
        self.groupBoxTracks.setObjectName("groupBoxTracks")
        self.groupBoxReleases = QtWidgets.QGroupBox(self.splitterHorizontal)
        self.groupBoxReleases.setObjectName("groupBoxReleases")
        self.groupBoxTest = QtWidgets.QGroupBox(self.splitterVertical)
        self.groupBoxTest.setObjectName("groupBoxTest")
        self.gridLayout.addWidget(self.splitterVertical, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1432, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DiscoDOS"))
        self.groupBoxMix.setTitle(_translate("MainWindow", "Mixes"))
        self.groupBoxTracks.setTitle(_translate("MainWindow", "Tracks"))
        self.groupBoxReleases.setTitle(_translate("MainWindow", "Releases"))
        self.groupBoxTest.setTitle(_translate("MainWindow", "Test"))
