# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numeroPerfecto.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_numeroPerfecto(object):
    def setupUi(self, numeroPerfecto):
        numeroPerfecto.setObjectName("numeroPerfecto")
        numeroPerfecto.resize(320, 240)
        self.resultPerfecto = QtWidgets.QLabel(numeroPerfecto)
        self.resultPerfecto.setGeometry(QtCore.QRect(30, 170, 249, 34))
        self.resultPerfecto.setText("")
        self.resultPerfecto.setObjectName("resultPerfecto")
        self.layoutWidget = QtWidgets.QWidget(numeroPerfecto)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 255, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtNumPerfecto = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNumPerfecto.setObjectName("txtNumPerfecto")
        self.gridLayout.addWidget(self.txtNumPerfecto, 2, 0, 1, 1)
        self.pbAceptarPerfecto = QtWidgets.QPushButton(self.layoutWidget)
        self.pbAceptarPerfecto.setObjectName("pbAceptarPerfecto")
        self.gridLayout.addWidget(self.pbAceptarPerfecto, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(numeroPerfecto)
        self.label.setGeometry(QtCore.QRect(80, 10, 141, 41))
        self.label.setObjectName("label")

        self.retranslateUi(numeroPerfecto)
        QtCore.QMetaObject.connectSlotsByName(numeroPerfecto)

    def retranslateUi(self, numeroPerfecto):
        _translate = QtCore.QCoreApplication.translate
        numeroPerfecto.setWindowTitle(_translate("numeroPerfecto", "Dialog"))
        self.pbAceptarPerfecto.setText(_translate("numeroPerfecto", "Aceptar"))
        self.label_2.setText(_translate("numeroPerfecto", "Ingrese un numero para saber si es perfecto o no:"))
        self.label.setText(_translate("numeroPerfecto", "NUMERO PERFECTO"))
