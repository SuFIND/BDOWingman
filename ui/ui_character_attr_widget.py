# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design/character_attr_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CharacterAttrWidget:
    def __init__(self):
        self.maxBearLoadEdit = None
        self.maxBearLoadLabel = None
        self.curBearLoadLabel = None
        self.curBearLoadEdit = None
        self.gridLayout = None
        self.gridLayout_2 = None
        self.frame = None
        self.line = None
        self.charecterLabel = None
        self.verticalLayout = None
        self.verticalLayout_2 = None

    def setupUi(self, characterAttrWidget):
        characterAttrWidget.setObjectName("characterAttrCtrl")
        # characterAttrCtrl.resize(472, 158)

        # 控件内部垂直布局
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(characterAttrWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # 角色属性 - 标签
        self.charecterLabel = QtWidgets.QLabel(characterAttrWidget)
        self.charecterLabel.setMaximumHeight(25)
        self.charecterLabel.setObjectName("characterLabel")
        self.verticalLayout.addWidget(self.charecterLabel)

        # 角色属性 - 标签下方的水平分割线线
        self.line = QtWidgets.QFrame(characterAttrWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        # 角色属性 - 负重和最大负重的展示布局设置
        self.frame = QtWidgets.QFrame(characterAttrWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # 角色属性 - 表单内 - LineEdit - 角色负重（LTS）
        self.curBearLoadEdit = QtWidgets.QLineEdit(self.frame)
        self.curBearLoadEdit.setObjectName("curBearLoadEdit")
        self.gridLayout.addWidget(self.curBearLoadEdit, 0, 1, 1, 1)

        # 角色属性 - 表单内 - 标签 - 角色负重（LTS）
        self.curBearLoadLabel = QtWidgets.QLabel(self.frame)
        self.curBearLoadLabel.setObjectName("curBearLoadLabel")
        self.gridLayout.addWidget(self.curBearLoadLabel, 0, 0, 1, 1)

        # 角色属性 - 表单内 - 标签 - 角色最大负重（LTS）
        self.maxBearLoadLabel = QtWidgets.QLabel(self.frame)
        self.maxBearLoadLabel.setObjectName("maxBearLoadLabel")
        self.gridLayout.addWidget(self.maxBearLoadLabel, 1, 0, 1, 1)

        # 角色属性 - 表单内 - LineEdit - 角色最大负重（LTS）
        self.maxBearLoadEdit = QtWidgets.QLineEdit(self.frame)
        self.maxBearLoadEdit.setObjectName("maxBearLoadEdit")
        self.gridLayout.addWidget(self.maxBearLoadEdit, 1, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(characterAttrWidget)
        QtCore.QMetaObject.connectSlotsByName(characterAttrWidget)

    def retranslateUi(self, characterAttrWidget):
        _translate = QtCore.QCoreApplication.translate
        characterAttrWidget.setWindowTitle(_translate("characterAttrCtrl", "Form"))
        self.charecterLabel.setText(_translate("characterAttrCtrl", "角色属性"))
        self.curBearLoadLabel.setText(_translate("characterAttrCtrl", "角色负重（LTS）"))
        self.maxBearLoadLabel.setText(_translate("characterAttrCtrl", "角色最大负重（LTS）"))