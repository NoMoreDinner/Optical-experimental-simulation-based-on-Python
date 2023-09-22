import numpy,math
from Myfun import wavelength_to_map
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication , QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Ui_NewtonRing import Ui_MainWindow
from numpy import pi, linspace ,meshgrid ,sin ,square, sqrt
from matplotlib import font_manager
from ShowHtml import MainApp as Window_Html
import os
# 导入字体管理模块



class MainApp(QMainWindow , Ui_MainWindow):

    def __init__(self):
        self.init = 0
        # "QLabel {border-image: url(img/main.jpg) 0 {0} 28 {1};}"
        self.mainstrtemp = "url(img/100.jpg) 0 {0} 145 {1}"  # 512 10453*184;9961,0=0;8,9953=40
        self.vicestrtemp = "url(img/100.jpg) 0 {0} 145 {1}"  # 206 10203*184;9997,0=0;39,9958=100
        # 宋体字体
        self.SongTi = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
        QMainWindow.__init__(self)

        self._translate = QtCore.QCoreApplication.translate

        self.row = 0;self.col = 0

        self.N = 200
        X = linspace(-4e-3,4e-3, self.N);Y = X
        [x, y] = meshgrid(X, Y)
        r2 = square(x) + square(y)
        self.bin = numpy.where(r2 > 1.5e-5, 0, 1)
        for i in range(0,self.N):
            self.bin[self.N-i-1][i] = 0

        self.X_Mmax = 12e-3  # m
        X_Mmin =  - self.X_Mmax
        Y_Mmax = self.X_Mmax
        Y_Mmin = X_Mmin
        N = self.N  # 清晰度
        # 设置网格
        X = linspace(X_Mmin, self.X_Mmax, N+1000)
        Y = X
        [x, y] = meshgrid(X, Y)
        # 距离中心距离
        self.r = square(x) + square(y)

        self.setupUi(self)
        self.fig()
        self.setpushButton()


    def setpushButton(self):
        self.pushButton_in.clicked.connect(self.pushButton_in_Cilicked)
        self.pushButton_out.clicked.connect(self.pushButton_clear_Cilicked)
        self.pushButton_result.clicked.connect(self.pushButton_result_Cilicked)
        self.pushButton_clear_Cilicked()
        self.pushButton_recover.clicked.connect(self.pushButton_recover_Clicked)
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_return.clicked.connect(self.pushButton_return_Clicked)
        self.pushButton_start.clicked.connect(self.pushButton_start_Clicked)
        self.pushButton_stop.clicked.connect(self.pushButton_stop_Clicked)
        self.pushButton_help.clicked.connect(self.pushButton_help_Clicked)

    def pushButton_help_Clicked(self):
        path = os.path.abspath('.')
        self.Window_Html = Window_Html()
        self.Window_Html.showhtml(path + "\data\html\帮助文档\牛顿环干涉\demo.html")
        self.Window_Html.showFullScreen()


    def pushButton_start_Clicked(self):
        from ShowGif import MainApp as Window_Html
        self.Window_Html = Window_Html()
        self.Window_Html.showgif("data/gif/牛顿环演示图.gif")
        self.Window_Html.show()

    def pushButton_stop_Clicked(self):
        pass

    def pushButton_return_Clicked(self):
        self.close()
        # from main import MainApp as MainWindow
        # self.window = MainWindow()
        # self.window.show()

    def pushButton_recover_Clicked(self):
        self.SpinBox_lambda.setProperty("value", 589.3)
        self.SpinBox_R.setProperty("value", 3.0)

    def fig(self):  # 计算图像

        N = self.N
        I0 = 1.0   # 初始光强
        R = self.SpinBox_R.value()  # 曲率半径
        lamda = self.SpinBox_lambda.value() * 1.E-9  # 波长 nm -》 m
        self.lamda = lamda
        n = self.RefractiveIndex()
        x = self.horizontalSlider.value()
        y = self.verticalSlider.value()
        x = x-1
        y = y-1
        r = self.r[y:y+N:1,x:x+N:1]

        I = I0 * square(sin(pi * r * n/ (R * lamda)))
        I = I * self.bin
        # 生成对应波长的色矩
        my_cmap = wavelength_to_map(self.SpinBox_lambda.value())

        I[:, int(N / 2)] = 0
        I[int(N / 2)] = 0


        # 创建图像
        mpl = self.mplwidget.canvas
        # 清除当前图像
        mpl.ax.clear()
        # 设置图像参数
        mpl.ax.imshow(I, cmap=my_cmap, interpolation='bessel', origin='lower', vmin=0, vmax=1)
        mpl.ax.axis('off')  # 去掉坐标轴
        mpl.draw()  # 显示


        ## 改变主尺与副尺的位置
        x0 = 2 # cm
        distance = self.X_Mmax*200*5/6/1000*x  # cm
        r2 = r[int(N/2),int(N/2)]
        num = int(abs(numpy.floor(n * r2/lamda/R)))
        self.label_RingNum.setText(self._translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">" +
                                              str(num) +
                                              "</span></p></body></html>"))
        temp = 11800/100
        self.location = str(x0 * 10 + distance * 10)
        right = round(12745 - x0*temp - distance*temp)
        left = 12945 - right
        self.mainstr = self.mainstrtemp.format(right, left)
        self.label_main_1.setStyleSheet(("QLabel {border-image: " + self.mainstr + ";}"))

        distance = distance*10 - math.floor(distance*10)
        right = 12745 - round(distance*11800)
        left = 12945 - right
        self.vicestr = self.vicestrtemp.format(right, left)
        self.label_vice_1.setStyleSheet(("QLabel {border-image: " + self.vicestr + ";}"))




        # data = numpy.array([[24.04, 35.92],[24.2,35.78],[24.36,35.64],[24.52,35.46],[24.68,35.3],
        #                     [24.84,35.14],[25.02,34.98],[25.2,34.78],[25.4,34.6],[25.58,34.4]])
        # for i in range(0, 10):
        #     for j in range(0, 2):
        #         self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))




    def pushButton_in_Cilicked(self):  #  写入数据
        self.tableWidget.setItem(self.row, self.col, QTableWidgetItem(self.location))
        if self.col == 0:
            self.row = self.row + 1
        else:
            self.row = self.row - 1
        if self.row > 19:
            self.col = 1
            self.row = self.row - 1

    def pushButton_clear_Cilicked(self):  #  清除全部的数据
        self.row = 0;self.col = 0
        for i in range(0,20):
            for j in range(0,3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(""))

    def pushButton_result_Cilicked(self):
        mode = self.comboBox_h.currentIndex()
        DATA = numpy.empty([1,1])
        DATA = numpy.delete(DATA, 0, 0)
        L = DATA
        k = 0
        for i in range(0, 20):
            left = self.tableWidget.item(i, 0).text()
            right = self.tableWidget.item(i, 1).text()
            if left != "" and right != "":
                leftnum = float(left)
                rightnum = float(right)
                D = round(abs(leftnum-rightnum),4)
                DATA = numpy.vstack((DATA, [D]))
                L = numpy.vstack((L, [40 - i]))
                k += 1
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(D)))
            else:
                self.show_message()
                return

        if mode == 0:
            R = numpy.empty([1, 1])
            R = numpy.delete(R, 0, 0)
            for i in range(0,k-1-5):
                temp = abs( (square(DATA[i]) - square(DATA[i+5])) / (4*(L[i]-L[i+5])*self.lamda)*1e-6 )
                R = numpy.vstack((R, [temp]))
            resultstr = '<html><head/><body><p align="center"><span style=" font-size:16pt;">您计算的曲率半径为：{0}m</span></p>' \
                        '<p align="center"><span style=" font-size:16pt;">实际曲率半径为：{1}m</span></p>' \
                        '<p align="center"><span style=" font-size:16pt;">误差为：{2}%</span></p></body></html>'
            countR = R.mean()
            realR = self.SpinBox_R.value()
            S = abs(countR-realR)/realR*100
            _translate = QtCore.QCoreApplication.translate
            self.label_result.setText(_translate("MainWindow", resultstr.format(round(countR,4),round(realR,3) , round(S,4))))
        else:
            R = numpy.empty([1, 1])
            R = numpy.delete(R, 0, 0)
            for i in range(0, k - 1 - 5):
                temp = abs((square(DATA[i]) - square(DATA[i + 5])) / (4 * (L[i] - L[i + 5]) * self.lamda) * 1e-6)
                R = numpy.vstack((R, [temp]))
            resultstr = '<html><head/><body><p align="center"><span style=" font-size:16pt;">您计算的介质折射率为：{0}</span></p>' \
                        '<p align="center"><span style=" font-size:16pt;">实际折射率为：{1}</span></p>' \
                        '<p align="center"><span style=" font-size:16pt;">误差为：{2}%</span></p></body></html>'
            countR = R.mean()
            realR = self.SpinBox_R.value()
            countn = realR/countR
            realn = self.RefractiveIndex()
            S = abs(countn - realn) / realn * 100
            _translate = QtCore.QCoreApplication.translate
            self.label_result.setText(_translate("MainWindow", resultstr.format(round(countn,4), round(realn,3), round(S,4))))



    def RefractiveIndex(self):
        if self.comboBox_n.currentIndex() == 0:
            return 1
        elif self.comboBox_n.currentIndex() == 1:
            return 1.5
        else:
            return 1.3

    def show_message(self):
        QMessageBox.critical(self, "错误", "缺少数据")






    @ pyqtSlot("double")
    def on_SpinBox_lambda_valueChanged(self):
        self.fig()

    @ pyqtSlot("double")
    def on_SpinBox_R_valueChanged(self):
        self.fig()

    @ pyqtSlot("double")
    def on_doubleSpinBox_valueChanged(self, value):
        self.horizontalSlider.setProperty("value", int(value*10))
        self.fig()

    @ pyqtSlot("int")
    def on_horizontalSlider_valueChanged(self, value):
        self.doubleSpinBox.setProperty("value", value/10)
        self.fig()

    @ pyqtSlot("double")
    def on_doubleSpinBox_3_valueChanged(self, value):
        self.verticalSlider.setProperty("value", int(self.verticalSlider.maximum() - value*10))
        self.fig()

    @ pyqtSlot("int")
    def on_verticalSlider_valueChanged(self,value):
        self.doubleSpinBox_3.setProperty("value", self.doubleSpinBox_3.maximum()-value/10)
        self.fig()





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainApp()
    MyApplication.showFullScreen()
    sys.exit(app.exec())