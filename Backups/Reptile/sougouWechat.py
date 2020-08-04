from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys



from sougouWechat2 import Chrome
from selenium.webdriver.firefox.options import Options
import re
firefox_options = Options()
firefox_options.add_argument('--headless')
browser = webdriver.Firefox(firefox_options=firefox_options)
# browser = webdriver.Firefox()
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"
wait = WebDriverWait(browser, 10)
KEYWORD = '抢劫'

def list_url():
    for i in range(10):
        try:
            ID = "sogou_vr_11002601_title_" + str(i)
            idID = "#" + ID
            # sogou_vr_11002601_title_0 activity-name
            search_button = browser.find_element_by_id(ID)
            browser.execute_script("arguments[0].target = '_self';", search_button)
            submit1 = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, idID))
            )
            submit1.click()
            careful_title = browser.find_element_by_id("activity-name")
            print(careful_title.text)
            browser.back()
            URL = browser.current_url
            if URL.split("/")[2] != "weixin.sogou.com":
                browser.back()
                print("再次返回")
        except BaseException:
            print("这是第一个")
            print(sys.exc_info())
            browser.back()
            except_url = browser.current_url
            print(except_url)
            page = except_handle(except_url)
            # time.sleep(500)
            browser.quit()
            # chrome_main(KEYWORD, page)
            chrome = Chrome()
            chrome.chrome_main(KEYWORD,page)
    return True

def except_handle(except_url):
    pattern = re.compile(r'page=(\d+)&')  # 查找数字
    result = pattern.findall(except_url)
    return result[0]

def main():
    for i in range(10):
        i = i+1
        print("开始爬取第%d页" % i)
        signA = list_url()
        if signA is True:
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#sogou_next'))
            )
            submit.click()
    # browser.quit()
    # chrome_main(KEYWORD)


if __name__ == '__main__':
    browser.get('https://weixin.sogou.com/')
    input_name = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#query'))
    )
    input_name.send_keys(KEYWORD)
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.swz'))
    )
    submit.click()
    main()
