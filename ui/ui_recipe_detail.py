# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design/item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecipeDetail(object):
    def setupUi(self, RecipeDetail):
        RecipeDetail.setObjectName("RecipeDetail")
        RecipeDetail.setWindowModality(QtCore.Qt.NonModal)
        self.gridLayout_2 = QtWidgets.QGridLayout(RecipeDetail)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(RecipeDetail)
        self.title.setMaximumHeight(25)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.line = QtWidgets.QFrame(RecipeDetail)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame = QtWidgets.QFrame(RecipeDetail)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_frame = QtWidgets.QFrame(self.frame)
        self.info_frame.setMaximumHeight(50)
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.info_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.info_frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.minProcessingTimes = QtWidgets.QLabel(self.info_frame)
        self.minProcessingTimes.setObjectName("minProcessingTimes")
        self.horizontalLayout.addWidget(self.minProcessingTimes)
        self.label_2 = QtWidgets.QLabel(self.info_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.info_frame)
        self.output_frame = QtWidgets.QFrame(self.frame)
        self.output_frame.setMaximumHeight(50)
        self.output_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_frame.setObjectName("output_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.output_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.output_frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.output_frame)
        self.detail_frame = QtWidgets.QFrame(self.frame)
        self.detail_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detail_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detail_frame.setObjectName("detail_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.detail_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.detail_gridLayout = QtWidgets.QGridLayout()
        self.detail_gridLayout.setObjectName("detail_gridLayout")
        self.label_4 = QtWidgets.QLabel(self.detail_frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_4.setObjectName("label_4")
        self.detail_gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.detail_gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.detail_frame)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RecipeDetail)
        QtCore.QMetaObject.connectSlotsByName(RecipeDetail)

    def retranslateUi(self, RecipeDetail):
        _translate = QtCore.QCoreApplication.translate
        RecipeDetail.setWindowTitle(_translate("RecipeDetail", "Form"))
        self.title.setText(_translate("RecipeDetail", "????????????"))
        self.label.setText(_translate("RecipeDetail", "????????????????????????"))
        self.minProcessingTimes.setText(_translate("RecipeDetail", "??????"))
        self.label_2.setText(_translate("RecipeDetail", "??????????????????"))
        self.label_3.setText(_translate("RecipeDetail", "????????????"))
        self.label_4.setText(_translate("RecipeDetail", "?????????"))
