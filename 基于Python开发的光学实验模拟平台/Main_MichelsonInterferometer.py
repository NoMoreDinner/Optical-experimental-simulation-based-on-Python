import numpy,math
from Myfun import wavelength_to_map
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication , QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Ui_MichelsonInterferometer import Ui_MainWindow
from numpy import pi, linspace ,meshgrid ,sin ,square, sqrt, cos, arctan
from matplotlib import font_manager
from ShowHtml import MainApp as Window_Html
import os
# 导入字体管理模块



class MainApp(QMainWindow , Ui_MainWindow):

    def __init__(self):
        self.init = 0
        # "QLabel {border-image: url(img/main.jpg) 0 {0} 28 {1};}"
        self.mainstrtemp = "url(img/100.jpg) 0 {0} 145 {1}"  #512 10453*184;9961,0=0;8,9953=40
        self.vicestrtemp = "url(img/100.jpg) 0 {0} 145 {1}"  # 206 10203*184;9997,0=0;39,9958=100
        # 宋体字体
        self.SongTi = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
        QMainWindow.__init__(self)

        self.row = 0;self.table_num = 0

        self.N = 200
        self.X_Mmax = 10e-3  # m
        X_Mmin =  - self.X_Mmax
        Y_Mmax = self.X_Mmax
        Y_Mmin = X_Mmin
        N = self.N  # 清晰度
        # 设置网格
        X = linspace(X_Mmin, self.X_Mmax, N)
        Y = X
        [x, y] = meshgrid(X, Y)
        # 距离中心距离
        r = square(x) + square(y)
        f = 0.1  #  焦距m
        self.theta = arctan(sqrt(r)/f)

        self._translate = QtCore.QCoreApplication.translate
        self.maxl = 5e-4
        self.d0 = 1e-3 + 1/2*self.maxl
        self.setupUi(self)
        self.fig()
        self.setpushButton()



    def setpushButton(self):
        self.pushButton_in.clicked.connect(self.pushButton_in_Cilicked)
        self.pushButton_clear.clicked.connect(self.pushButton_clear_Cilicked)
        self.pushButton_result.clicked.connect(self.pushButton_result_Cilicked)
        self.pushButton_clear_Cilicked()
        self.pushButton_recover.clicked.connect(self.pushButton_recover_Clicked)
        self.pushButton_return.clicked.connect(self.pushButton_return_Clicked)
        self.pushButton_start.clicked.connect(self.pushButton_start_Clicked)
        self.pushButton_stop.clicked.connect(self.pushButton_stop_Clicked)
        self.pushButton_help.clicked.connect(self.pushButton_help_Clicked)

    def pushButton_help_Clicked(self):
        path = os.path.abspath('.')
        self.Window_Html = Window_Html()
        self.Window_Html.showhtml(path+"\data\html\帮助文档\迈克尔逊\demo.html")
        self.Window_Html.showFullScreen()

    def pushButton_start_Clicked(self):
        from ShowGif import MainApp as Window_Html
        self.Window_Html = Window_Html()
        self.Window_Html.showgif("data/gif/迈克尔逊演示图.gif")
        self.Window_Html.show()


    def pushButton_stop_Clicked(self):
        pass
        # from PyQt5 import QtGui
        # self.gif.stop()
        # self.label_picture.setPixmap(QtGui.QPixmap("img/迈克尔逊原理图.jfif"))


    def pushButton_recover_Clicked(self):
        self.SpinBox_lambda.setProperty("value", 632.8)

    def pushButton_return_Clicked(self):
        self.close()
        # from main import MainApp as MainWindow
        # self.window = MainWindow()
        # self.window.show()

    def fig(self):  # 计算图像
        N = self.N
        d0 = 1e-3  # 初始距离 m
        maxl = self.maxl
        x = self.horizontalSlider.value()
        lamda = self.SpinBox_lambda.value() * 1.E-9  # 波长 nm -》 m
        self.lamda = lamda
        delta = d0 + x/self.horizontalSlider.maximum()*maxl  # 总长0.1mm


        I = 2*pi * delta  * cos(self.theta)/lamda
        I = square(cos(I))
        # 生成对应波长的色矩
        my_cmap = wavelength_to_map(self.SpinBox_lambda.value())


        num = int(abs(numpy.floor(2*(delta-self.d0)/lamda)))
        self.label_Ni.setText(self._translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">"+
                                             str(num)+
                                             "</span></p></body></html>"))






        # 创建图像
        mpl = self.mplwidget.canvas
        # 清除当前图像
        mpl.ax.clear()
        # 设置图像参数
        mpl.ax.imshow(I, cmap=my_cmap, interpolation='bessel', origin='lower', vmin=0, vmax=1)
        mpl.ax.axis('off')  # 去掉坐标轴
        mpl.draw()  # 显示


        ## 改变主尺与副尺的位置
        x0 = 11 # cm
        distance = delta
        temp = 11800/100
        self.location = str(format((x0 * 10 + distance * 1000), '.4f'))
        right = round(12745 - x0 * temp - distance * temp)
        left = 12945 - right
        self.mainstr = self.mainstrtemp.format(right, left)
        self.label_main_1.setStyleSheet(("QLabel {border-image: " + self.mainstr + ";}"))

        distance = distance*10 - math.floor(distance*10)
        right = 12745 - round(distance * 11800)
        left = 12945 - right
        self.vicestr = self.vicestrtemp.format(right, left)
        self.label_l1.setStyleSheet(("QLabel {border-image: " + self.vicestr + ";}"))

        distance = distance * 100 - math.floor(distance * 100)
        right = 12745 - round(distance * 11800)
        left = 12945 - right
        self.vicestr = self.vicestrtemp.format(right, left)
        self.label_n1.setStyleSheet(("QLabel {border-image: " + self.vicestr + ";}"))





    def pushButton_in_Cilicked(self):  #  写入数据
        if self.table_num == 0:
            self.tableWidget_data_1.setItem(self.row, 1, QTableWidgetItem(self.location))
        else:
            self.tableWidget_data_2.setItem(self.row, 1, QTableWidgetItem(self.location))
        self.row = self.row + 1
        if self.row >= 5:
            self.table_num += 1
            self.row = 0
        if self.table_num >= 2:
            self.table_num = 0
            self.row = 0

    def pushButton_clear_Cilicked(self):  #  清除全部的数据
        self.row = 0;self.table_num = 0
        for i in range(0,5):
            j = 1
            self.tableWidget_data_1.setItem(i, j, QTableWidgetItem(""))
            self.tableWidget_data_2.setItem(i, j, QTableWidgetItem(""))
            self.tableWidget_result.setItem(i, j, QTableWidgetItem(""))

    def pushButton_result_Cilicked(self):
        DATA = numpy.empty([1,1])
        DATA = numpy.delete(DATA, 0, 0)
        k = 0
        for i in range(0, 5):
            left = self.tableWidget_data_1.item(i, 1).text()
            right = self.tableWidget_data_2.item(i, 1).text()
            if left != "" and right != "":
                leftnum = float(left)
                rightnum = float(right)
                D = round(abs(leftnum-rightnum),4)
                DATA = numpy.vstack((DATA, [D]))
                k += 1
                self.tableWidget_result.setItem(i, 1, QTableWidgetItem(str(D)))
            else:
                self.show_message()
                return


        Lamda = numpy.empty([1, 1])
        Lamda = numpy.delete(Lamda, 0, 0)
        for i in range(0,k):
            temp = 2*DATA[i]/250*1e6
            Lamda = numpy.vstack((Lamda, [temp]))
        resultstr = '<html><head/><body><p align="center"><span style=" font-size:16pt;">您计算的激光波长为：{0}nm</span></p>' \
                    '<p align="center"><span style=" font-size:16pt;">实际波长为：{1}nm</span></p>' \
                    '<p align="center"><span style=" font-size:16pt;">误差为：{2}%</span></p></body></html>'
        countLamda = Lamda.mean()
        realLamda = self.SpinBox_lambda.value()
        S = abs(countLamda-realLamda)/realLamda*100
        self.label_result.setText(self._translate("MainWindow", resultstr.format(round(countLamda,4),round(realLamda,3) , round(S,4))))



    def show_message(self):
        QMessageBox.critical(self, "错误", "缺少数据")






    @ pyqtSlot("double")
    def on_SpinBox_lambda_valueChanged(self):
        self.fig()

    @ pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.horizontalSlider.setProperty("value", int(value*10))
        self.fig()

    @ pyqtSlot("int")
    def on_horizontalSlider_valueChanged(self, value):
        self.SpinBox_e.setProperty("value", value/10)
        self.fig()







if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.showFullScreen()
    sys.exit(app.exec())