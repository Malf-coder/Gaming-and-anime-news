# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'News.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.label.setStyleSheet("background-color: rgb(34, 40, 49);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-4, 0, 151, 601))
        self.label_2.setStyleSheet("background-color: rgb(57, 62, 70);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.NewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewsButton.setGeometry(QtCore.QRect(10, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.NewsButton.setFont(font)
        self.NewsButton.setStyleSheet("QPushButton#NewsButton {\n"
                                      "  font-weight: 700;\n"
                                      "  color:#00ADB5 ;\n"
                                      "  text-decoration: none;\n"
                                      "  border-radius: 3px;\n"
                                      "  border-width: 3px;\n"
                                      "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                      "  transition: 0.2s;\n"
                                      "  border-style: outset;\n"
                                      "  border-radius: 20px;\n"
                                      "  border-color:#00ADB5;\n"
                                      "} \n"
                                      "QPushButton#NewsButton:hover { border-color: rgb(0, 145, 150);\n"
                                      "                                                     color: rgb(0, 145, 150);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.NewsButton.setObjectName("NewsButton")
        self.AnimeButton = QtWidgets.QPushButton(self.centralwidget)
        self.AnimeButton.setGeometry(QtCore.QRect(10, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(87)
        font.setStrikeOut(False)
        self.AnimeButton.setFont(font)
        self.AnimeButton.setStyleSheet("QPushButton#AnimeButton {\n"
                                       "  font-weight: 700;\n"
                                       "  color:#222831 ;\n"
                                       "  text-decoration: none;\n"
                                       "  border-radius: 3px;\n"
                                       "  border-width: 3px;\n"
                                       "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                       "  transition: 0.2s;\n"
                                       "  border-style: outset;\n"
                                       "  border-radius: 20px;\n"
                                       "  border-color:#222831;\n"
                                       "} \n"
                                       "QPushButton#AnimeButton:hover { border-color:rgb(20, 24, 30);\n"
                                       "                                                    color:rgb(20, 24, 30);\n"
                                       "}")
        self.AnimeButton.setObjectName("AnimeButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News"))
        self.NewsButton.setText(_translate("MainWindow", "Game news"))
        self.AnimeButton.setText(_translate("MainWindow", "Anime news"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
