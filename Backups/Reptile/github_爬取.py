from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

# firefox_options = Options()
# firefox_options.add_argument('--headless')
# firefox_options.add_argument('--disable-gpu')
# browser = webdriver.Firefox(firefox_options=firefox_options)

browser = webdriver.Firefox()
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
wait = WebDriverWait(browser, 10)


def get_home_page():
    num1 = 1
    browser.refresh()
    html = browser.page_source
    doc = pq(html)
    num_comment = doc('#code_search_results').find('.current').attr('data-total-pages')
    num_comment = int(num_comment)
    if num_comment is None:
        num_comment = 1
    else:
        num_comment -= 1
    for n in range(num_comment):
        submit2 = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#code_search_results > div.paginate-container.codesearch-pagination-container > div > a.next_page'))
        )
        submit2.click()
        print("这是应该在第%d页" % (n + 2))
        first_page(num1)


def first_page(num1):
    browser.refresh()
    html = browser.page_source
    doc = pq(html)
    names = doc('#code_search_results').find('.text-bold').items()
    name_list = []
    num2 = 0
    for name in names:
        str1 = name.text()
        if str1 in name_list:
            continue
        else:
            url = 'https://github.com/' + str1
            num2 += 1
            print("这是第%d页的第%d个作者的作品的地址:%s" % (num1, num2, url))
            second_page(url, num1, num2)
    browser.back()


def second_page(url, num1, num2):
    browser.get(url)
    browser.refresh()
    html = browser.page_source
    doc = pq(html)
    works = doc('.file-wrap .js-navigation-item').find('.message').items()
    num3 = 0
    url_list = []
    for work in works:
        str2 = work.find('.link-gray').attr('href')
        if str2 in url_list:
            continue
        else:
            url_list.append(str2)
        url = 'https://github.com/' + str2
        num3 += 1
        print("这是第%d页第%d个作者的第%d个作品的地址:%s" % (num1, num2, num3, url))
        finally_page(url, num1, num2, num3)
    browser.back()


def finally_page(url, num1, num2, num3):
    browser.get(url)
    browser.refresh()
    html = browser.page_source
    doc = pq(html)
    num_comment = doc('#all_commit_comments .commit-comment-count').text()[0:1]
    if num_comment != "0":
        print("第%d页第%d个作者的第%d个作品有%s个评论" % (num1, num2, num3, num_comment))
        comments = doc('#all_commit_comments ').find('#comments .edit-comment-hide p').items()
        num4 = 0
        for comment in comments:
            comment = comment.text()
            num4 += 1
            print("第%d评论是：%s" % (num4, comment))
    else:
        print("第%d页第%d个作者的第%d个作品没有评论" % (num1, num2, num3))
    browser.back()


def entry():
    browser.get('https://github.com/login')
    input_name = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#login_field'))
    )
    input_name.send_keys('zzf-damon')
    input_password = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
    )
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn'))
    )
    input_password.send_keys('zhang00a')
    submit.click()
    return None


def keys(key_word):
    input_keys = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input-sm'))
    )
    input_keys.send_keys(key_word)
    submit2 = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    '#jump-to-suggestion-search-global > a:nth-child(1) > div:nth-child(4) > span:nth-child(2)'))
    )
    submit2.click()
    submit_code = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.menu-item:nth-child(2)'))
    )
    submit_code.click()
    get_home_page()
