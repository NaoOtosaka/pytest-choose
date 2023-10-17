"""
@File: plugin.py
@Author: Azusa
@Description:

"""
import pytest
from typing import List

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
        help="'File encoding, default 'utf-8'"
    )
    group.addoption(
        "--fc-path",
        action="store",
        default="./choose.json",
        help="'File Path, default './choose.json'"
    )


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: List["pytest.Item"]):
    if config.getoption('--fc') == 'on':
        origin_count = len(items)
        count = 0
        path = config.getoption('--fc-path')
        terminal_write(session, '\n', prefix=False)
        terminal_write(session, f'Cases list: {path}', bold=True)
        parse = ChooseFileAnalysis(path, session, encoding=config.getoption('--fc-coding')).parse()
        if parse:
            for item in items:
                cls = item.parent.name if isinstance(item.parent, pytest.Class) else ''
                if cls and cls in parse['class']:
                    continue
                if item.name in parse['function']:
                    continue
                del items[items.index(item)]
                count += 1
            terminal_write(session, f'Filter {count} cases and collect {origin_count - count} cases', bold=True)
        else:
            terminal_write(session, 'Unsupported file format, please use JSON format file', red=True, bold=True)
            terminal_write(session, 'Not filtered')
