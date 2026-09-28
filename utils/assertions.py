import logging
from jsonschema import (validate, ValidationError)

logger = logging.getLogger(__name__)

def assert_status(r, expected):
    logger.info(f"断言状态码：期望 {expected}, 实际 {r.status_code}")

    assert r.status_code == expected, f"期望状态码 {expected}, 实际 {r.status_code}"

def assert_json_value(r, path, expected):
    keys = path.split(".")
    data = r.json()

    for k in keys:
        data = data[k]
    logger.info(f"断言字段 {path}：期望 {expected}, 实际 {data}")
    assert data == expected, f"期望字段 {path} 值为 {expected}, 实际为 {data}"

def assert_schema(r, schema):
    logger.info("断言 JSON Schema")
    validate(instance = r.json(), schema=schema)

def assert_in(r, text):
    assert text in r.text, f"响应中未包含：{text}"


