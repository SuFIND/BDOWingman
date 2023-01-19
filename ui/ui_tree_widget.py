# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : ui_tree_widget.py
@Author : FF
@Time : 2023/1/16 14:30
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class ItemTreeViewer:
    def __init__(self):
        self.gridLayout = None
        self.verticalLayout = None
        self.searchPanel = None
        self.treeItemPanel = None

    def setupUi(self, widget: QtWidgets.QWidget):
        widget.setMinimumWidth(300)
        widget.setObjectName("itemTreeViewerWidget")

        # set layout
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchPanel = QtWidgets.QPlainTextEdit(widget)
        self.searchPanel.setMaximumHeight(25)
        self.searchPanel.setObjectName("searchPanel")

        self.treeItemPanel = QtWidgets.QTreeView(widget)
        self.treeItemPanel.setObjectName("treeItemPanel")
        self.treeItemPanel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置不可编辑节点

        self.verticalLayout.addWidget(self.searchPanel)
        self.verticalLayout.addWidget(self.treeItemPanel)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        self.searchPanel.setPlaceholderText(_translate("MainWindow", "搜索"))

        model = QtGui.QStandardItemModel(widget)
        model.setHorizontalHeaderLabels(["物品"])

        cate_cuisine = QtGui.QStandardItem()
        cate_cuisine.setText("料理")
        cate_cuisine.setData("culinary", role=1)
        model.appendRow(cate_cuisine)

        test_item = QtGui.QStandardItem()
        test_item.setText("醃製蔬菜")
        test_item.setData("112", role=1)
        cate_cuisine.setChild(0, 0, test_item)

        self.treeItemPanel.setModel(model)

