"""
@File: terminal_io.py
@Author: Azusa
@Description: 

"""
import pytest
from . import __plugin_name__

prefix_str = f"[{__plugin_name__}] "

def terminal_write(
        session: pytest.Session,
        message, prefix: bool = True,
        red: bool = False, green: bool = False,
        bold: bool = False, light: bool = False,
        blink: bool = False, invert: bool = False
):
    session.config.pluginmanager.getplugin("terminalreporter").write(
        f'{prefix_str if prefix else ""}{message}\n',
        red=red, green=green,
        bold=bold, light=light,
        blink=blink, invert=invert
    )
