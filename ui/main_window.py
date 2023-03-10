# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from control.tree_panel_ctrl import TreePanelCtrl
from control.character_attr_ctrl import CharacterAttrCtrl
from control.recipe_detail_ctrl import RecipeDetailCtrl


class Ui_MainWindow(object):
    def __init__(self):
        self.verticalLayout_right_2 = None
        self.verticalLayout_right_3 = None
        self.frame_2 = None
        self.gridLayout = None
        self.gridLayout_2 = None
        self.tab = None
        self.tabWidget = None
        self.formLayout = None
        self.centralwidget = None
        self.treePanelCtrl = None
        self.characterAttrCtrl = None
        self.recipeDetailCtrl = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 672)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Left Panel 左侧树形控件及搜索框
        self.init_tree_panel_ctrl()

        # Right Panel 右侧操作Panel

        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_right_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_right_3.setObjectName("verticalLayout_right_3")
        self.verticalLayout_right_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_right_2.setObjectName("verticalLayout_right_2")

        # # 右侧 - 角色属性
        self.init_character_attr_ctrl()

        self.init_recipe_detail_ctrl()

        self.verticalLayout_right_3.addLayout(self.verticalLayout_right_2)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget.addTab(self.tab_2, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionbanben1 = QtWidgets.QAction(MainWindow)
        self.actionbanben1.setObjectName("actionbanben1")
        self.menu.addAction(self.actionbanben1)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BDO Wingman"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "计算"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "其他"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.actionbanben1.setText(_translate("MainWindow", "许可"))
        # self.item_change_sig.connect(self.item_select_change)

    def init_recipe_detail_ctrl(self):
        self.recipeDetailCtrl = RecipeDetailCtrl(self.frame_2)
        self.verticalLayout_right_2.addWidget(self.recipeDetailCtrl)

    def init_tree_panel_ctrl(self):
        self.treePanelCtrl = TreePanelCtrl(self.tab)
        self.treePanelCtrl.SetTreeItemSelectionSig(self.item_change_sig)
        self.gridLayout.addWidget(self.treePanelCtrl, 0, 1, 1, 1)

    def init_character_attr_ctrl(self):
        self.characterAttrCtrl = CharacterAttrCtrl(self.frame_2)
        self.verticalLayout_right_2.addWidget(self.characterAttrCtrl)

    def item_select_change(self, sig_str: str):
        print(sig_str)
