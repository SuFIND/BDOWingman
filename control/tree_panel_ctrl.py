# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : tree_panel_ctrl.py
@Author : FF
@Time : 2023/1/19 11:20
"""
from PyQt5 import QtWidgets, QtCore
from ui.ui_tree_widget import ItemTreeViewer


class TreePanelCtrl(QtWidgets.QWidget):
    def __init__(self, parent, *args):
        """
        树项目窗口控件
        :param parent: 父控件
        :param args:
            - flags，见PyQt5.QtWidgets.QWidget形参说明
        """
        super(TreePanelCtrl, self).__init__(parent, *args)
        self.viewer = ItemTreeViewer()
        self.viewer.setupUi(self)

        # 持有的信号
        self.treeItemChangeSig = None

        # 当前可返回的一些数据
        self.cur_selection = None

    def SetTreeItemSelectionSig(self, sig: QtCore.pyqtSignal):
        """
        设置选择项目改变的信号槽
        :param sig:
        :return:
        """
        self.treeItemChangeSig = sig
        self.viewer.treeItemPanel.selectionModel().currentChanged.connect(self.onTreeItemSelectChange)

    def onTreeItemSelectChange(self, current, previous):
        """
        树控件所选项目改变时回调方法
        :param current:
        :param previous:
        :return:
        """
        # current.parent().data()
        # current.row(), current.column(), current.data()
        category = current.parent().data(role=1)
        item_id = current.data(role=1)
        item_name = current.data()
        if self.treeItemChangeSig is None:
            # 如果没有相关的信号定义
            return
        info_key = f"{category}:{item_id}:{item_name}"
        self.cur_selection = info_key
        self.treeItemChangeSig.emit(info_key)

    def GetCurSelection(self):
        """获取当前树形控件的所选项信息"""
        return self.cur_selection
