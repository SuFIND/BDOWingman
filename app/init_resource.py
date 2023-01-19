# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : init_resource.py
@Author : FF
@Time : 2023/1/16 18:04
"""
import os
import sys
import traceback

global global_var
global_var = {}

import toml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from utils.applog import Logger


def init_config(paths: list):
    config = toml.load(paths)
    return config


def init_db(cfg: dict):
    ok = True
    try:
        sql_path = cfg["sqlite"]["path"]
        engine = create_engine(f"sqlite:///{sql_path}")
        Session = sessionmaker(bind=engine)
        session = Session()
        global_var["db_engine"] = engine
        global_var["db_session"] = session
    except SQLAlchemyError as e:
        err = traceback.format_exc()
        Logger.error(err)
        ok = False
    return ok


def init_resource(cfg: dict):
    funcs = [
        init_db
    ]
    for func in funcs:
        ok = func(cfg)
        if ok:
            continue
        sys.exit(-1)
