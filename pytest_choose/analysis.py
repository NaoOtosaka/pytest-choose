"""
@File: analysis.py
@Author: Azusa
@Description: 

"""
import json
import pathlib


class ChooseFileAnalysis:
    def __init__(self, file_path: str, encoding: str = 'utf-8'):
        self.file_path = pathlib.PurePath(file_path)

        self.f_type = self.file_path.suffix
        self.f_obj = open(self.file_path.as_posix(), encoding=encoding)

    def __json_parse(self):
        return json.loads(self.f_obj.read())

    def parse(self):
        if self.f_type == '.json':
            return self.__json_parse()
