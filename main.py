import sys
from xml.sax import parseString
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from pyparsing import ParseSyntaxException
from sklearn.covariance import MinCovDet
from main_window_ui import Ui_MainWindow
import resources_rc
import formulas
from PyQt5 import QtGui

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('ui/resources/icone.png'))
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.conteudo)
        self.pushButton_2.clicked.connect(self.exercicios)

    def login(self):
        self.dialog = Login(self)
        self.dialog.exec()

    def conteudo(self):
        dialog = Conteudo(self)
        dialog.exec()
    
    def exercicios(self):
        dialog = Exercicios(self)
        dialog.exec()

class Apoios(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/apoios.ui", self)

class Equilibrio(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/equilibrio.ui", self)

class Distribuida(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/distribuida.ui", self)

class Conteudo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/conteudo.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.apoios)
        self.pushButton_2.clicked.connect(self.equilibrio)
        self.pushButton_3.clicked.connect(self.distribuida)
        self.pushButton_4.clicked.connect(win.show)

    def apoios(self):
        dialog = Apoios(self)
        dialog.exec()
    
    def equilibrio(self):
        dialog = Equilibrio(self)
        dialog.exec()
    
    def distribuida(self):
        dialog = Distribuida(self)
        dialog.exec()

class Exercicios(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exercicios.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton_7.clicked.connect(win.show)
        self.pushButton.clicked.connect(self.exemplo1)
        self.pushButton_2.clicked.connect(self.exemplo2)
        self.pushButton_3.clicked.connect(self.exemplo3)
        self.pushButton_4.clicked.connect(self.exemplo4)
        self.pushButton_5.clicked.connect(self.exemplo5)
        self.pushButton_6.clicked.connect(self.exemplo6)
    
    def exemplo1(self):
        dialog = Exemplo1(self)
        dialog.exec()

    def exemplo2(self):
        dialog = Exemplo2(self)
        dialog.exec()

    def exemplo3(self):
        dialog = Exemplo3(self)
        dialog.exec()

    def exemplo4(self):
        dialog = Exemplo4(self)
        dialog.exec()
    
    def exemplo5(self):
        dialog = Exemplo5(self)
        dialog.exec()
    
    def exemplo6(self):
        dialog = Exemplo6(self)
        dialog.exec()

class Exemplo1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo1.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):  
        Fr, Fa = formulas.forcas1(int(self.lineEdit.text()), int(self.lineEdit_2.text()))
        Fc, Mc = formulas.esforcos1(int(self.lineEdit_2.text()), int(self.lineEdit_3.text()))
        self.label_4.setText(str(Fc))
        self.label_6.setText(str(Mc))
        self.label_8.setText(str(Fr))
        self.label_10.setText(str(Fa))

class Exemplo2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo2.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):
        Fr, Fa = formulas.forcas2(int(self.lineEdit.text()), int(self.lineEdit_2.text()))
        Fc, Mc = formulas.esforcos2(int(self.lineEdit_2.text()), int(self.lineEdit.text()), int(self.lineEdit_3.text()))
        self.label_4.setText(str(Fc))
        self.label_6.setText(str(Mc))
        self.label_8.setText(str(Fr))
        self.label_10.setText(str(Fa))

class Exemplo3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo3.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):
        Fa, Fb = formulas.forcas3(int(self.lineEdit_3.text()), int(self.lineEdit.text()))
        Mc = formulas.esforcos3(Fb, int(self.lineEdit.text()), int(self.lineEdit_2.text()))
        self.label_4.setText(str(Mc))
        self.label_8.setText(str(Fa))
        self.label_10.setText(str(Fb))

class Exemplo4(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo4.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):
        Fa, Fb = formulas.forcas4(int(self.lineEdit_5.text()), int(self.lineEdit_4.text()), int(self.lineEdit_2.text()))
        Fc, Mc = formulas.esforcos4(int(self.lineEdit_4.text()), int(self.lineEdit_6.text()), int(self.lineEdit_5.text()), int(self.lineEdit_2.text()))
        self.label_17.setText(str(Fa))
        self.label_19.setText(str(Fb))
        self.label_13.setText(str(Fc))
        self.label_15.setText(str(Mc))

class Exemplo5(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo5.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):
        Fa, Fb, Fr = formulas.forcas5(int(self.lineEdit_2.text()), int(self.lineEdit_3.text()), int(self.lineEdit.text()), int(self.lineEdit_4.text()))
        Fc, Mc = formulas.esforcos5(int(self.lineEdit_3.text()), int(self.lineEdit_5.text()), int(self.lineEdit.text()), int(self.lineEdit_2.text()), int(self.lineEdit_4.text()))
        self.label_4.setText(str(Fc))
        self.label_6.setText(str(Mc))
        self.label_8.setText(str(Fa))
        self.label_10.setText(str(Fb))

class Exemplo6(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/exemplo6.ui", self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(win.exercicios)

    def resp(self):
        Fa, Fb = formulas.forcas6(int(self.lineEdit.text()), int(self.lineEdit_2.text()), int(self.lineEdit_3.text()), int(self.lineEdit_4.text()))
        Fc, Mc = formulas.esforcos6(int(self.lineEdit_4.text()), Fb, int(self.lineEdit_3.text()), int(self.lineEdit_5.text()), int(self.lineEdit_2.text()), int(self.lineEdit.text()))
        self.label_4.setText(str(Fc))
        self.label_6.setText(str(Mc))
        self.label_8.setText(str(Fa))
        self.label_10.setText(str(Fb))

class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/bem_vindo.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.login()
    if win.dialog.accept:
        nome = win.dialog.NomeUsuario.text()
        win.label_2.setText(f"Bem vindo {nome}, escolha o que deseja aprender:")
    sys.exit(app.exec())