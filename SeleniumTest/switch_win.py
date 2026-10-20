import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. 导入 Select 类
from selenium.webdriver.support.ui import Select


def switch_window_example():
    driver = webdriver.Chrome()
    driver.get("https://baidu.com")
    original = driver.current_window_handle
    print("原窗口:", original)

    # 2. 用 JS 强行打开一个新标签页（百度的首页上没有现成的链接）
    driver.execute_script("window.open('https://www.baidu.com/s?wd=selenium');")

    # 3. 等待新窗口出现
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: len(d.window_handles) > 1)

    # 4. 切换到新窗口
    for handle in driver.window_handles:
        if handle != original:
            driver.switch_to.window(handle)
            sleep(20)
            break

    print("已切换到新窗口:", driver.current_url)
    sleep(10)

    for handle in driver.window_handles:
        if handle == original:
            driver.switch_to.window(handle)
            sleep(20)
            break

    print("已切换到原窗口:", driver.current_url)

def drollwin_selector():
    driver = webdriver.Chrome()
    # 国内可访问的测试下拉框页面
    driver.get("https://sahitest.com/demo/selectTest.htm")

    # 定位下拉框
    select_element = driver.find_element(By.ID, "s1")
    select = Select(select_element)

    # 💡 新增：遍历并打印所有选项的文本，看看真实值到底是什么
    print("下拉框中包含的选项有：")
    for option in select.options:
        # 打印时用 repr() 包起来，这样可以看清前后是否有隐藏的空格
        print(repr(option.text))

        # 💡 修改：使用索引选择（从 0 开始计数）
    # 如果你看到打印出来的第一个选项是你想要的，就传 0；第二个传 1，以此类推
    time.sleep(10)
    select.select_by_index(1)

    # 2. 💡 打印当前被选中的选项文本
    current_selection = select.first_selected_option
    print("当前选中的是：", current_selection.text)

    # 3. 如果你想打印更详细的信息（比如它的 value 属性），可以这样写：
    print("当前选中项的 value 是：", current_selection.get_attribute("value"))

    time.sleep(10)
    print("下拉框选择成功")
    driver.quit()

if __name__ == "__main__":
    #switch_window_example()
    drollwin_selector()