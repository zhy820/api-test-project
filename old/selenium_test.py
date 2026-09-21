from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.common.keys import Keys


def check_chrome_driver():
    try:
        # 尝试启动 Chrome 浏览器
        driver = webdriver.Chrome()
        print("ChromeDriver 安装成功!")
        print(f"Chrome 浏览器版本: {driver.capabilities['browserVersion']}")
        print(f"ChromeDriver 版本: {driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]}")
        # 访问测试页面验证功能
        driver.get("https://www.baidu.com")
        print("测试页面加载成功，标题:", driver.title)
        # 等待 5 秒钟以便查看浏览器
        time.sleep(5)

        #找到输入框输入“selelium”
        # time.sleep(5)
        # 仅用于find_element 方法，每半秒钟查询一次直到10s超时
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "kw")
        element.send_keys("selenium")

        #element = driver.find_element(By.CLASS_NAME, "新闻")
        element = driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(1)")
        #element.click()
        print(element.text)

        # 关闭浏览器
        driver.quit()
        return True
    except WebDriverException as e:
        print("ChromeDriver 验证失败，错误信息:")
        print(str(e))
        return False


if __name__ == '__main__':
    # 执行验证
    if check_chrome_driver():
        print("验证通过，环境配置正确")
    else:
        print("验证未通过，请检查以下问题:")
        print("1. 是否已安装 ChromeDriver?")
        print("2. ChromeDriver 是否已添加到系统 PATH?")
        print("3. Chrome 浏览器版本是否与 ChromeDriver 匹配?")
        print("4. 是否有其他 Chrome 进程未关闭?")
