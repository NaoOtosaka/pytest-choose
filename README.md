# pytest-choose
English | <a href="https://github.com/NaoOtosaka/pytest-choose/blob/master/docs/README_ZH.md">简体中文</a>

Provide the pytest with the ability to collect use cases based on rules in text files

## Install

```shell
pip install pytest-choose
```

## Example
Create Test Files:

```python
# test_demo.py
class TestDemo:
    def test_demo_1(self):
        print(1)

    def test_demo_2(self):
        print(2)

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

```

Create the choose.json file:

```json
// choose.json
{
  "class": [
    "TestDemo"
  ],
  "function": [
    "test_demo_2",
    "test_demo_3",
    "test_demo_4",
    "test_demo_5"
  ]
}
```

Run tests:

```shell
pytest --fc="on" --fc-path="./choose.json" --fc-coding="utf-8"
```

Running results:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0
rootdir: pytest-choose
plugins: choose-0.0.1
collecting ... 
[pytest-choose] Cases list: ./choose.json
[pytest-choose] Filter 2 cases and collect 5 cases
collected 7 items

cases\test_choose.py .....                         [100%] 
======================== 5 passed in 0.04s ======================== 

```

## Parameter Description

| Parameter | Description |
| --- | --- |
| --fc | Default 'off' for file choose, option: 'on' or 'off' |
| --fc-path | File Path, default './choose.json' |
| --fc-coding | File encoding, default 'utf-8' |

## License

pytest-choose is licensed under [GPLv3](/C:/Users/c25555/AppData/Local/Programs/Joplin/resources/app.asar/LICENSE "./LICENSE").

Copyright © 2023 by Azusa.