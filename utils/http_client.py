import logging
import os
from datetime import datetime

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

#Log file setting
#LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

#Log file DIR
LOG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "logs"
)

os.makedirs(LOG_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

#log file name
LOG_FILE = os.path.join(LOG_DIR, f"test_{timestamp}.log")

logging.basicConfig(
    #level=logging.INFO,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',

    handlers=[
        #输出到文件，指定文件格式，避免输出乱码
        logging.FileHandler(LOG_FILE, encoding="utf-8"),

        #输出到控制台
        logging.StreamHandler()
    ],
    force=True
)

print("日志文件:", LOG_FILE)

logger = logging.getLogger(__name__)

def get_session():
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        #allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

session = get_session()

def request(method, url, **kwargs):
    kwargs.setdefault("timeout", 15)

    logger.info(f"请求：{method} {url}，参数：{kwargs.get('json') or kwargs.get('params')}")
    r = session.request(method, url, **kwargs)

    logger.info(f"响应： {r.status_code}，耗时：{r.elapsed.total_seconds()}秒，响应内容：{r.text}")
    #logger.info(f"响应: {r.status_code}, 耗时: {r.elapsed.total_seconds()}秒, 响应内容: {r.text}".replace("%", "%%"))
    return r

if __name__ == "__main__":
    logger.info("手动测试写入")