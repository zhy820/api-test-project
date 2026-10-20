from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging

# 配置日志，而不是简单的 print，这在高级测试中很重要
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def handle_dynamic_element(driver):
    """
    处理动态加载元素的核心函数
    """
    # 1. 设置全局页面加载超时，防止因网络问题无限等待
    driver.set_page_load_timeout(30)

    try:
        # 2. 访问页面（如果笔试提供了具体的URL，请替换这里）
        # 如果笔试是要求写在某个特定网站上，请换成那个URL
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        # 3. 点击触发动态加载的按钮
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()
        logging.info("已点击触发按钮，开始等待动态元素...")

        # 4. 核心：处理动态加载
        # 设置最长等待时间为 15 秒
        wait = WebDriverWait(driver, 15, poll_frequency=0.5)

        # 等待元素可见
        finish_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        # 5. 获取元素文本
        element_text = finish_element.text
        logging.info(f"✅ 成功获取动态元素内容: {element_text}")
        return element_text

    except TimeoutException:
        logging.error("❌ 超时错误：动态元素在规定时间内未能加载出来。")
        # 在高级测试中，这里通常会截图保存现场，方便排查
        driver.save_screenshot("dynamic_element_timeout.png")
        return None
    except WebDriverException as e:
        logging.error(f"❌ WebDriver 异常（可能是网络或浏览器崩溃）: {e}")
        return None


if __name__ == "__main__":
    # 初始化浏览器
    driver = webdriver.Chrome()
    try:
        handle_dynamic_element(driver)
    finally:
        # 确保无论发生什么，浏览器最后都能关闭
        driver.quit()

if __name__ == "__main__":
    handle_dynamic_element()