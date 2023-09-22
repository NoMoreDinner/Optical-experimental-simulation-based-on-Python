# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(215, 231, 232);")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(620, 0, 871, 71))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 60, 411, 528))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_x = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_x.setMinimumSize(QtCore.QSize(200, 75))
        self.label_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_x.setObjectName("label_x")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_x)
        self.SpinBox_x = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.SpinBox_x.setMinimumSize(QtCore.QSize(200, 75))
        self.SpinBox_x.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.SpinBox_x.setFont(font)
        self.SpinBox_x.setStyleSheet("/*QSpinBox*/\n"
"QDoubleSpinBox {\n"
"padding-right: 15px; /* make room for the arrows */\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"background:rgba(0,0,0,50);\n"
"}\n"
"/*\n"
"QDoubleSpinBox::up-button {\n"
"border-image:url(:/image/images/up_arrow.png)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"border-image:url(:/image/images/down_arrow.png)\n"
"}\n"
"*/\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top:3px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom:3px;\n"
"}")
        self.SpinBox_x.setDecimals(1)
        self.SpinBox_x.setMinimum(0.1)
        self.SpinBox_x.setMaximum(5.0)
        self.SpinBox_x.setSingleStep(0.1)
        self.SpinBox_x.setProperty("value", 1.0)
        self.SpinBox_x.setObjectName("SpinBox_x")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SpinBox_x)
        self.label_d = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_d.setMinimumSize(QtCore.QSize(200, 0))
        self.label_d.setObjectName("label_d")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_d)
        self.SpinBox_R = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.SpinBox_R.setMinimumSize(QtCore.QSize(0, 75))
        self.SpinBox_R.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.SpinBox_R.setFont(font)
        self.SpinBox_R.setStyleSheet("/*QSpinBox*/\n"
"QDoubleSpinBox {\n"
"padding-right: 15px; /* make room for the arrows */\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"background:rgba(0,0,0,50);\n"
"}\n"
"/*\n"
"QDoubleSpinBox::up-button {\n"
"border-image:url(:/image/images/up_arrow.png)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"border-image:url(:/image/images/down_arrow.png)\n"
"}\n"
"*/\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top:3px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom:3px;\n"
"}")
        self.SpinBox_R.setDecimals(1)
        self.SpinBox_R.setMinimum(0.1)
        self.SpinBox_R.setMaximum(5.0)
        self.SpinBox_R.setSingleStep(0.1)
        self.SpinBox_R.setProperty("value", 0.5)
        self.SpinBox_R.setObjectName("SpinBox_R")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SpinBox_R)
        self.label_f = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_f.setMinimumSize(QtCore.QSize(200, 75))
        self.label_f.setObjectName("label_f")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_f)
        self.SpinBox_f = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.SpinBox_f.setMinimumSize(QtCore.QSize(0, 75))
        self.SpinBox_f.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.SpinBox_f.setFont(font)
        self.SpinBox_f.setStyleSheet("/*QSpinBox*/\n"
"QDoubleSpinBox {\n"
"padding-right: 15px; /* make room for the arrows */\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"background:rgba(0,0,0,50);\n"
"}\n"
"/*\n"
"QDoubleSpinBox::up-button {\n"
"border-image:url(:/image/images/up_arrow.png)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"border-image:url(:/image/images/down_arrow.png)\n"
"}\n"
"*/\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top:3px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom:3px;\n"
"}")
        self.SpinBox_f.setDecimals(1)
        self.SpinBox_f.setMinimum(0.0)
        self.SpinBox_f.setMaximum(100.0)
        self.SpinBox_f.setSingleStep(0.1)
        self.SpinBox_f.setProperty("value", 50.0)
        self.SpinBox_f.setObjectName("SpinBox_f")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SpinBox_f)
        self.label_N = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_N.setMinimumSize(QtCore.QSize(200, 75))
        self.label_N.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_N.setObjectName("label_N")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_N)
        self.SpinBox_N = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.SpinBox_N.setMinimumSize(QtCore.QSize(0, 75))
        self.SpinBox_N.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.SpinBox_N.setFont(font)
        self.SpinBox_N.setStyleSheet("/*QSpinBox*/\n"
"QSpinBox {\n"
"padding-right: 15px; /* make room for the arrows */\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"background:rgba(0,0,0,50);\n"
"}\n"
"/*\n"
"QDoubleSpinBox::up-button {\n"
"border-image:url(:/image/images/up_arrow.png)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"border-image:url(:/image/images/down_arrow.png)\n"
"}\n"
"*/\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"margin-top:3px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom:3px;\n"
"}")
        self.SpinBox_N.setMinimum(200)
        self.SpinBox_N.setMaximum(2000)
        self.SpinBox_N.setSingleStep(2)
        self.SpinBox_N.setProperty("value", 500)
        self.SpinBox_N.setObjectName("SpinBox_N")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.SpinBox_N)
        self.label_lamda = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_lamda.setMinimumSize(QtCore.QSize(200, 75))
        self.label_lamda.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_lamda.setObjectName("label_lamda")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_lamda)
        self.SpinBox_lamda = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.SpinBox_lamda.setMinimumSize(QtCore.QSize(0, 75))
        self.SpinBox_lamda.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.SpinBox_lamda.setFont(font)
        self.SpinBox_lamda.setStyleSheet("/*QSpinBox*/\n"
"QDoubleSpinBox {\n"
"padding-right: 15px; /* make room for the arrows */\n"
"border:1px solid black;\n"
"border-radius:5px;\n"
"background:rgba(0,0,0,50);\n"
"}\n"
"/*\n"
"QDoubleSpinBox::up-button {\n"
"border-image:url(:/image/images/up_arrow.png)\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"border-image:url(:/image/images/down_arrow.png)\n"
"}\n"
"*/\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top:3px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom:3px;\n"
"}")
        self.SpinBox_lamda.setDecimals(1)
        self.SpinBox_lamda.setMinimum(400.0)
        self.SpinBox_lamda.setMaximum(780.0)
        self.SpinBox_lamda.setSingleStep(0.1)
        self.SpinBox_lamda.setProperty("value", 487.2)
        self.SpinBox_lamda.setObjectName("SpinBox_lamda")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.SpinBox_lamda)
        self.pushButton_recover = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_recover.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_recover.setFont(font)
        self.pushButton_recover.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_recover.setObjectName("pushButton_recover")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_recover)
        self.pushButton_return = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_return.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_return.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_return.setObjectName("pushButton_return")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_return)
        self.label_4.raise_()
        self.SpinBox_x.raise_()
        self.SpinBox_R.raise_()
        self.label_x.raise_()
        self.label_d.raise_()
        self.label_f.raise_()
        self.SpinBox_f.raise_()
        self.label_N.raise_()
        self.SpinBox_N.raise_()
        self.label_lamda.raise_()
        self.SpinBox_lamda.raise_()
        self.pushButton_recover.raise_()
        self.pushButton_return.raise_()
        self.formLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 660, 411, 361))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_x_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_x_2.setMinimumSize(QtCore.QSize(200, 75))
        self.label_x_2.setMaximumSize(QtCore.QSize(200, 75))
        self.label_x_2.setObjectName("label_x_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_x_2)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit.setMaximumSize(QtCore.QSize(200, 75))
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.comboBox_style = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_style.setMinimumSize(QtCore.QSize(200, 75))
        self.comboBox_style.setMaximumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.comboBox_style.setFont(font)
        self.comboBox_style.setStyleSheet("")
        self.comboBox_style.setObjectName("comboBox_style")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_style)
        self.label_d_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_d_2.setMinimumSize(QtCore.QSize(200, 75))
        self.label_d_2.setMaximumSize(QtCore.QSize(200, 75))
        self.label_d_2.setObjectName("label_d_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_d_2)
        self.comboBox_N = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_N.setMinimumSize(QtCore.QSize(200, 75))
        self.comboBox_N.setMaximumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.comboBox_N.setFont(font)
        self.comboBox_N.setObjectName("comboBox_N")
        self.comboBox_N.addItem("")
        self.comboBox_N.addItem("")
        self.comboBox_N.addItem("")
        self.comboBox_N.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_N)
        self.label_n_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_n_2.setMinimumSize(QtCore.QSize(200, 75))
        self.label_n_2.setMaximumSize(QtCore.QSize(200, 75))
        self.label_n_2.setObjectName("label_n_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_n_2)
        self.pushButton_Save2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_Save2.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_Save2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_Save2.setFont(font)
        self.pushButton_Save2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_Save2.setObjectName("pushButton_Save2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_Save2)
        self.pushButton_Save1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_Save1.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_Save1.setFont(font)
        self.pushButton_Save1.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_Save1.setObjectName("pushButton_Save1")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_Save1)
        self.pushButton_exit = QtWidgets.QPushButton(MainWindow)
        self.pushButton_exit.setGeometry(QtCore.QRect(1820, 0, 100, 60))
        self.pushButton_exit.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        # self.layoutWidget = QtWidgets.QWidget(MainWindow)
        # self.layoutWidget.setGeometry(QtCore.QRect(640, 680, 971, 400))
        # self.layoutWidget.setObjectName("layoutWidget")
        # self.formLayout_I = QtWidgets.QFormLayout(self.layoutWidget)
        # self.formLayout_I.setContentsMargins(0, 0, 0, 0)
        # self.formLayout_I.setObjectName("formLayout_I")
        self.formLayoutWidget_6 = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(1510, 70, 407, 206))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_2.setStyleSheet("font: 9pt \"Times New Roman\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background:rgb(255, 255, 250);\n"
"border: 1px solid black;")
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(1520, 340, 301, 241))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(1510, 280, 152, 47))
        self.label_8.setStyleSheet("font: 9pt \"Times New Roman\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_start = QtWidgets.QPushButton(MainWindow)
        self.pushButton_start.setGeometry(QtCore.QRect(1650, 1000, 200, 60))
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.formLayoutWidget_3 = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(480, 90, 71, 1066))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_I = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_I.setMinimumSize(QtCore.QSize(0, 500))
        self.label_I.setMaximumSize(QtCore.QSize(200, 500))
        self.label_I.setObjectName("label_I")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_I)
        self.label_diffraction = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_diffraction.setMinimumSize(QtCore.QSize(0, 500))
        self.label_diffraction.setMaximumSize(QtCore.QSize(200, 500))
        self.label_diffraction.setObjectName("label_diffraction")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_diffraction)
        # self.formLayoutWidget_4 = QtWidgets.QWidget(MainWindow)
        # self.formLayoutWidget_4.setGeometry(QtCore.QRect(640, 80, 991, 591))
        # self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        # self.formLayout_diffraction = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        # self.formLayout_diffraction.setContentsMargins(0, 0, 0, 0)
        # self.formLayout_diffraction.setObjectName("formLayout_diffraction")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(1520, 660, 131, 41))
        self.label_7.setStyleSheet("font: 9pt \"Times New Roman\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.pushButton_start_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_start_2.setGeometry(QtCore.QRect(1620, 590, 200, 60))
        self.pushButton_start_2.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.pushButton_start_2.setFont(font)
        self.pushButton_start_2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton_start_2.setObjectName("pushButton_start_2")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(620, 70, 871, 34))
        self.label_6.setObjectName("label_6")
        self.label_PrinciplePicture = QtWidgets.QLabel(MainWindow)
        self.label_PrinciplePicture.setGeometry(QtCore.QRect(1520, 700, 401, 291))
        self.label_PrinciplePicture.setObjectName("label_PrinciplePicture")
        self.formLayoutWidget.raise_()
        self.formLayoutWidget_2.raise_()
        self.pushButton_exit.raise_()
        self.label.raise_()
        # self.layoutWidget.raise_()
        self.formLayoutWidget_6.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.pushButton_start.raise_()
        self.formLayoutWidget_3.raise_()
        # self.formLayoutWidget_4.raise_()
        self.label_7.raise_()
        self.pushButton_start_2.raise_()
        self.label_6.raise_()
        self.label_PrinciplePicture.raise_()

        self.formLayoutWidget_4 = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(480, -200, 1081, 1091))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_diffraction = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_diffraction.setContentsMargins(0, 0, 0, 0)
        self.formLayout_diffraction.setObjectName("formLayout_diffraction")
        self.formLayoutWidget_5 = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(480, 580, 1081, 500))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayoutWidget_5.lower()
        self.formLayoutWidget_4.lower()
        self.formLayout_I = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_I.setContentsMargins(0, 0, 0, 0)
        self.formLayout_I.setObjectName("formLayout_I")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        from mplwidget import MPL_WIDGET
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mplwidget_diffraction = MPL_WIDGET(self.centralwidget)
        self.mplwidget_diffraction.setObjectName("mplwidget_diffraction")
        self.formLayout_diffraction.addWidget(self.mplwidget_diffraction)

        self.mplwidget_I = MPL_WIDGET(self.centralwidget)
        self.mplwidget_I.setObjectName("mplwidget_I")
        self.formLayout_I.addWidget(self.mplwidget_I)

        self.label_PrinciplePicture.setPixmap(QtGui.QPixmap("img/圆孔衍射原理图.png").scaled(401, 291))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">圆孔衍射演示实验</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">参数调节区</span></p></body></html>"))
        self.label_x.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt;\">屏宽(mm)</span></p></body></html>"))
        self.label_d.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt;\">孔径(mm)</span></p></body></html>"))
        self.label_f.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt;\">焦距(cm)</span></p></body></html>"))
        self.label_N.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt;\">像素n(2^n)</span></p></body></html>"))
        self.label_lamda.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt;\">波长(nm)</span></p></body></html>"))
        self.pushButton_recover.setText(_translate("MainWindow", "恢复默认"))
        self.pushButton_return.setText(_translate("MainWindow", "返回主界面"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">图像保存区</span></p></body></html>"))
        self.label_x_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">文件名</span></p></body></html>"))
        self.comboBox_style.setItemText(0, _translate("MainWindow", ".jpg"))
        self.comboBox_style.setItemText(1, _translate("MainWindow", ".png"))
        self.comboBox_style.setItemText(2, _translate("MainWindow", ".bmp"))
        self.label_d_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">格式</span></p></body></html>"))
        self.comboBox_N.setItemText(0, _translate("MainWindow", "150"))
        self.comboBox_N.setItemText(1, _translate("MainWindow", "300"))
        self.comboBox_N.setItemText(2, _translate("MainWindow", "450"))
        self.comboBox_N.setItemText(3, _translate("MainWindow", "600"))
        self.label_n_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:20pt; font-weight:600;\">分辨率</span></p></body></html>"))
        self.pushButton_Save2.setText(_translate("MainWindow", "保存光强分布"))
        self.pushButton_Save1.setText(_translate("MainWindow", "保存衍射图像"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">实验目的</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">1.理解圆孔衍射的实验原理。</span></p><p><span style=\" font-size:18pt;\">2.了解圆孔衍射的成像规律。</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"img/圆孔衍射公式.gif\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">光强公式</span></p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "原理演示"))
        self.label_I.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">衍</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">射</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">图</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">像</span></p></body></html>"))
        self.label_diffraction.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">光</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">强</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">分</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">布</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">原理图</span></p></body></html>"))
        self.pushButton_start_2.setText(_translate("MainWindow", "详细推导"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">仿真图像区</span></p></body></html>"))
        self.label_PrinciplePicture.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"img/圆孔衍射原理图.png\"/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec())
