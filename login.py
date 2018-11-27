
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from mainWindow import *
from rootUI import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class login_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(login_Window,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        font = QtGui.QFont()
        #font.setBold(True)
        #font.setPointSize(8)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 12))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font)
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.checkPass)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BIBA模型登录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        MainWindow.setWindowIcon(QtGui.QIcon('./img/icon.png'))
        MainWindow.setStyleSheet("background-image:url(./img/icon.png)")

    def checkPass(self):
        nameIn = self.lineEdit.text()
        passwdIn = self.lineEdit_2.text()
        md5 = hashlib.md5()
        md5.update(passwdIn.encode("utf-8"))
        passwdIn = md5.hexdigest()
        if (nameIn == '') or (passwdIn == ''):
            QMessageBox.warning(self,
                                "警告",
                                "账号和密码不能为空",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()
        print(nameIn, passwdIn)
        fr = open('./etc/passwd.txt')
        arrayofLines = fr.readlines()
        numberofLines = len(arrayofLines)
        for line in arrayofLines:
            line = line.strip()
            listFromLine = line.split(':')
            name = listFromLine[0]
            if name == nameIn:
                numberofLines = -1
                passwd = listFromLine[1]
                if passwd == passwdIn:
                    group = listFromLine[2]
                    print("\n登录成功!\n")
                    if name == 'root':
                        rootUI.show()
                        MainWindow.close()
                    else:
                        urName = nameIn
                        mainUI.lineEdit.setText(urName)
                        mainUI.lineEdit_2.setText(group)
                        mainUI.show()
                        MainWindow.close()
                else:
                    QMessageBox.warning(self,
                                        "警告",
                                        "密码错误！",
                                        QMessageBox.Yes)
                    self.lineEdit.setFocus()
        fr.close()
        return 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_Window()
    mainUI = Ui_MainWindow()
    rootUI = root_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
