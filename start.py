# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : start.py
@Author : FF
@Time : 2023/1/14 10:39
"""
import logging.handlers
import os

from PyQt5 import QtWidgets
from app.app import App
from utils.applog import Logger
from app.init_resource import init_config, init_resource


def main():
    import sys

    # 初始化日志模块
    Logger.info("app start ...")

    # 初始化配置模块
    config_path = os.environ.get("CFG_PATH", os.path.join(os.getcwd(), "config", "master.toml"))
    config = init_config(config_path)

    # 初始化必要资源
    init_resource(config)

    app = QtWidgets.QApplication(sys.argv)
    main_app = App()
    main_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
