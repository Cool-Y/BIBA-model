import sys
import os
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout,QDirModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.file_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setCursorPosition(4)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 70, 113, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(13)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(450, 20, 321, 401))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 450, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 450, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 500, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(150,500,200,60))
        self.textEdit_1.setObjectName("textEdit")
        self.textEdit_1.setFont(font)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 520, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 528, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.readfile)
        self.pushButton_2.clicked.connect(self.writefile)
        self.pushButton_4.clicked.connect(self.touchfile)

        self.model = QFileSystemModel()
        cur_path = os.getcwd()
        self.model.setRootPath(cur_path)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(30, 150, 400, 300))
        self.treeView.setObjectName("treeView")
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.setRootPath(cur_path))
        #self.treeView = QTreeView()
        self.treeView.setAnimated(False)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setWindowTitle("Dir View")
        self.treeView.resize(400, 320)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.treeView)
        self.setLayout(windowLayout)
        self.treeView.doubleClicked.connect(self.showpath)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "普通用户"))
        MainWindow.setWindowIcon(QtGui.QIcon('./img/icon.png'))
        self.label.setText(_translate("MainWindow", "您好！"))
        self.label_2.setText(_translate("MainWindow", "您的用户等级为："))
        self.pushButton.setText(_translate("MainWindow", "读取"))
        self.pushButton_2.setText(_translate("MainWindow", "写入"))
        self.pushButton_3.setText(_translate("MainWindow", "选择"))
        self.pushButton_4.setText(_translate("MainWindow", "新建文件"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "输入文件名"))

    def showpath(self,signal):
        print('获取文件位置成功\n')
        file_path = self.treeView.model().filePath(signal)
        self.textEdit_1.setPlaceholderText(file_path)
        self.file_path = file_path

    def getGrade(self):
        fa = open('./etc/ac.txt', 'r')
        a = fa.read()
        dict = eval(a)
        return dict

    def readfile(self):
        dict = self.getGrade()
        fgrade = str(dict[self.file_path])
        ugrade = self.lineEdit_2.text()
        if ugrade >=  fgrade:
            print(ugrade+ ' 正在读取  '+fgrade)
            filename = self.file_path
            print(filename)
            fr = open(filename)
            lines = ''
            arrayofLines = fr.readlines()
            for line in arrayofLines:
                lines += line
            self.textEdit.setText(lines)
            print('读取成功\n')
        else:
            QMessageBox.warning(self,
                                "警告",
                                "您的用户等级太高",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()


    def writefile(self):
        dict = self.getGrade()
        fgrade = dict[self.file_path]
        ugrade = self.lineEdit_2.text()
        print(ugrade + ' 正在写入  ' + fgrade)
        if ugrade <= fgrade:
            filename = self.file_path
            str = self.textEdit.toPlainText()
            print(str)
            fo = open(filename, 'r+')
            fo.seek(0, 2)
            fo.write(str)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "您的用户等级太低",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

    def touchfile(self):
        urName = self.lineEdit.text()
        filename = self.lineEdit_4.text()
        cur_path = os.getcwd()
        new_path = os.path.join(cur_path + '/file', urName)
        print(urName)
        if os.path.exists(new_path) == False:
            os.mkdir(new_path)
        os.chdir(new_path)
        fr = open(filename, 'w')
        key = (new_path + '/' + filename).replace('\\', '/')
        fr.close()
        os.chdir(cur_path)
        fa = open('./etc/ac.txt', 'r')
        a = fa.read()
        if a == '':
            dict = {}
        else:
            dict = eval(a)
        dict[key] = self.lineEdit_2.text()
        fr = open('./etc/ac.txt', 'w')
        fr.write(str(dict))
        fr.close()
        fa.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
