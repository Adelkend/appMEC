# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/distribuida.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 215)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 256, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Força distribuída"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; text-decoration: underline;\">Força Distribuída</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-85d7050b-7fff-a8f8-3ad9-b9e73a89c6ec\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">P</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">ara calcular a força resultante da ação de uma força disposta por um comprimento, basta integrar a força ao longo do comprimento sobre o qual ela atua. O ponto de aplicação da força será o baricentro da figura formada pelo carregamento. Num retângulo, por exemplo, a força é aplicada no meio dele; enquanto num triângulo a força seria aplicada a um terço da altura.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Voltar"))
