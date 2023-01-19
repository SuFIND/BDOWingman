# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : app_utils.py
@Author : FF
@Time : 2023/1/19 14:31
"""
from db_model.model import Items, Culinary, MaterialGroup


class ItemsSigSDK:
    orm_relationship = {
        "item": Items,
        "culinary": Culinary,
        "materialgroup": MaterialGroup,
    }

    def __init__(self, sig: str):
        self.sig = sig
        self.item_id = None
        self.item_type = None
        self.item_title_tc = None
        self._parse_sig()

    def _parse_sig(self):
        try:
            self.item_type, self.item_id, self.item_title_tc = self.sig.split(":")
        except Exception as e:
            pass

    def is_valid(self):
        return True if self.item_id is not None else False

    def get_id(self):
        return self.item_id

    def get_belong_to(self):
        return self.item_type

    def get_title_tc(self):
        return self.item_title_tc

    def get_item_orm_model(self):
        return self.orm_relationship.get(self.item_type)
