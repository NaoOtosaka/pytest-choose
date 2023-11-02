"""
@File: filter.py
@Author: c25555
@Description: 

"""
import pytest


class ItemFilter:
    support_key = ['class', 'function']

    def __init__(self, parse: dict, item: pytest.Item):
        self.parse = parse
        self.item = item

    def _class_filter(self) -> bool:
        cls = self.item.parent.name if isinstance(self.item.parent, pytest.Class) else ''
        if cls and cls in self.parse['class']:
            return True
        return False

    def _function_filter(self) -> bool:
        if self.item.name in self.parse['function']:
            return True
        return False

    def filter(self) -> bool:
        result = False
        if 'class' in self.parse.keys():
            result = self._class_filter()
        if 'function' in self.parse.keys():
            result = self._function_filter()
        return result
