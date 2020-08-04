import time
import requests
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
from openpyxl.drawing.image import Image
from pyquery import PyQuery as pq
import re
from multiprocessing import Pool
import threading
import random
import xlwt
import os
import binascii


# os.chdir('E:\MayunSpiderResult')

headers = {
    'user-agent': ""
}
agentStr = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
    "UCWEB7.0.2.37/28/999"
]
agentStr = random.choice(agentStr)
headers['user-agent'] = agentStr
url_list = []

lists1 = [['作者/代码名称', '页号', '标签', '代码段数', '评论数', '点赞数', '作者/代码名称', '用户名', '评论内容', '评论时间']]


def chr_trans(key_word):
    keys = ""
    for i in key_word:
        # print(i)
        if (i >= u'\u0041' and i <= u'\u005a') or (i >= u'\u0061' and i <= u'\u007a'):
            keys = keys + i
        else:
            str3 = binascii.b2a_hex(i.encode("utf8"))
            str2 = str(str3)
            str4 = re.findall("b'(.*?)'", str2, re.S)[0]
            if len(str4) == 2:
                str4 = "%" + str4
            else:
                str4 = "%" + str4[0:2] + "%" + str4[2:4] + "%" + str4[-2:]
            keys = keys + str4
    return keys


def second(page_num, url):
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    comment_num = doc('.search-content').find('.item-header').items()
    code_num = 0
    for c_num in comment_num:
        code_num += 1
        name = c_num('.title').find('b').text()
        num = c_num('span').text()
        lable = c_num('.title').find('div').text()
        num0 = num[0]
        num2 = num[2]
        num4 = num[4]
        print("第%d页     第%d段代码" % (page_num, code_num))
        print("作者 / 代码段名：%s     代码标签是%s" % (name, name))
        print("代码段数:%s  评论数:%s   点赞数：%s" % (num[0], num[2], num[4]))

        if num[2] is not "0" and name != "长孙无忌919 / 集成学习和半监督学习":
            comment_url = c_num.find('a').attr('href')
            str1 = "https://gitee.com"
            str2 = "#git-issue-comments"
            comment_url = str1 + comment_url + str2
            print("评论的地址：%s" % comment_url)
            # last(comment_url)
            try:
                html1 = requests.get(comment_url, headers=headers).text
                doc1 = pq(html1)
                comments = doc1('.column #notes-list').find(".content").items()
                for comment in comments:
                    content = comment.find("p").text()
                    img_address = comment.find('.emoji').attr('src')
                    author = comment.find(".author").text()
                    timeago = comment.find('.timeago').text()
                    print("作者是：%s  其评论是:%s   其评论时间是%s" % (author, content, timeago))
                    lists1.append(['%s' % name, '%s' % page_num, '%s' % lable, '%s' % num0, '%s' % num2, '%s' % num4,
                                   '%s' % author, '%s' % content, '%s' % timeago])
            except Exception as e:
                print("出现异常-->" + str(e))
        else:
            continue


'''
def last(url):
    try:
        html = requests.get(url, headers=headers).text
        doc = pq(html)
        comments = doc('.column #notes-list').find(".content").items()
        for comment in comments:
            content = comment.find("p").text()
            author = comment.find(".author").text()
            timeago = comment.find('.timeago').text()
            print("作者是：%s  其评论是:%s   其评论时间是%s" % (author, content, timeago))
            lists1.append(['%s' % name,'%s' % author ,'%s' % content ,'%s' % timeago])
    except Exception as e:
        print("出现异常-->" + str(e))
'''


def first(keyword):
    url = r"https://gitee.com/search?utf8=%E2%9C%93&q=" + keyword + "&type=code"
    # print(url)
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    # f = open('./9.html', mode='w', encoding='utf-8')
    # f.write(html)
    page_list = []
    nums = doc('#git-discover-page').find('.item').items()
    for num in nums:
        # num = re.findall('page=(.*?)&amp;q=', str(num.attr("href")), re.S)
        num = str(num.text())
        # print(num)
        if num.isalnum():
            page_list.append(int(num))
    if page_list:
        index = page_list.index(max(page_list))
        page_num = page_list[index]
        print("该检索词共计%s页" % page_num)
        for num in range(1, page_num + 1):
            str1 = "https://gitee.com/search?page="
            str2 = "&q=" + keyword + "&type=code"
            url = str1 + str(num) + str2
            second(num, url)
    else:
        num = 0
        print("该检索词共一页")
        second(num, url)
        # print("这是第%d页的地址%s" % (num, url))


if __name__ == '__main__':
    book1 = xlwt.Workbook()  # 新建一个excel
    sheet1 = book1.add_sheet(u'RubyComment', cell_overwrite_ok=True)
    keyword = input("请输入查找的关键词")
    keyword = chr_trans(keyword)
    first(keyword)
    for j in range(0, len(lists1)):
        row1 = 0
        for list1 in lists1:  # 再循环里面list的值，每一列
            col1 = 0
            for s1 in list1:
                sheet1.write(row1, col1, s1)
                j += 1
                col1 += 1  # 列不变行加一
            row1 += 1
        book1.save('RubyComment.xls')
