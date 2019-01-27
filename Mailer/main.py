# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mailer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from model import Model
import os 
import sendgrid
from sendgrid.helpers.mail import Content, Mail, Email
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 555)
        MainWindow.setMinimumSize(QtCore.QSize(789, 555))
        MainWindow.setMaximumSize(QtCore.QSize(800, 555))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 510, 181, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 40, 351, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 341, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 2, 341, 441))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 40, 431, 491))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(360, 10, 431, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 10, 341, 20))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.splitter_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 510, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.browseSlot)
        self.pushButton_3.clicked.connect(self.writeSlot)
        self.lineEdit_3.returnPressed.connect(self.returnedPressedSlot)
        self.pushButton.clicked.connect(self.sendMail)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MailerApp"))
        self.pushButton_3.setText(_translate("MainWindow", "Write Doc"))
        self.label_6.setText(_translate("MainWindow", "Load leads"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Enter your email content"))
        self.pushButton.setText(_translate("MainWindow", "Send mail"))
        self.label_5.setText(_translate("MainWindow", "Subject:"))
        self.label_2.setText(_translate("MainWindow", "From:"))

        @pyqtSlot()
        def browseSlot(self):
            pass
        @pyqtSlot()
        def writeSlot(self):
            pass
        @pyqtSlot()
        def returnedPressedSlot(self):
            pass 
        @pyqtSlot()
        def sendMail(self):
            pass
class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.model = Model()
    def debugPrint(self, msg):
        self.textEdit_2.append(msg)
    def refreshAll(self):
        self.lineEdit_3.setText(self.model.getFileName())
        self.textEdit_2.setText(self.model.getFileContents())
    def returnedPressedSlot(self):
        fileName = self.lineEdit_3.text()
        if self.model.isValid(fileName):
            self.model.setFilename(self.lineEdit_3.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n"+ fileName)
            m.setIcon(QtWidgets.QMessageBox.WARNING)
            m.setStandardButtons(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified:"+ fileName)
            
    def writeSlot(self):
        self.textEdit_2.moveCursor(QtGui.QTextCursor.End)
        self.textEdit_2.insertPlainText(self.model.openfile(self.lineEdit_3.text()))
        
    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.DontUseNativeDialog  
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileNane()", "",
         "All Files (*);; Python Files(*.txt", options=options)
        if fileName:
            self.debugPrint("setting file name:"+ fileName)
            self.model.setFilename(fileName)
            self.refreshAll()  
    def getList(self):
        self.mailArray = list(self.textEdit_2.toPlainText()) 
        return self.mailArray
    def sendMail(self):
        count =0
        
        with open(str(self.lineEdit_3.text()), "r") as file:
            for m in file.readlines():
                try:
                    self.mail(m)
                    self.label.setText("DONE!")
                except:
                    print("Error")

    def getParams(self):
        print(self.textEdit_2.toPlainText(),self.lineEdit_2.text(),self.lineEdit.text() )
        
    def mail(self, email):
        self.sg = sendgrid.SendGridAPIClient(
            apikey="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"
        )
        self.from_email = Email(str(self.textEdit_3.toPlainText()))
        self.to_email = Email(str(email))
        self.subject = str(self.lineEdit_2.text())
        self.content = Content("text/plain",str(self.textEdit.toPlainText()))
        self.sendmail = Mail(self.from_email, self.subject, self.to_email, self.content)
        # self.sendmail.get()
        self.response = self.sg.client.mail.send.post(request_body=self.sendmail.get())
        print(self.sendmail.get())
        # The statements below can be included for debugging purposes
        print(self.response.status_code)
        print(self.response.body)
        print(self.response.headers) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

