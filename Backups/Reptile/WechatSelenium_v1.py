from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FOP
from selenium.webdriver.chrome.options import Options as COP
import time, sys, re, traceback

KEYWORD = ['抢劫杀人', '失踪', '状告', '死亡', '事故', '收费', '就业', '不顾死活', '腐败', '违规', '违反规定', '骗子', '黑车', '暴力',
           '一夜情', '激情', '爆炸', '砍人', '纠纷', '打假', '打砸', '案件', '斧头', '欠债', '玩忽职守', '被杀',
           '涉恶', '恶势力', '公道', '严惩', '殴打', '处罚', '贪官', '黑恶', '检举', '拒不执行', '判决', '裁定', '刑事案件',
           '网络司法拍卖', '庭审', '当事人', '诉讼权利', '民事诉讼', '风险提示', '起诉', '民事诉状', '诈骗罪', '寻衅滋事罪',
           '故意伤害罪', '职务侵占罪', '开设赌场罪', '敲诈勒索罪', '危险驾驶罪', '强奸罪', '非法经营罪', '交通肇事罪',
           '一审', '宣判', '主犯', '从犯', '获刑', '没收财产', '诈骗', '认罪', '判决', '认罪', '上诉', '法院', '公开开庭'
    , '审理']


def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            print('Error execute: %s' % actual_do.__name__)

    return add_robust


# @robust
def except_handle(except_url):
    head_url = except_url.split("?")
    if head_url[0] == "https://weixin.sogou.com/antispider/":
        return False
    else:
        pattern = re.compile(r'page=(\d+)&')  # 查找数字
        page = pattern.findall(except_url)
    return page[0]


@robust
def url_list(keyword, page):
    firefoxPage = FirefoxPage(keyword, page)
    signD = firefoxPage.firefox_main()
    if signD is True:
        return True
    else:
        url_list(keyword, signD[1])


@robust
def list_url(browser, wait):
    for i in range(10):
        try:
            ID = "sogou_vr_11002601_title_" + str(i)
            idID = "#" + ID
            search_button = browser.find_element_by_id(ID)
            browser.execute_script("arguments[0].target = '_self';", search_button)
            submit1 = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, idID))
            )
            submit1.click()
            try:
                content_except = browser.find_element_by_class_name("weui-btn-area")
                if content_except:
                    print("重要提醒：这个网页转移，现在是不能爬到的")
                    browser.back()
                    continue
            except BaseException:
                careful_title = browser.find_element_by_id("activity-name")
                print(careful_title.text)
                browser.back()
                URL_list = browser.current_url
                if URL_list.split("/")[2] != "weixin.sogou.com":
                    browser.back()
                    print("再次返回")
        except BaseException:
            print("try1")
            print(sys.exc_info())
            print(browser.current_url)
            continue
            # browser.back()
            # except_url = browser.current_url
            # page = except_handle(except_url)
            # page = int(page) + 1
            # # time.sleep(500)
            # browser.quit()
            # # chrome_main(keyword, page)
            # return False, str(page)
    return True


@robust
class FirefoxPage(object):
    def __init__(self, keyword, page):
        firefox_options = FOP()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        # self.browserF = webdriver.Firefox()
        self.browserF = webdriver.Firefox(firefox_options=firefox_options)
        self.waitF = WebDriverWait(self.browserF, 10)
        self.keyword = keyword
        self.page = page

    @robust
    def firefox_main(self):
        self.browserF.get(
            "https://weixin.sogou.com/weixin?query=" + self.keyword + "&type=2&page=" + self.page)
        print(self.browserF.current_url)
        page = int(self.page)
        for i in range(page, 11):
            # i = i+ 1
            print("开始爬取第%d页" % i)
            # self.signB = list_url(self.browserF, self.waitF)
            list_url(self.browserF, self.waitF)
            submit = self.waitF.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#sogou_next'))
            )
            submit.click()
            signF = except_handle(self.browserF.current_url)
            if signF is False:
                self.browserF.quit()
                return False, str(i)
        return True


if __name__ == '__main__':
    for keyword in KEYWORD:
        print(keyword)
        page = "1"
        firefoxPage = FirefoxPage(keyword, page)
        signA = firefoxPage.firefox_main()
        time.sleep(10)
        if signA is True:
            continue
        else:
            signE = url_list(keyword, signA[1])
            if signE is True:
                continue
