# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : model.py
@Author : FF
@Time : 2023/1/16 18:11
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, func
from sqlalchemy.types import String, Integer, DateTime

Base = declarative_base()


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title_tc = Column(String, comment="物品名称（繁体中文）")
    ref_url_tc = Column(String, comment="详情页url")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Culinary(Base):
    __tablename__ = 'culinary'

    id = Column(Integer, primary_key=True)
    title_tc = Column(String, nullable=False)
    material_1_id = Column(Integer)
    material_1_type = Column(String)
    material_1_title_tc = Column(String)
    material_1_weight= Column(Integer)
    material_2_id = Column(Integer)
    material_2_type = Column(String)
    material_2_title_tc = Column(String)
    material_2_weight = Column(Integer)
    material_3_id = Column(Integer)
    material_3_type = Column(String)
    material_3_title_tc = Column(String)
    material_3_weight = Column(Integer)
    material_4_id = Column(Integer)
    material_4_type = Column(String)
    material_4_title_tc = Column(String)
    material_4_weight = Column(Integer)
    material_5_id = Column(Integer)
    material_5_type = Column(String)
    material_5_title_tc = Column(String)
    material_5_weight = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class MaterialGroup(Base):
    __tablename__ = 'materialgroup'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False, unique=True)
    group_title_tc = Column(String, nullable=False)
    item_id = Column(Integer, index=True)
    item_title_tc = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
