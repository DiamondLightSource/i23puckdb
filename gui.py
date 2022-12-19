# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1428, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/combipuck.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_scan = QtWidgets.QPushButton(self.centralwidget)
        self.but_scan.setGeometry(QtCore.QRect(30, 20, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.but_scan.setFont(font)
        self.but_scan.setMouseTracking(True)
        self.but_scan.setTabletTracking(True)
        self.but_scan.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.but_scan.setAutoFillBackground(False)
        self.but_scan.setAutoDefault(False)
        self.but_scan.setDefault(False)
        self.but_scan.setFlat(False)
        self.but_scan.setObjectName("but_scan")
        self.lab_avail = QtWidgets.QLabel(self.centralwidget)
        self.lab_avail.setGeometry(QtCore.QRect(520, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lab_avail.setFont(font)
        self.lab_avail.setObjectName("lab_avail")
        self.lab_onloan = QtWidgets.QLabel(self.centralwidget)
        self.lab_onloan.setGeometry(QtCore.QRect(680, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_onloan.setFont(font)
        self.lab_onloan.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_onloan.setObjectName("lab_onloan")
        self.lab_total = QtWidgets.QLabel(self.centralwidget)
        self.lab_total.setGeometry(QtCore.QRect(840, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_total.setFont(font)
        self.lab_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_total.setObjectName("lab_total")
        self.but_locate = QtWidgets.QPushButton(self.centralwidget)
        self.but_locate.setGeometry(QtCore.QRect(30, 340, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.but_locate.setFont(font)
        self.but_locate.setObjectName("but_locate")
        self.lab_I23 = QtWidgets.QLabel(self.centralwidget)
        self.lab_I23.setGeometry(QtCore.QRect(1310, 20, 121, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lab_I23.setFont(font)
        self.lab_I23.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_I23.setObjectName("lab_I23")
        self.lab_RD = QtWidgets.QLabel(self.centralwidget)
        self.lab_RD.setGeometry(QtCore.QRect(1130, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_RD.setFont(font)
        self.lab_RD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_RD.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_RD.setObjectName("lab_RD")
        self.lab_VM = QtWidgets.QLabel(self.centralwidget)
        self.lab_VM.setGeometry(QtCore.QRect(1290, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_VM.setFont(font)
        self.lab_VM.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_VM.setObjectName("lab_VM")
        self.lab_CO = QtWidgets.QLabel(self.centralwidget)
        self.lab_CO.setGeometry(QtCore.QRect(1130, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_CO.setFont(font)
        self.lab_CO.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_CO.setObjectName("lab_CO")
        self.lab_KEO = QtWidgets.QLabel(self.centralwidget)
        self.lab_KEO.setGeometry(QtCore.QRect(1290, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_KEO.setFont(font)
        self.lab_KEO.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_KEO.setObjectName("lab_KEO")
        self.lab_AW = QtWidgets.QLabel(self.centralwidget)
        self.lab_AW.setGeometry(QtCore.QRect(1210, 610, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_AW.setFont(font)
        self.lab_AW.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_AW.setObjectName("lab_AW")
        self.qr_I23 = QtWidgets.QLabel(self.centralwidget)
        self.qr_I23.setGeometry(QtCore.QRect(1140, 20, 161, 161))
        self.qr_I23.setText("")
        self.qr_I23.setPixmap(QtGui.QPixmap("resources/QR_I23.png"))
        self.qr_I23.setScaledContents(True)
        self.qr_I23.setObjectName("qr_I23")
        self.qr_RD = QtWidgets.QLabel(self.centralwidget)
        self.qr_RD.setGeometry(QtCore.QRect(1150, 220, 80, 80))
        self.qr_RD.setText("")
        self.qr_RD.setPixmap(QtGui.QPixmap("resources/QR_RD.png"))
        self.qr_RD.setScaledContents(True)
        self.qr_RD.setObjectName("qr_RD")
        self.qr_VM = QtWidgets.QLabel(self.centralwidget)
        self.qr_VM.setGeometry(QtCore.QRect(1310, 220, 80, 80))
        self.qr_VM.setText("")
        self.qr_VM.setPixmap(QtGui.QPixmap("resources/QR_VM.png"))
        self.qr_VM.setScaledContents(True)
        self.qr_VM.setObjectName("qr_VM")
        self.qr_CO = QtWidgets.QLabel(self.centralwidget)
        self.qr_CO.setGeometry(QtCore.QRect(1150, 380, 80, 80))
        self.qr_CO.setText("")
        self.qr_CO.setPixmap(QtGui.QPixmap("resources/QR_CO.png"))
        self.qr_CO.setScaledContents(True)
        self.qr_CO.setObjectName("qr_CO")
        self.qr_KEO = QtWidgets.QLabel(self.centralwidget)
        self.qr_KEO.setGeometry(QtCore.QRect(1310, 380, 80, 80))
        self.qr_KEO.setText("")
        self.qr_KEO.setPixmap(QtGui.QPixmap("resources/QR_KEO.png"))
        self.qr_KEO.setScaledContents(True)
        self.qr_KEO.setObjectName("qr_KEO")
        self.qr_AW = QtWidgets.QLabel(self.centralwidget)
        self.qr_AW.setGeometry(QtCore.QRect(1230, 530, 80, 80))
        self.qr_AW.setText("")
        self.qr_AW.setPixmap(QtGui.QPixmap("resources/QR_AW.png"))
        self.qr_AW.setScaledContents(True)
        self.qr_AW.setObjectName("qr_AW")
        self.lcdNum_avail = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_avail.setGeometry(QtCore.QRect(513, 72, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNum_avail.setFont(font)
        self.lcdNum_avail.setAutoFillBackground(True)
        self.lcdNum_avail.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNum_avail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNum_avail.setLineWidth(5)
        self.lcdNum_avail.setMidLineWidth(0)
        self.lcdNum_avail.setDigitCount(3)
        self.lcdNum_avail.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNum_avail.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNum_avail.setObjectName("lcdNum_avail")
        self.lcdNum_onloan = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_onloan.setGeometry(QtCore.QRect(670, 70, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNum_onloan.setFont(font)
        self.lcdNum_onloan.setAutoFillBackground(True)
        self.lcdNum_onloan.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNum_onloan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNum_onloan.setLineWidth(5)
        self.lcdNum_onloan.setMidLineWidth(0)
        self.lcdNum_onloan.setDigitCount(3)
        self.lcdNum_onloan.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNum_onloan.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNum_onloan.setObjectName("lcdNum_onloan")
        self.lcdNum_total = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNum_total.setGeometry(QtCore.QRect(830, 70, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNum_total.setFont(font)
        self.lcdNum_total.setAutoFillBackground(True)
        self.lcdNum_total.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNum_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNum_total.setLineWidth(5)
        self.lcdNum_total.setMidLineWidth(0)
        self.lcdNum_total.setDigitCount(3)
        self.lcdNum_total.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNum_total.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNum_total.setObjectName("lcdNum_total")
        self.tableWidget_db = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_db.setGeometry(QtCore.QRect(370, 200, 721, 451))
        self.tableWidget_db.setAlternatingRowColors(True)
        self.tableWidget_db.setObjectName("tableWidget_db")
        self.tableWidget_db.setColumnCount(5)
        self.tableWidget_db.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidget_db.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.but_scan, self.but_locate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_scan.setText(_translate("MainWindow", "SCAN"))
        self.lab_avail.setText(_translate("MainWindow", "Availiable"))
        self.lab_onloan.setText(_translate("MainWindow", "On Loan"))
        self.lab_total.setText(_translate("MainWindow", "Total"))
        self.but_locate.setText(_translate("MainWindow", "LOCATE"))
        self.lab_I23.setText(_translate("MainWindow", "I23"))
        self.lab_RD.setText(_translate("MainWindow", "RD"))
        self.lab_VM.setText(_translate("MainWindow", "VM"))
        self.lab_CO.setText(_translate("MainWindow", "CO"))
        self.lab_KEO.setText(_translate("MainWindow", "KEO"))
        self.lab_AW.setText(_translate("MainWindow", "AW"))
        item = self.tableWidget_db.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Puck ID"))
        item = self.tableWidget_db.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Person"))
        item = self.tableWidget_db.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_db.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget_db.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Remark"))
