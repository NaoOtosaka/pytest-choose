"""
@File: filter.py
@Author: c25555
@Description: 

"""
from typing import Union

import pytest


class ItemFilter:
    support_key = ['class', 'function']

    def __init__(self, parse: dict, item: pytest.Item, filter_parse: Union[dict, bool] = None):
        self.parse = parse
        self.filter_parse = {} if not filter_parse else filter_parse
        self.item = item

    def _class_filter(self) -> bool:
        cls = self.item.parent.name if isinstance(self.item.parent, pytest.Class) else ''
        if not cls:
            return False
        if cls in self.filter_parse['class']:
            return False
        return True

    def _function_filter(self) -> bool:
        item_name = self.item.originalname if hasattr(self.item, 'originalname') else self.item.name
        if item_name in self.filter_parse['function']:
            return False
        return True

    def _class_choose(self) -> bool:
        cls = self.item.parent.name if isinstance(self.item.parent, pytest.Class) else ''
        if not cls:
            return False
        if cls not in self.parse['class']:
            return False
        return True

    def _function_choose(self) -> bool:
        item_name = self.item.originalname if hasattr(self.item, 'originalname') else self.item.name
        if item_name not in self.parse['function']:
            return False
        return True

    def filter(self) -> bool:
        result = False
        if self.parse:
            if 'class' in self.parse.keys():
                result = self._class_choose()
            if 'function' in self.parse.keys():
                result = True if result else self._function_choose()
        if self.filter_parse:
            if 'class' in self.filter_parse.keys():
                result = self._class_filter()
            if 'function' in self.filter_parse.keys():
                result = False if not result else self._function_filter()
        return result