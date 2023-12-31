# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\Add_product.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_product(object):
    def setupUi(self, Add_product):
        Add_product.setObjectName("Add_product")
        Add_product.resize(1200, 720)
        Add_product.setMaximumSize(QtCore.QSize(1280, 720))
        Add_product.setStyleSheet("background-color: rgb(255, 248, 225);")
        self.centralwidget = QtWidgets.QWidget(Add_product)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(1280, 720))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(700, 300))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_input = QtWidgets.QLineEdit(self.frame_4)
        self.name_input.setMaximumSize(QtCore.QSize(700, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 127);\n"
"boeder:none;\n"
"border-bottom:3px solid rgba(255, 0, 127, 255);\n"
"padding-bottom:7px;\n"
"border-radius:0px")
        self.name_input.setObjectName("name_input")
        self.verticalLayout_2.addWidget(self.name_input)
        self.barcode_input = QtWidgets.QLineEdit(self.frame_4)
        self.barcode_input.setMaximumSize(QtCore.QSize(700, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.barcode_input.setFont(font)
        self.barcode_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 127);\n"
"boeder:none;\n"
"border-bottom:3px solid rgba(255, 0, 127, 255);\n"
"padding-bottom:7px;\n"
"border-radius:0px")
        self.barcode_input.setObjectName("barcode_input")
        self.verticalLayout_2.addWidget(self.barcode_input)
        self.price_input = QtWidgets.QLineEdit(self.frame_4)
        self.price_input.setMaximumSize(QtCore.QSize(700, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.price_input.setFont(font)
        self.price_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 127);\n"
"boeder:none;\n"
"border-bottom:3px solid rgba(255, 0, 127, 255);\n"
"padding-bottom:7px;\n"
"border-radius:0px")
        self.price_input.setObjectName("price_input")
        self.verticalLayout_2.addWidget(self.price_input)
        self.quantity_input = QtWidgets.QLineEdit(self.frame_4)
        self.quantity_input.setMaximumSize(QtCore.QSize(700, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quantity_input.setFont(font)
        self.quantity_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 127);\n"
"boeder:none;\n"
"border-bottom:3px solid rgba(255, 0, 127, 255);\n"
"padding-bottom:7px;\n"
"border-radius:0px")
        self.quantity_input.setObjectName("quantity_input")
        self.verticalLayout_2.addWidget(self.quantity_input)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(300, 300))
        self.frame_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AddButton = QtWidgets.QPushButton(self.frame_7)
        self.AddButton.setMaximumSize(QtCore.QSize(190, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("QPushButton#AddButton{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(255, 201, 255, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#AddButton:hover{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(225, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton#AddButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"\n"
"}\n"
"")
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout_4.addWidget(self.AddButton)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LoadButton = QtWidgets.QPushButton(self.frame_6)
        self.LoadButton.setMaximumSize(QtCore.QSize(190, 60))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet("QPushButton#LoadButton{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(255, 201, 255, 255));\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#LoadButton:hover{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(225, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton#LoadButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"\n"
"}\n"
"")
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalLayout_3.addWidget(self.LoadButton)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 520))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 0, 127);\n"
"background-color: rgb(220, 220, 220);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(228)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        Add_product.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_product)
        QtCore.QMetaObject.connectSlotsByName(Add_product)

    def retranslateUi(self, Add_product):
        _translate = QtCore.QCoreApplication.translate
        Add_product.setWindowTitle(_translate("Add_product", "MainWindow"))
        self.name_input.setPlaceholderText(_translate("Add_product", "Name"))
        self.barcode_input.setPlaceholderText(_translate("Add_product", "Barcode"))
        self.price_input.setPlaceholderText(_translate("Add_product", "Price"))
        self.quantity_input.setPlaceholderText(_translate("Add_product", "Quantity"))
        self.AddButton.setText(_translate("Add_product", "ADD"))
        self.LoadButton.setText(_translate("Add_product", "LOAD"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_product", "Name Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Add_product", "Barcode"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Add_product", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Add_product", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Add_product", "Delete"))
