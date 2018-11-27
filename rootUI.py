import sys
import os
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout,QDirModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib

class root_Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(root_Window, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.name = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 51, 31))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 120, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 210, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 170, 221, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 160, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 390, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 320, 171, 181))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(360, 370, 191, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理员"))
        MainWindow.setWindowIcon(QtGui.QIcon('./img/icon.png'))
        self.pushButton_3.setText(_translate("MainWindow", "用户名："))
        self.pushButton_5.setText(_translate("MainWindow", "用户等级："))
        self.comboBox.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox.setItemText(3, _translate("MainWindow", "D"))
        self.pushButton_4.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "添加用户"))
        self.label.setText(_translate("MainWindow", "已有用户"))
        self.label_2.setText(_translate("MainWindow", "尊敬的管理员你好！"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_6.setText(_translate("MainWindow", "已有用户"))

        self.pushButton.clicked.connect(self.adduser)
        self.pushButton_6.clicked.connect(self.readuser)
        self.pushButton_2.clicked.connect(self.rmuser)

    def adduser(self):
        name = self.lineEdit_4.text()
        passwd = self.lineEdit_6.text()
        md5 = hashlib.md5()
        md5.update(passwd.encode("utf-8"))
        passwd = md5.hexdigest()
        group = self.comboBox.currentText()
        self.name = name
        if self.euxit():
            if name == '' or passwd == '':
                QMessageBox.warning(self,
                                    "警告",
                                    "账号和密码不能为空",
                                    QMessageBox.Yes)
                self.lineEdit.setFocus()
            else:
                cur_path = os.getcwd()
                filename = cur_path + '/etc/passwd.txt'
                fi = open(filename, 'r+')
                str = '\n' + name + ':' + passwd + ':' + group
                print('成功增加用户' + str + '\n')
                fi.seek(0, 2)
                fi.write(str)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "用户已存在",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

    def readuser(self):
        cur_path = os.getcwd()
        filename = cur_path + '/etc/passwd.txt'
        fo = open(filename)
        arrayofLines = fo.readlines()
        names = ''
        for line in arrayofLines:
            line = line.strip()
            listFromLine = line.split(':')
            names = names + listFromLine[0] + '\n'
        self.textEdit.setPlaceholderText(names)

    def rmuser(self):
        print(1)
        cur_path = os.getcwd()
        filename = cur_path + '/etc/passwd.txt'
        rmName = self.lineEdit.text()
        with open(filename, 'r',encoding="utf-8") as r:
            lines = r.readlines()
            lenl = len(lines)
        with open(filename, 'w',encoding="utf-8") as w:
            for line in lines:
                l = line.strip()
                listFromLine = l.split(':')
                if rmName == listFromLine[0]:
                    print('删除用户' + rmName)
                    continue
                if line == '\n':
                    print('find')
                    line = ''
                w.write(line)



    def euxit(self):
        name = self.name
        flag = True
        cur_path = os.getcwd()
        filename = cur_path + '/etc/passwd.txt'
        fo = open(filename)
        arrayofLines = fo.readlines()
        for line in arrayofLines:
            line = line.strip()
            listFromLine = line.split(':')
            if name == listFromLine[0]:
                flag = False
        return flag


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = root_Window()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())