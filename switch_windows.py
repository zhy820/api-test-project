
#switch windows

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def swith_windows():
    driver = webdriver.Chrome()

    # 打开第一个窗口
    driver.get("https://www.baidu.com")

    original_window = driver.current_window_handle

    # 打开第二个窗口
    driver.execute_script("window.open('https://www.google.com');")

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    # 切换到第二个窗口
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    #在新窗口操作
    print("当前窗口标题:", driver.title)

    # 切换回原窗口
    driver.switch_to.window(original_window)
    print("切换回原窗口标题:", driver.title)

    # 通过索引转换
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.window(driver.window_handles[1])