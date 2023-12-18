"""
@File: plugin.py
@Author: Azusa
@Description:

"""
import pytest
from typing import List

from .filter import ItemFilter
from .analysis import ChooseFileAnalysis
from .terminal_io import terminal_write


def pytest_addoption(parser: pytest.Parser):
    group = parser.getgroup(
        'file-choose',
        'Provide the pytest with the ability to collect use cases based on rules in text files'
    )
    group.addoption(
        "--fc",
        action="store",
        default="off",
        help="Default 'off' for file choose, option: 'on' or 'off'"
    )
    group.addoption(
        "--fc-coding",
        action="store",
        default="utf-8",
        help="File encoding, default 'utf-8'"
    )
    group.addoption(
        "--fc-path",
        action="store",
        default="./choose.json",
        help="File Path, default './choose.json'"
    )
    group.addoption(
        "--fc-filter-path",
        action="store",
        default="./filter.json",
        help="Filter file Path, default './filter.json'"
    )


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: List["pytest.Item"]):
    if config.getoption('--fc') == 'on':
        origin_count = len(items)
        count = 0
        path = config.getoption('--fc-path')
        filter_path = config.getoption('--fc-filter-path')
        coding = config.getoption('--fc-coding')
        terminal_write(session, '\n', prefix=False)
        terminal_write(session, f'Cases list: {path}', bold=True)
        terminal_write(session, f'Filter list: {filter_path}', bold=True)
        parse = ChooseFileAnalysis(path, session, encoding=coding).parse()
        filter_parse = ChooseFileAnalysis(filter_path, session, encoding=coding, is_filter_file=True).parse()
        if parse:
            for item in items[:]:
                if ItemFilter(parse, item, filter_parse).filter():
                    continue
                del items[items.index(item)]
                count += 1
            terminal_write(session, f'Filter {count} cases and collect {origin_count - count} cases', bold=True)
        else:
            terminal_write(session, 'Unsupported file format, please use JSON format file', red=True, bold=True)
            terminal_write(session, 'Not filtered')
