import requests
from pyquery import PyQuery as pq
import re
import random
import json
import pyodbc
# from selenium import webdriver
import time


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
ReconmmendKeyWord = ['前端', '架构', '编程语言', '数据库', '游戏开发', '物联网', '音视频开发']


def py_requests(url):
    html = requests.get(url, headers=headers).text  # request请求网页
    doc = pq(html)
    return doc


# 获取所有分类节点的网址
def getAnode():
    url = r"https://www.csdn.net"
    doc = py_requests(url)
    recommendType_list = []
    nums = doc('#nav').find('a').items()
    for num in nums:
        # print(num)
        reconmmendKeylink = num.attr('href')
        reconmmendKeyword = num.text()
        relink = 'https://www.csdn.net' + reconmmendKeylink
        print("分支是：%s ,链接是 %s" % (reconmmendKeyword, relink))
        # 将访问前端、架构、编程语言、数据库、游戏开发、移动开发、物联网、音视频开发的链接存到列表中一个个的访问
        if reconmmendKeyword in ReconmmendKeyWord:
            recommendType_list.append(relink)  # 将所有推荐的链接存到列表中
            print("1")
    for i in range(len(recommendType_list)):
        # print(recommendType_list[i])
        get_article_link(recommendType_list[i])


# 获取所有评论数大于0的文章的链接
def get_article_link(url):  # url作为形参
    # driver = webdriver.Chrome()
    # str = driver.get(url)
    # print("这是driver.get(url)的输出%s" % str)
    # time.sleep(5)
    recommendArtical_list = []
    for i in range(100):
        # driver.execute_script('window.scrollTo(0,1000000)')  # 模拟鼠标滑动，下拉分页，获取更多未加载的内容
        # time.sleep(3)
        # html = driver.page_source
        # print("这是第一个html%s" % html)
        doc = py_requests(url)
        items = doc('#feedlist_id').find('.clearfix').items()
        for item in items:
            titles = item('.title').find('a').text()
            title = titles.split("推荐不准", 1)[0]
            link = item('.title').find('a').attr('href')
            nums = re.findall("(\d+)", item('.interactive').find('span').text())
            if len(nums) > 1:  # 评论数>0,选取有评论的数据
                read_num, comment_num = nums[0], nums[1]
                print("文章标题是：%s    文章链接是：%s      阅读数是：%s    评论数是：%s" % (title, link, read_num, comment_num))
                # "https://blog.csdn.net/qdqzgcs/article/details/89192280"
                list_link = link.split(
                    "/")  # ['https:', '', 'blog.csdn.net', 'qdqzgcs', 'article', 'details', '89192280']
                recommendArtical_list.append(['%s' % link, '%s' % list_link[3], '%s' % list_link[6], '%s' % title])
    for j in range(len(recommendArtical_list)):
        # print(recommendArtical_list[j])
        article_link = recommendArtical_list[j][0]
        article_flag = recommendArtical_list[j][1]
        article_num = recommendArtical_list[j][2]
        article_title = recommendArtical_list[j][3]
        print("标题：%s  文章链接是：%s  唯一标识是：%s  唯一标号是：%s" % (article_title, article_link, article_flag, article_num))
        comment_content(article_link, article_flag, article_num, article_title, read_num)


def comment_content(link, article_flag, article_num, title, read_num):
    doc = py_requests(link)
    code = doc('.blog-content-box').find('code').text()
    count = 0
    if len(code) > 0:  # 如果文章内存在代码段，则将评论信息存到数据库
        url1 = r"https://blog.csdn.net/" + article_flag + r"/phoenix/comment/list/" + article_num + r"?page=1&size=15&tree_type=1"
        web_data = requests.get(url1, headers=headers).text
        datas = json.loads(web_data, )
        # print(datas.keys())#dict_keys(['result', 'callback', 'data', 'vote', 'content'])
        # print(datas.get("data"))
        if datas.get("data") == None:
            print("-----评论不存在------")
        else:
            comment_count = datas.get("data").get("count")  # 获取评论数
            page_num = datas.get("data").get("page_count")  # 获取评论的页数
            print("共计评论数：%s  页数：%s" % (comment_count, page_num))
            for i in range(page_num):
                try:
                    new_url = r"https://blog.csdn.net/" + article_flag + r"/phoenix/comment/list/" + article_num + r'?page=' + str(
                        i) + r'&size=15&tree_type=1'
                    web_data = requests.get(new_url, headers=headers).text
                    datas = json.loads(web_data)
                    lists = datas.get("data").get("list")
                    # print(lists)
                    list = []
                    for i in range(len(lists)):
                        # list=lists[i]
                        # print(list)
                        info = lists[i].get("info")
                        # print(info)
                        NickName = info.get("NickName")
                        Content = info.get("Content")
                        PostTime = info.get("PostTime")
                        print("文章标题是：%s  文章链接：%s   评论人：%s    评论内容是：%s   评论时间是：%s " % (
                            title, link, NickName, Content, PostTime))
                        count += 1
                        # cursor.execute(
                        #     "insert into CodeComment(title,comment_user, comment_content, read_num, comment_time) values(?, ?, ?, ?, ?)",
                        #     (title, NickName, Content, read_num, PostTime))
                        # cursor.commit()
                    print("-------------------第一页评论提取结束---------------------------")
                except Exception as e:
                    print("出现异常-->" + str(e))
            print("-------------------文章评论提取end---------------------------")
            print("共计获取评论%d条" % count)


if __name__ == '__main__':
    # conn = pyodbc.connect(
    #     'DRIVER={SQL Server};SERVER=192.168.1.101,1433;DATABASE=CodeCommentDataOriginal;UID=sa;PWD=123456')
    # cursor = conn.cursor()
    getAnode()
    # conn.close()
