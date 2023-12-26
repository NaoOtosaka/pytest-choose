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
        "--fc-allow-path",
        action="append",
        default=[],
        help="Whitelist rule file path, supports duplicate input"
    )
    group.addoption(
        "--fc-block-path",
        action="append",
        default=[],
        help="Blacklist rule file path, supports duplicate input"
    )


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: List["pytest.Item"]):
    if config.getoption('--fc') == 'on':
        origin_count = len(items)
        count = 0
        allow_list_path = config.getoption('--fc-allow-path')
        block_list_path = config.getoption('--fc-block-path')
        coding = config.getoption('--fc-coding')
        terminal_write(session, '\n', prefix=False)
        allow_list_parse = ChooseFileAnalysis(allow_list_path, session, encoding=coding).parse()
        block_list_parse = ChooseFileAnalysis(block_list_path, session, encoding=coding, is_filter_file=True).parse()
        if allow_list_parse or block_list_parse:
            for item in items[:]:
                if ItemFilter(allow_list_parse, item, block_list_parse).filter():
                    continue
                del items[items.index(item)]
                count += 1
            terminal_write(session, f'Filter {count} cases and collect {origin_count - count} cases', bold=True)
        else:
            terminal_write(session, 'Unsupported file format, please use JSON format file', red=True, bold=True)
            terminal_write(session, 'Not filtered')
