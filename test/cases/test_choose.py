"""
@File: test_choose.py
@Author: Azusa
@Description: 

"""
import pytest


class TestDemo:
    def test_demo_1(self):
        print(1)

    @pytest.mark.testt
    def test_demo_2(self):
        print(2)


@pytest.mark.test
def test_demo_3():
    print(3)


def test_demo_4():
    print(4)


def test_demo_5():
    print(5)


def test_demo_6():
    print(6)


def test_demo_7():
    print(7)
