import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.http_client import session

logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url,timeout=15):
        self.base_url = base_url
        self.timeout = timeout
        self.session = self._get_session()

    def _get_session(self):
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504]
        )

        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", self.timeout)
        logger.info(f"请求: {method} {url}")

        r = self.session.request(method, url, **kwargs)
        logger.info(f"响应: {r.status_code} | 耗时：{r.elapsed.total_seconds():.2f}s")
        return r

    def get(self,path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)