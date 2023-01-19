# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : main_window.py
@Author : FF
@Time : 2023/1/14 12:07
"""
import traceback

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from ui.main_window import Ui_MainWindow
from app.init_resource import global_var
from utils.applog import Logger
from utils.app_utils import ItemsSigSDK
from db_model.model import Culinary, Items


class App(QMainWindow, Ui_MainWindow):
    # 信号
    item_change_sig = QtCore.pyqtSignal(str)  # 物品切换信号
    detail_change_sig = QtCore.pyqtSignal(str)  # 配方细节修改信号

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        self.item_change_sig.connect(self.handle_item_selection_change)

    def handle_item_selection_change(self, str_sig: str) -> None:
        session = global_var['db_session']
        try:
            sig = ItemsSigSDK(str_sig)
            if not sig.is_valid():
                Logger.warning(f"not valid item selection sig {str_sig}")
                return
            orm = sig.get_item_orm_model()
            if orm in {Culinary}:
                row = session.query(orm).filter(getattr(orm, "id") == sig.get_id()).first()
                if row is None:
                    # TODO 需要做提醒弹窗暂不支持该项目查看配方，并记录
                    return
                print(row)
        except Exception as e:
            session.rollback()
            err = traceback.format_exc()
            Logger.error(err)

    def handle_character_attr_change(self):
        pass

    def handle_detail_val_change(self):
        pass
