# api-test-project
Just test

# API 自动化测试项目

基于 pytest + requests 的接口自动化测试项目。

## 技术栈

- Python 3.10
- pytest
- requests
- Allure / pytest-html
- YAML 配置

## 项目结构

PythonProject/
├── config/
│   ├── config.yaml
│   └── settings.py
├── utils/
│   ├── __init__.py
│   └── http_client.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_demo.py
│   ├── test_login.py
│   ├── test_params.py
│   └── test_log.py
├── logs/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md


## 环境准备

```bash
pip install -r requirements.txt