# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : recipe_detail_ctrl.py
@Author : FF
@Time : 2023/1/19 11:22
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_recipe_detail import Ui_RecipeDetail


class RecipeDetailCtrl(QtWidgets.QWidget):
    def __init__(self, parent, *args):
        """
        树项目窗口控件
        :param parent: 父控件
        :param args:
            - flags，见PyQt5.QtWidgets.QWidget形参说明
        """
        super(RecipeDetailCtrl, self).__init__(parent, *args)
        self.viewer = Ui_RecipeDetail()
        self.viewer.setupUi(self)

        # 持有的信号

        # 当前可返回的一些数据
