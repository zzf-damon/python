import jieba
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import requests, json
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
from urllib3.exceptions import ProtocolError

punctuation = '!,;:?"\'. '
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'

userName = "20192104103"
password = "20192104103"

while True:
    try:
        firefox_options = Options()
        firefox_options.add_argument('--headless')
        browser = webdriver.Firefox(options=firefox_options)
        browser.get("http://222.197.219.6:8080/cclzc/login.jsp")

        browser.find_element_by_css_selector('#yhbh').send_keys(userName)
        browser.find_element_by_css_selector('#yhmm').send_keys(password)
        browser.find_element_by_css_selector("#entry").click()

        browser.find_element_by_css_selector("button[onclick='search()']").click()
        signA = browser.find_element_by_css_selector(".login_title").text
        cookies = {
            "JSESSIONID": browser.get_cookie("JSESSIONID")["value"]
        }
        src_text = ""
        teg_text = ""
        data_xh = ""
        url2 = "http://222.197.219.6:8080/cclzc/search?tgt=1&src=0&zh=" + src_text + "&xyz=" + teg_text + "&data_xh=" + data_xh + "&ywzql=&zh_update=" + src_text + "&updatexyz=" + teg_text

        while signA == "Corpus Tagging":
            print(browser.find_element_by_xpath("/html/body/form/div[3]/label/font").text)
            response = requests.get(url2, cookies=cookies).text
            data = json.loads(json.loads(response)["message"])
            src_text = data[0]
            teg_text = data[1]
            data_xh = data[3]
            # src_text = browser.find_element_by_css_selector("#src_text_1").text
            print(src_text)
            # teg_text = browser.find_element_by_css_selector("#updatexyz").text
            print(teg_text)
            signB = False
            end_count = src_text.count("。")
            question_count = src_text.count("？")
            exclamation_count = src_text.count("！")

            if end_count <= 1 and question_count <= 1 and exclamation_count <= 1:  # 判断中文句子
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
            time.sleep(1)
            signA = browser.find_element_by_css_selector(".login_title").text
        else:
            print("就你竟然有反扒，你配吗？？？")
            browser.quit()
    except KeyboardInterrupt:
        break
    except NoSuchElementException and StaleElementReferenceException and ConnectionError and JSONDecodeError and ProtocolError:
        print("没有找到元素")
