# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera-viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(5, 11, 640, 480))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 20, 101, 16))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.comboBoxCamera = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCamera.setGeometry(QtCore.QRect(660, 40, 161, 24))
        self.comboBoxCamera.setObjectName("comboBoxCamera")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(660, 80, 161, 28))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(660, 110, 161, 28))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.pushButtonSoftwareTrigger = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButtonSoftwareTrigger.setGeometry(
            QtCore.QRect(660, 160, 161, 28))
        self.pushButtonSoftwareTrigger.setObjectName(
            "pushButtonSoftwareTrigger")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Basler Camera Viewer"))
        self.label.setText(_translate("MainWindow", "Select Camera"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start Grabber"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop Grabber"))
        self.pushButtonSoftwareTrigger.setText(
            _translate("MainWindow", "Software Trigger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())