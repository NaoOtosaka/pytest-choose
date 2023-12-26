"""
@File: main.py
@Author: Azusa
@Description: 

"""
import pytest

pytest.main(
    [
        '--fc', 'on',
        '--fc-allow-path', './choose.json',
        '--fc-allow-path', './choose_1.json/',
        # '--fc-allow-path', './choose_2.json',
        '--fc-block-path', './filter.json',
        '--fc-block-path', './filter_1.json',
    ]
)
