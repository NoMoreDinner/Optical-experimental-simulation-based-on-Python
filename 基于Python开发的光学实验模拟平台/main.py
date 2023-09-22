import numpy,math
from Myfun import wavelength_to_map
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication , QMainWindow, QTableWidgetItem, QMessageBox
from UiApp import Ui_MainWindow
import sys
import os

path = os.path.abspath('.')
# 导入字体管理模块



class MainApp(QMainWindow , Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)


        self.setupUi(self)

        self.setpushButton()


    def setpushButton(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\demos.html"))

        # self.pushButton_exit.clicked.connect(self.pushButton_exit_Clicked)
        self.pushButton_in.clicked.connect((self.pushButton_in_Clicked))
        self.pushButton_YangDoubleSlit.clicked.connect(self.pushButton_YangDoubleSlit_Clicked)
        self.pushButton_DoubleSlitDiffraction.clicked.connect(self.pushButton_DoubleSlitDiffraction_Clicked)
        self.pushButton_SplittingInterference.clicked.connect(self.pushButton_SplittingInterference_Clicked)
        self.pushButton_GratingDiffraction.clicked.connect(self.pushButton_GratingDiffraction_Clicked)
        self.pushButton_RoundHoleDiffraction.clicked.connect(self.pushButton_RoundHoleDiffraction_Clicked)
        self.pushButton_NewtonRing.clicked.connect(self.pushButton_NewtonRing_Clicked)
        self.pushButton_MichelsonInterferometer.clicked.connect(self.pushButton_MichelsonInterferometer_Clicked)
        self.pushButton_read.clicked.connect(self.pushButton_read_Clicked)
        self.pushButton_measure.clicked.connect(self.pushButton_measure_Clicked)

        from Main_YangDoubleSlit import MainApp as Window
        self.Window = Window()

    def pushButton_measure_Clicked(self):
        pass


    def pushButton_read_Clicked(self):
        from ShowHtml import MainApp as Window_Html
        self.Window_Html = Window_Html()
        self.Window_Html.showhtml(self.path)
        self.Window_Html.showFullScreen()

    def pushButton_NewtonRing_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\牛顿环干涉\demo.html"))
        self.path = path + "\data\html\牛顿环干涉\demo.html"
        from Main_NewtonRing import MainApp as Window
        self.Window = Window()

    def pushButton_YangDoubleSlit_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path+"\data\html\杨氏双缝\demo.html"))
        self.path = path + "\data\html\杨氏双缝\demo.html"
        from Main_YangDoubleSlit import MainApp as Window
        self.Window = Window()

    def pushButton_DoubleSlitDiffraction_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\双缝衍射\demo.html"))
        self.path = path + "\data\html\双缝衍射\demo.html"
        from Main_DoubleSlitDiffraction import MainApp as Window
        self.Window = Window()

    def pushButton_SplittingInterference_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\劈尖干涉\demo.html"))
        self.path = path + "\data\html\劈尖干涉\demo.html"
        from Main_SplittingInterference import MainApp as Window
        self.Window = Window()

    def pushButton_GratingDiffraction_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\光栅衍射\demo.html"))
        self.path = path + "\data\html\光栅衍射\demo.html"
        from Main_GratingDiffraction import MainApp as Window
        self.Window = Window()

    def pushButton_RoundHoleDiffraction_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\圆孔衍射\demo.html"))
        self.path = path + "\data\html\圆孔衍射\demo.html"
        from Main_RoundHoleDiffraction import MainApp as Window
        self.Window = Window()

    def pushButton_MichelsonInterferometer_Clicked(self):
        self.webEngineView.load(QtCore.QUrl.fromLocalFile(path + "\data\html\迈克尔逊干涉\demo.html"))
        self.path = path + "\data\html\迈克尔逊干涉\demo.html"
        from Main_MichelsonInterferometer import MainApp as Window
        self.Window = Window()


    def pushButton_in_Clicked(self):
        self.Window.showFullScreen()
        # self.hide()


    # def pushButton_recover_Cilicked(self):
    #     self.SpinBox_x.setProperty("value", 0.002)
    #     self.SpinBox_d.setProperty("value", 0.001)
    #     self.SpinBox_n.setProperty("value", 1.00)
    #     self.SpinBox_f.setProperty("value", 50.0)
    #     self.SpinBox_N.setProperty("value", 8)
    #     self.SpinBox_lamda.setProperty("value", 487.2)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.show()
    sys.exit(app.exec())