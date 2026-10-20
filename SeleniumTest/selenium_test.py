from sys import orig_argv

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_winHandle():
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.baidu.com")
    handles = driver.window_handles # get all handles
    print(handles)
    winHandle = driver.current_window_handle
    print(winHandle)
    return winHandle

def get_element():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    # 定位"设置"
    setting = driver.find_element(By.ID, "s-usersetting-top")
    print("找到元素:", setting.text)  # 设置

    # 悬停展开二级菜单
    ActionChains(driver).move_to_element(setting).perform()

    # 点击二级菜单项（示例：搜索设置）
    try:
        item = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'搜索设置')]"))
        )
        item.click()
        time.sleep(10)
        print("已点击 搜索设置")
    except Exception as e:
        print("未找到二级菜单:", e)

def win_test():
    #Open browser and navigate to Baidu
    driver = webdriver.Chrome()

    #Open Baidu homepage
    driver.get("https://www.baidu.com")

    #Win Operation
    time.sleep(10)
    driver.maximize_window()

    time.sleep(5)
    driver.back()

    time.sleep(5)
    driver.forward()

    time.sleep(5)
    driver.refresh()

    time.sleep(5)
    driver.minimize_window()

    #Close the current window
    time.sleep(10)

    driver.close()

    #Close the browser
    driver.quit()

def find_element():
    driver = webdriver.Chrome()

    driver.get("https://www.baidu.com")


    try:
        wait = WebDriverWait(driver, 10)

        # 3. 等待元素出现（使用 visibility_of_element_located 更好）
        # 这里用 By.LINK_TEXT 定位 "新闻"
        news_link = wait.until(
            #精准匹配，a/
            #EC.visibility_of_element_located((By.LINK_TEXT, "新闻"))

            #模糊匹配
            #EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), '新闻')]"))
            #driver.find_element(By.XPATH, "//a[contains(text(), '新闻')]")

            #基准匹配，去掉前后空格
            EC.visibility_of_element_located((By.XPATH,  "//a[normalize-space(text())='新闻']"))
        )

        if (news_link.text == "新闻"):  # 验证文本是否正确
            print("✅ 找到元素，文本正确:", news_link.text)
            news_link.click()
            time.sleep(10)

            #swith to the new window
            orig_win_handle = driver.current_window_handle
            for handle in driver.window_handles:
                if handle == orig_win_handle:
                    driver.switch_to.window(handle)
                    print("已切换到新窗口:", driver.current_url)
                    break

        else:
            print("❌ 找到元素，但文本不正确:", news_link.text)
            return



        # # 精确匹配
        # driver.find_element(By.XPATH, "//a[text()='新闻']")
        #
        # # 或者模糊匹配（防止空格干扰）
        # driver.find_element(By.XPATH, "//a[contains(text(), '新闻')]")
        #
        # driver.find_element(By.LINK_TEXT, "新闻")
        # 点击


    except Exception as e:
        if e == selenium.common.exceptions.NoSuchElementException:
            print("元素未找到:", e)
        elif e == selenium.common.exceptions.ElementNotInteractableException:
            print("元素不可交互:", e)
        else:
            print("其他异常:", e)


if __name__ == "__main__":
    #get_winHandle()
    #win_test()
    find_element()