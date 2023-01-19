# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : character_attr_ctrl.py
@Author : FF
@Time : 2023/1/19 11:21
"""
from PyQt5 import QtWidgets, QtCore
from ui.ui_character_attr_widget import CharacterAttrWidget


class CharacterAttrCtrl(QtWidgets.QWidget):
    def __init__(self, parent, *args):
        """
        树项目窗口控件
        :param parent: 父控件
        :param args:
            - flags，见PyQt5.QtWidgets.QWidget形参说明
        """
        super(CharacterAttrCtrl, self).__init__(parent, *args)
        self.viewer = CharacterAttrWidget()
        self.viewer.setupUi(self)

        # 持有的信号
        self.bearLoadChangeSig = None

        # 当前可返回的一些数据
        self.curBearLoadVal = 0
        self.maxBearLoadVal = 0

    def SetTreeItemSelectionSig(self, sig: QtCore.pyqtSignal):
        """
        设置文本编辑框改变的信号槽
        :param sig:
        :return:
        """
        self.bearLoadChangeSig = sig
        # TODO
