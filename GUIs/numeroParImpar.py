# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numeroParImpar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_numeroParImpar(object):
    def setupUi(self, numeroParImpar):
        numeroParImpar.setObjectName("numeroParImpar")
        numeroParImpar.resize(320, 240)
        self.resultParImpar = QtWidgets.QLabel(numeroParImpar)
        self.resultParImpar.setGeometry(QtCore.QRect(40, 170, 249, 34))
        self.resultParImpar.setText("")
        self.resultParImpar.setObjectName("resultParImpar")
        self.layoutWidget = QtWidgets.QWidget(numeroParImpar)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 251, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtNum = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNum.setObjectName("txtNum")
        self.gridLayout.addWidget(self.txtNum, 2, 0, 1, 1)
        self.pbAceptarNumParImpar = QtWidgets.QPushButton(self.layoutWidget)
        self.pbAceptarNumParImpar.setObjectName("pbAceptarNumParImpar")
        self.gridLayout.addWidget(self.pbAceptarNumParImpar, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(numeroParImpar)
        self.label.setGeometry(QtCore.QRect(90, 10, 141, 41))
        self.label.setObjectName("label")

        self.retranslateUi(numeroParImpar)
        QtCore.QMetaObject.connectSlotsByName(numeroParImpar)

    def retranslateUi(self, numeroParImpar):
        _translate = QtCore.QCoreApplication.translate
        numeroParImpar.setWindowTitle(_translate("numeroParImpar", "Dialog"))
        self.pbAceptarNumParImpar.setText(_translate("numeroParImpar", "Aceptar"))
        self.label_2.setText(_translate("numeroParImpar", "Ingrese un numero para saber si es PAR o IMPAR:"))
        self.label.setText(_translate("numeroParImpar", "NUMERO PAR O IMPAR"))
