# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSWd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PSWD(object):
    def setupUi(self, PSWD):
        PSWD.setObjectName("PSWD")
        PSWD.resize(800, 578)
        self.centralwidget = QtWidgets.QWidget(PSWD)
        self.centralwidget.setObjectName("centralwidget")
        self.PSWD_2 = QtWidgets.QFrame(self.centralwidget)
        self.PSWD_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.PSWD_2.setStyleSheet("background-color: rgb(170, 255, 127)\n"
"")
        self.PSWD_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PSWD_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PSWD_2.setObjectName("PSWD_2")
        self.user = QtWidgets.QPushButton(self.PSWD_2)
        self.user.setGeometry(QtCore.QRect(60, 50, 41, 41))
        self.user.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Pictures/usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user.setIcon(icon)
        self.user.setIconSize(QtCore.QSize(70, 50))
        self.user.setObjectName("user")
        self.home = QtWidgets.QPushButton(self.PSWD_2)
        self.home.setGeometry(QtCore.QRect(660, 50, 31, 31))
        self.home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Pictures/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon1)
        self.home.setObjectName("home")
        self.comboBox = QtWidgets.QComboBox(self.PSWD_2)
        self.comboBox.setGeometry(QtCore.QRect(120, 50, 521, 41))
        self.comboBox.setStyleSheet("background-color: rgb(85, 170, 0)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.PSWD_2)
        self.label.setGeometry(QtCore.QRect(290, 200, 221, 341))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Pictures/gota.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.PSWD_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 540, 201, 28))
        self.pushButton.setStyleSheet("font: 12pt \"Century Gothic\";\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.PSWD_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 120, 621, 61))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.PSWD_2)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 260, 401, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 18px;")
        self.textEdit_2.setObjectName("textEdit_2")
        PSWD.setCentralWidget(self.centralwidget)

        self.retranslateUi(PSWD)
        QtCore.QMetaObject.connectSlotsByName(PSWD)

    def retranslateUi(self, PSWD):
        _translate = QtCore.QCoreApplication.translate
        PSWD.setWindowTitle(_translate("PSWD", "MainWindow"))
        self.comboBox.setItemText(0, _translate("PSWD", "Administrador"))
        self.comboBox.setItemText(1, _translate("PSWD", "General"))
        self.pushButton.setText(_translate("PSWD", "Guardar cambios"))
        self.textEdit.setHtml(_translate("PSWD", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic\'; font-size:12pt; color:#000000;\">Ingresa la constraseña para entrar al modo administrador</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("PSWD", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Escribe la contraseña...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PSWD = QtWidgets.QMainWindow()
    ui = Ui_PSWD()
    ui.setupUi(PSWD)
    PSWD.show()
    sys.exit(app.exec_())
