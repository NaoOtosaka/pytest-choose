"""
@File: analysis.py
@Author: Azusa
@Description: 

"""
import json
import pytest
import pathlib
from typing import Union, TextIO

from . import RULE_TYPE
from .terminal_io import terminal_write


class ChooseFileAnalysis:
    _support_type = [
        '.json',
    ]

    def __init__(
            self,
            file_path: list,
            session: pytest.Session,
            encoding: str = 'utf-8',
            is_filter_file: bool = False
    ):
        self.file_path = [pathlib.PurePath(path) for path in file_path]
        self.session = session
        self.is_filter_file = is_filter_file
        self.encoding = encoding

        self.analysis_result: dict = {t: [] for t in RULE_TYPE}

    def __msg(self, msg: str) -> str:
        if self.is_filter_file:
            return f'<Block list>: {msg}'
        else:
            return f'<Allow list>: {msg}'

    def __get_file_type(self, path: pathlib.PurePath) -> Union[str, bool]:
        """
        获取规则文件格式

        :param path: 规则文件路径
        :return: 文件后缀
        """
        if (t := path.suffix) in self._support_type:
            return t
        terminal_write(
            self.session,
            self.__msg(f'Unsupported file format, please check the file format -> {path.as_posix()}'),
            red=True
        )
        return False

    def __get_file_object(self, path: pathlib.PurePath) -> Union[TextIO, bool]:
        """
        初始化规则文件对象

        :param path: 规则文件路径
        :return: 规则文件对象
        """
        _path = path.as_posix()
        try:
            f_obj = open(_path, encoding=self.encoding)
        except FileNotFoundError as e:
            terminal_write(self.session, self.__msg(f"{_path} -> {e.strerror}"), red=True)
            return False
        else:
            terminal_write(self.session, self.__msg(f"{_path} -> Successful use of rules"), bold=True)
            return f_obj

    @staticmethod
    def __json_parse(f_obj: Union[TextIO, bool]) -> dict:
        """
        JSON格式规则文件解析，转字典

        :param f_obj: 文件对象
        :return: 解析后字典
        """
        if not f_obj:
            return {}
        return json.loads(f_obj.read())

    @staticmethod
    def __ini_parse(f_obj: TextIO) -> dict:
        pass

    def __parse_interface(self, t: str, path: pathlib.PurePath) -> dict:
        """
        解析接口

        :param t: 文件格式
        :param path: 文件路径
        :return: 解析后字典
        """
        if t == '.json':
            return self.__json_parse(self.__get_file_object(path))
        elif t == '.ini':
            return self.__ini_parse(self.__get_file_object(path))

    def __update_result(self, rule_dict: dict):
        """
        更新规则集，将新的规则字典更新至规则中并去重

        :param rule_dict: 规则字典
        :return:
        """
        for t in RULE_TYPE:
            if t not in rule_dict.keys():
                continue
            self.analysis_result[t] = list(set(rule_dict[t] + self.analysis_result[t]))  # 去重

    def parse(self) -> Union[bool, dict]:
        flag = False
        # 更新规则列表
        for path in self.file_path:
            if t := self.__get_file_type(path):
                rule = self.__parse_interface(t, path)
                self.__update_result(rule)
        # 判断更新后规则列表是否非空
        for t in RULE_TYPE:
            if self.analysis_result[t]:
                flag = True
        return self.analysis_result if flag else False
