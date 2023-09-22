from PyQt5.QtWidgets import QSizePolicy , QWidget , QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.plt = plt
        # 设置图窗和坐标
        self.fig, self.ax = plt.subplots()
        # 设置画布边缘颜色
        self.fig.patch.set_facecolor('#D7E7E8')
        # 设置画布背景颜色
        self.plt.rcParams['axes.facecolor'] = '#D7E7E8'
        # 画布的初始化
        FigureCanvas.__init__(self, self.fig)
        # 将小部件定义为可扩展
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 通知系统更新的策略
        FigureCanvas.updateGeometry(self)



class MPL_WIDGET(QWidget):
    def __init__(self, parent=None):
        # Qt MainWindow小部件的初始化
        QWidget.__init__(self, parent)
        # 将画布设置为 Matplotlib 小部件
        self.canvas = MplCanvas()
        # 创建垂直框布局
        self.vbl = QVBoxLayout()
        # 将 MPL 小部件添加到垂直框
        self.vbl.addWidget(self.canvas)
        # 将布局设置为垂直框
        self.setLayout(self.vbl)



