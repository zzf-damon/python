from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys,os
from selenium.webdriver.edge.options import Options
# edge_options = Options()
# edge_options.add_argument('--headless')
# edge_options.add_argument('--disable-gpu')
# browser1 = webdriver.Edge(edge_options=edge_options)

browser1 = webdriver.Edge(r"‪D:\conda\msedgedriver.exe")
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"
# wait1 = WebDriverWait(browser1, 10)

browser1.get("http://www.sina.cn/")

# @Time:2019/1/10 20:37
from selenium import webdriver

# 指定chrom的驱动
# 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome('E:\ChromDriver\chromdriver2.43\chromedriver.exe')
driver.implicitly_wait(10)

driver.get('https://www.51job.com/')
# 点击高级搜索
driver.find_element_by_css_selector(".more").click()

# 根据id找到关键字输入框,输入python
driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_xpath('//div[@class="tit"]/span').click()
# 点击工作地点
driver.find_element_by_id('work_position_input').click()

import time

time.sleep(2)

# 用css方法找到所有的城市
cityEles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')

# 遍历元素，一个个城市去找
for one in cityEles:
    # 城市名
    cityname = one.text
    # 用之前学过的attribute方法获取class的值
    cassvalue = one.get_attribute('class')
    #
    if cityname == '杭州':
        if cassvalue != 'on':
            one.click()
    elif cityname != '杭州':
        if cassvalue == 'on':
            one.click()
# 点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click()
# 点击职能类别
driver.find_element_by_id('funtype_click').click()
# 选择计算机软件
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
# 选择高级软件工程师
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
# 点击确定按钮
driver.find_element_by_id('funtype_click_bottom_save').click()
# 点击公司性质
driver.find_element_by_id('cottype_list').click()
# 选择外资欧美
driver.find_element_by_xpath('//*[@id="cottype_list"]/div/span[2]').click()
# 工作年限
driver.find_element_by_id('workyear_list').click()
# 选择1~3年
driver.find_element_by_xpath('//*[@id="workyear_list"]/div/span[3]').click()
# 点击搜索
driver.find_element_by_xpath('//div[@class="btnbox p_sou"]/span').click()
# 或者
# driver.find_element_by_xpath('//*[@id="saveSearch"]/preceding-sibling::span').click()
# 找职位
jobs = driver.find_elements_by_css_selector('#resultList div.el')

for job in jobs[1:]:
    # span是一个列表
    spans = job.find_elements_by_tag_name('span')
    # 列表生成式
    fields = [span.text for span in spans]
    print(fields)

# 退出
driver.quit()
