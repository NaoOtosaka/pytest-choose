"""
@File: analysis.py
@Author: Azusa
@Description: 

"""
import json
import pathlib
from typing import Union

import pytest

from .terminal_io import terminal_write


class ChooseFileAnalysis:
    _support_type = [
        '.json'
    ]

    def __init__(self, file_path: str, session: pytest.Session, encoding: str = 'utf-8', is_filter_file: bool = False):
        self.file_path = pathlib.PurePath(file_path)
        self.session = session
        self.is_filter_file = is_filter_file

        self.f_type = self.file_path.suffix
        self.f_obj = ""
        try:
            self.f_obj = open(self.file_path.as_posix(), encoding=encoding)
        except FileNotFoundError as e:
            terminal_write(session, self.__msg(e.strerror), red=True)
        else:
            terminal_write(session, self.__msg(self.file_path.as_posix()), bold=True)

    def __msg(self, msg: str) -> str:
        if self.is_filter_file:
            return f'<Filter list>: {msg}'
        else:
            return f'<Cases list>: {msg}'

    def __json_parse(self) -> dict:
        return json.loads(self.f_obj.read())

    def parse(self) -> Union[bool, dict]:
        if isinstance(self.f_obj, str):
            return False
        if self.f_type not in self._support_type:
            print('Unsupported file format, please use JSON format file')
            return False
        if self.f_type == '.json':
            return self.__json_parse()
