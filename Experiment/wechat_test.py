from selenium import webdriver  # 主要的
from selenium.common.exceptions import NoSuchElementException  # 捕获异常
from selenium.webdriver.support.ui import WebDriverWait  # 设置等待
from selenium.webdriver.firefox.options import Options as FOP  # 设置请求头
import datetime,re

startTime = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
firefox_options = FOP()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
# 禁止加载图片
firefox_options.set_preference('permissions.default.image', 2)
# 禁止加载css样式表
firefox_options.set_preference('permissions.default.stylesheet', 2)
# todo fixme 解决ip问题啊
firefox_options.set_preference('network.proxy.type', 1)
firefox_options.set_preference('network.proxy.http', '120.41.115.209')
firefox_options.set_preference('network.proxy.http_port', 4502)  # int
browserF = webdriver.Firefox(firefox_options=firefox_options)
wait = WebDriverWait(browserF, 10)
# browserF.get("https://weixin.sogou.com/weixin?query=一夜情&type=2&page=1")
browserF.get('http://httpbin.org/ip')
print(browserF.page_source)
pattern = re.compile(r"origin.  *\"(.*?),")
result = pattern.findall(browserF.page_source)

print(result)
# browserF.find_element_by_css_selector("#tool_show a").click()
#
# browserF.find_element_by_css_selector("#time").click()
# js = "var qp = document.getElementById('date_start');qp.value=''"
# browserF.execute_script(js)  # 执行javascript
# browserF.find_element_by_css_selector('#date_start').send_keys(startTime)
# browserF.find_element_by_css_selector("#time_enter").click()
# import time
# time.sleep(60)
browserF.quit()
