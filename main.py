# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QComboBox
import sys
from PyQt5 import uic
from get_NetworkInterface import get_network_interface


class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # super().__init__()
        self.ui = uic.loadUi(r".\ui\ip_scan.ui")  # , self)
        # self.ui.choose_network.activated.connect(self.onActivated)
        self.network_interface()

    # 从get_NetworkInterface获取网卡列表
    def network_interface(self):
        network_interface_list = get_network_interface()
        for i in network_interface_list:
            self.ui.choose_network.addItem(i)

    def fast_scan(self):
        type_a_addr = "10.0.0.0-10.255.255.255"
        type_b_addr = "172.16.0.0-172.31.255.255"
        type_c_addr = "192.168.0.0-192.168.255.255"


app = QApplication([])
m_w = MainWindow()
m_w.ui.show()
app.exec_()
