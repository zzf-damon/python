import jieba
import re
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument('--headless')  # 如果觉得没问题，就打开这一行，就可以了
browser = webdriver.Firefox(options=firefox_options)
browser.get("http://222.197.219.6:8080/cclzc/login.jsp")

userName = "20182204158"
password = "20182204158"

browser.find_element_by_css_selector('#yhbh').send_keys(userName)
browser.find_element_by_css_selector('#yhmm').send_keys(password)
browser.find_element_by_css_selector("#entry").click()



punctuation = '!,;:?"\'. '
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
browser.find_element_by_css_selector("button[onclick='search()']").click()
signA = browser.find_element_by_css_selector(".login_title").text

while signA == "Corpus Tagging":
    print(browser.find_element_by_xpath("/html/body/form/div[3]/label/font").text)
    src_text = browser.find_element_by_css_selector("#src_text_1").text
    print(src_text)
    teg_text = browser.find_element_by_css_selector("#updatexyz").text
    print(teg_text)
    signB = False
    end_count = src_text.count("。")
    question_count = src_text.count("？")
    exclamation_count = src_text.count("！")

    if end_count <= 1 or question_count <= 1 or exclamation_count <= 1:  # 判断中文句子
        en_text = re.sub(r'[{}]+'.format(punctuation), '', teg_text)
        if not en_text.encode('UTF-8').isalpha():  # 判断是否是全英文
            src_len = list(jieba.cut(re.sub(pattern, "", src_text)))
            teg_len = re.split(pattern, teg_text)
            if len(src_text) - len(teg_text) < 1:  # 判断长度
                print("True")
                browser.find_element_by_css_selector("#zq").click()
                signB = True
    if not signB:
        print("False")
        browser.find_element_by_css_selector("#cw").click()
    time.sleep(2)
    signA = browser.find_element_by_css_selector(".login_title").text
else:
    print("就你竟然有反扒，你配吗？？？")
    browser.quit()
