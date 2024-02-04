# pytest-choose
<a href="https://github.com/NaoOtosaka/pytest-choose/blob/master/docs/README_EN.md">English</a> | 简体中文

为pytest提供基于文本文件收集用例的能力

> v0.1.0升级说明：
> - v0.0.x版本升级至v0.1.0版本时，请将原`--fc-path`参数更改为`--fc-allow-path`
> - 升级后规则文件不强制要求完全包含`class` `function`块，按需编写即可

## 1.安装

```shell
pip install pytest-choose
```

## 2.参数说明

| Parameter       | Description                   |
|-----------------|-------------------------------|
| --fc            | 默认'off'，关闭文件选择。可选项'off', 'on' |
| --fc-coding     | 文件编码, 默认 'utf-8'              |
| --fc-allow-path | 白名单文件路径, 支持多次传入以应用多个规则文件      |
| --fc-block-path | 黑名单文件路径, 支持多次传入以应用多个规则文件      |

## 3.过滤文件模板
### 3.1.JSON
```json
{
  "@说明": [
    "@注释以‘@’符开头声明"
  ],
  "path": [
    "@下方填写用例路径",
    "TestClassName"
  ],
  "marker": [
    "@下方填写需要选中的测试tag",
    "test_function_name"
  ],
  "class": [
    "@下方填写需要执行的测试类",
    "TestClassName"
  ],
  "function": [
    "@下方填写需要执行的测试方法",
    "test_function_name"
  ]
}
```

## 4.示例
创建测试文件：
```python
# test_demo.py
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

```

### 4.1.基本使用

创建文件`choose.json`，用于选择用例:

```json
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
pytest --fc="on" --fc-allow-path="./choose.json" --fc-coding="utf-8"
```

测试结果如下:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\PytestDev\pytest-choose
plugins: choose-0.1.0
collecting ... 

[pytest-choose] <Allow list>: choose.json -> Successful use of rules
[pytest-choose] Filter 5 cases and collect 2 cases
collected 7 items

cases\test_choose.py ..                            [100%] 
======================== 2 passed in 0.03s ======================== 
```
### 4.2.黑名单过滤

创建文件`filter.json`，用于过滤用例:

```json
{
  "function": [
    "test_demo_3",
    "test_demo_4",
    "test_demo_5"
  ]
}
```

执行测试:

```shell
pytest --fc="on" --fc-block-path="./filter.json" --fc-coding="utf-8"
```

测试结果如下:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\PytestDev\pytest-choose
plugins: choose-0.1.0
collecting ... 

[pytest-choose] <Block list>: filter.json -> Successful use of rules
[pytest-choose] Filter 3 cases and collect 4 cases
collected 7 items

cases\test_choose.py ....                          [100%] 
======================== 4 passed in 0.05s ======================== 
```


### 4.3.黑白名单过滤
- 当同时使用黑白名单时，过滤结果为两个规则的差集（{x∣x∈白名单,且x∉黑名单}）
- 当黑白名单无重合项时，默认黑名单失效。

创建文件`choose.json`，用于选择用例:

```json
{
  "function": [
    "test_demo_2",
    "test_demo_3"
  ]
}
```
创建文件`filter.json`，用于过滤用例:

```json
{
  "function": [
    "test_demo_3",
    "test_demo_4",
    "test_demo_5"
  ]
}
```

执行测试:

```shell
pytest --fc="on" --fc-allow-path="./choose.json" --fc-block-path="./filter.json" --fc-coding="utf-8"
```

测试结果如下:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\PytestDev\pytest-choose
plugins: choose-0.1.0


[pytest-choose] <Allow list>: choose.json -> Successful use of rules
[pytest-choose] <Block list>: filter.json -> Successful use of rules
[pytest-choose] Filter 6 cases and collect 1 cases
collected 7 items

cases\test_choose.py .                             [100%] 
======================== 1 passed in 0.04s ======================== 
```

### 4.4.多规则文件过滤
- 当传入规则文件不存在时，仅会抛出响应日志，不会中止测试
- 当传入同类型的多个规则文件时，生效规则为该类型所有规则文件的并集

创建文件`choose.json`，`choose_1.json`，用于选择用例:

```json
{
  "function": [
    "test_demo_2",
    "test_demo_3"
  ]
}
```
```json
{
  "function": [
    "test_demo_4"
  ]
}
```
创建文件`filter.json`，用于过滤用例:

```json
{
  "function": [
    "test_demo_3",
    "test_demo_4",
    "test_demo_5"
  ]
}
```
同时传入不存在的文件`filter_1.json`，执行测试:

```shell
pytest --fc="on" --fc-allow-path="./choose.json" --fc-allow-path="./choose_1.json" --fc-block-path="./filter.json" --fc-block-path="./filter_1.json" --fc-coding="utf-8"
```

测试结果如下:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\PytestDev\pytest-choose
plugins: choose-0.1.0


[pytest-choose] <Allow list>: choose.json -> Successful use of rules
[pytest-choose] <Allow list>: choose_1.json -> Successful use of rules
[pytest-choose] <Block list>: filter.json -> Successful use of rules
[pytest-choose] <Block list>: filter_1.json -> No such file or directory
[pytest-choose] Filter 6 cases and collect 1 cases
collected 7 items

cases\test_choose.py .                              [100%] 
======================== 1 passed in 0.04s ======================== 
```

### 4.5.用例路径及Tag过滤
- 当传入path参数中路径不存在时会在用例收集阶段触发对应异常
- Tag参数以and方式拼接

创建文件`choose.json`用于选择用例:

```json
{
  "path": [
    "./cases/"
  ],
  "marker": [
    "test",
    "not testt"
  ],
  "function": [
    "test_demo_2",
    "test_demo_3"
  ]
}
```

测试结果如下:
```shell              
======================= test session starts =======================
platform win32 -- Python 3.9.6, pytest-7.4.3, pluggy-1.3.0
rootdir: D:\Project\PytestDev\pytest-choose
plugins: choose-0.2.0
collecting ... 

[pytest-choose] <Allow list>: choose.json -> Successful use of rules
[pytest-choose] Filter 5 cases and collect 2 cases
[pytest-choose] Use marker: test and not testt
[pytest-choose] Use case path: ['./cases/']
collected 7 items / 1 deselected / 6 selected                                                                                                                                                             

cases\test_choose.py .                              [100%] 
======================== 1 passed in 0.04s ======================== 
```

## 许可证

pytest-choose使用 GPLv3 许可证

Copyright © 2023 by Azusa.