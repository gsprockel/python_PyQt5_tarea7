import sys, re
#from PyQt5.QtWidgets import  QMessageBox
from GUIs.mainWindows import *
from GUIs.formularioMultip import *
from GUIs.numeroParImpar import *
from GUIs.numeroPerfecto import *
from GUIs.numeroPrimo import *
from GUIs.numeroExponencial import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwards):
        super(MainWindow,self).__init__(*args,**kwards)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #implentar clases o acciones
        self.ui.actionmultiplicar.triggered.connect(self.mostrarMultip)
        self.ui.actionNumero_Par.triggered.connect(self.mostrarNumeroPar)
        self.ui.actionNumero_perfecto.triggered.connect(self.mostrarNumeroPerfecto)
        self.ui.actionNumero_primo.triggered.connect(self.mostrarNumeroPrimo)
        self.ui.actionNumero_Exponencial.triggered.connect(self.mostrarExponencial)

        
    def mostrarMultip(self):
        ventanaFormMultip = formularioMultip(self)
        ventanaFormMultip.show()
    
    def mostrarNumeroPar(self):
        ventanaNumeroPar=numeroParImpar(self)
        ventanaNumeroPar.show()

    def mostrarNumeroPerfecto(self):
        ventanaNumPerfecto = numeroPerfecto(self)
        ventanaNumPerfecto.show()

    def mostrarNumeroPrimo(self):
        ventanaNumPrimo = numeroPrimo(self)
        ventanaNumPrimo.show()

    def mostrarExponencial(self):
        ventananumExponencial = numeroExponencial(self)
        ventananumExponencial.show()



class formularioMultip(QtWidgets.QDialog):
    def __init__(self,*args,**kwards):
        super(formularioMultip,self).__init__(*args,**kwards)
        self.ui = Ui_formularioMultip()
        self.ui.setupUi(self)

        self.ui.pbAceptar.clicked.connect(self.multiplNum)
    
    def multiplNum(self):
        #
        result = float(self.ui.txtdato1.text()) * float(self.ui.txtdato2.text())

        self.ui.lblresultado.setText(str(result))
        # print(result)

class numeroParImpar(QtWidgets.QDialog):
    def __init__(self,*args,**kwards):
        super(numeroParImpar,self).__init__(*args,**kwards)
        self.ui = Ui_numeroParImpar()
        self.ui.setupUi(self)

        self.ui.pbAceptarNumParImpar.clicked.connect(self.ParImpar)

    def ParImpar(self):
        result=int(self.ui.txtNum.text())%2
        if result == 0:
            self.ui.resultParImpar.setText(str("es un numero par"))
        else:
            self.ui.resultParImpar.setText(str("es un numero impar"))

class numeroPerfecto(QtWidgets.QDialog):

    def __init__(self,*args,**kwards):
        super(numeroPerfecto,self).__init__(*args,**kwards)
        self.ui = Ui_numeroPerfecto()
        self.ui.setupUi(self)

        self.ui.pbAceptarPerfecto.clicked.connect(self.numPerfecto)

    def numPerfecto(self):
        suma=0
        valor=int(self.ui.txtNumPerfecto.text())
        for i in range(1, valor): 
            if valor % i == 0:    
                suma=suma+i
        
        if suma != valor:
            self.ui.resultPerfecto.setText(str("El " + str(valor) + " NO es un numero perfecto"))
        else:
            self.ui.resultPerfecto.setText(str("El " + str(valor) + " es un numero perfecto"))

class numeroPrimo(QtWidgets.QDialog):
    def __init__(self,*args,**kwards):
        super(numeroPrimo,self).__init__(*args,**kwards)
        self.ui = Ui_numeroPrimo()
        self.ui.setupUi(self)

        self.ui.pbAceptarNumPrimo.clicked.connect(self.numPrimo)

    def numPrimo(self):
        x=0
        valor= int(self.ui.txtNumPrimo.text())
        if valor < 2: 
            x=1
        for i in range(2, valor): 
            if valor % i == 0:    
                x=1
                break
        
        if x==1:
            self.ui.resultPrimos.setText(str("El "+str(valor)+" no es un numero Primo"))
        else: 
            self.ui.resultPrimos.setText(str("El "+str(valor)+" es un numero Primo"))

class numeroExponencial(QtWidgets.QDialog):
    def __init__(self,*args,**kwards):
        super(numeroExponencial,self).__init__(*args,**kwards)
        self.ui = Ui_numeroExponencial()
        self.ui.setupUi(self)

        self.ui.pb_aceptar.clicked.connect(self.exponencial)

    def exponencial(self):
        n=50
        valor = int(self.ui.txtnum.text())
        resultado = valor ** n
        self.ui.result.setText(str("El numero exponencial de "+str(valor)+"^50 es "+str(resultado)))


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()