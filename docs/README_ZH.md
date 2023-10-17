# pytest-choose
<a href="https://github.com/NaoOtosaka/pytest-choose/blob/master/README.md">English</a> | 简体中文

为pytest提供基于文本文件收集用例的能力

## 安装

```shell
pip install pytest-choose
```

## 示例
创建测试文件：

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

创建文件`choose.json`，用于选择用例:

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

执行测试:

```shell
pytest --fc="on" --fc-path="./choose.json" -fc-coding="utf-8"
```

测试结果如下:
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

## 参数说明

| Parameter | Description                   |
| --- |-------------------------------|
| --fc | 默认'off'，关闭文件选择。可选项'off', 'on' |
| --fc-path | 文件路径, 默认 './choose.json'      |
| --fc-coding | 文件编码, 默认 'utf-8'              |

## 许可证

pytest-choose使用 [GPLv3](/C:/Users/c25555/AppData/Local/Programs/Joplin/resources/app.asar/LICENSE "./LICENSE")许可证

Copyright © 2023 by Azusa.