"""
@File: filter.py
@Author: c25555
@Description: 

"""
from typing import Union

import pytest


class ItemFilter:
    def __init__(self, parse: dict, item: pytest.Item, filter_parse: Union[dict, bool] = None):
        self.parse = parse
        self.filter_parse = {} if not filter_parse else filter_parse
        self.item = item

    def _class_filter(self) -> bool:
        cls = self.item.parent.name if isinstance(self.item.parent, pytest.Class) else ''
        if not cls:
            return True
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
        result = None
        if self.parse:
            result = self._class_choose()
            result = self._function_choose() if not result else result
        if (result is not False) and self.filter_parse:
            result = self._class_filter() if (result is None) or result else result
            result = self._function_filter() if result else result
        return result
