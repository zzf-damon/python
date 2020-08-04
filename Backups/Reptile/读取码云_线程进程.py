import requests
from pyquery import PyQuery as pq
import re
from multiprocessing import Queue, Process
import threading
import random
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


# f = open('./9.html', mode='w', encoding='utf-8')
# f.write(html)
# path = "/home/z/python/Mar_24/9.html"
# f = open(path, 'r', encoding='utf-8')
# html = f.read())

def second(q):
    while True:
        url = q.get(True)
        # break
        if url == "这是终极测试":
            print("这是终极测试——————说明读进程应该终止，且value为5")
            break
        else:
            t = threading.Thread(target=last, args=(url,))
            t.start()
            t.join()
    print("爬取的评论列表已经完成")


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
    except Exception as e:
        print("出现异常-->" + str(e))



def first(q, page_nums):
    for page_num in range(1, int(page_nums) + 1):
        url = "https://gitee.com/search?page=" + str(page_num) + "&q=coding&type=code"
        # print("这是第%d页的地址%s" % (num, url))
        # second(num, url)
        # t = threading.Thread(target=run, args=(url,))
        # t.start()
        html = requests.get(url, headers=headers).text
        doc = pq(html)
        comment_num = doc('.search-content').find('.item-header').items()
        # names = doc('.search-content .item-header').find('.title').items()
        code_num = 0
        for c_num in comment_num:
            code_num += 1
            name = c_num('.title').find('b').text()
            num = c_num('span').text()
            lable = c_num('.title').find('div').text()
            print("这是第%d页的第%d段代码" % (page_num, code_num))
            print("作者 / 代码段名为：%s     其中他的标签是%s" % (name, lable))
            print("代码段数:%s  评论数:%s   点赞数：%s" % (num[0], num[2], num[4]))
            if num[2] is not "0":
                comment_url = c_num.find('a').attr('href')
                str1 = "https://gitee.com"
                str2 = "#git-issue-comments"
                comment_url = str1 + comment_url + str2
                print("他的评论的地址是 %s" % comment_url)
                # last(comment_url)
                q.put(comment_url)
            else:
                continue
        q.put("这是终极测试")


if __name__ == '__main__':
    # url = "https://gitee.com/search?page=2&q=coding&type=code"
    # page_num = 1
    # second(page_num, url)
    start = time.time()
    print("这是开始的时间%s " % str(start))
    q = Queue()
    keyword = input("请输入查找的关键词")
    # first(keyword)
    url = r"https://gitee.com/search?q=" + keyword + "&type=code"
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    # f = open('./9.html', mode='w', encoding='utf-8')
    # f.write(html)
    page_list = []
    nums = doc('.search-footer').find('.item').items()
    if nums is None:
        page_num = 1
    else:
        for num in nums:
            num = re.findall('page=(.*?)&q=', str(num.attr("href")), re.S)
            # print(num)
            page_list.append(num)
        index = page_list.index(max(page_list))
        page_num = page_list[index]
        print("这是共有%s页" % page_num[0])
    pw = Process(target=first, args=(q, page_num[0],))
    pr = Process(target=second, args=(q, ))
    pw.start()
    pr.start()
    pr.join()
    end = time.time()
    print("这是最后的时间%s" % str(end - start))


"""
import requests
from pyquery import PyQuery as pq
import re
from multiprocessing import Queue, Process
import threading
import random
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


# f = open('./9.html', mode='w', encoding='utf-8')
# f.write(html)
# path = "/home/z/python/Mar_24/9.html"
# f = open(path, 'r', encoding='utf-8')
# html = f.read())

def second(q):
    while True:
        url = q.get(True)
        # break
        if url == "这是终极测试":
            print("这是终极测试——————说明读进程应该终止，且value为5")
            break
        else:
            t = threading.Thread(target=last, args=(url,))
            t.start()
            t.join()
    print("爬取的评论列表已经完成")


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
    except Exception as e:
        print("出现异常-->" + str(e))



def first(q, page_nums):
    for page_num in range(1, int(page_nums) + 1):
        url = "https://gitee.com/search?page=" + str(page_num) + "&q=coding&type=code"
        # print("这是第%d页的地址%s" % (num, url))
        # second(num, url)
        # t = threading.Thread(target=run, args=(url,))
        # t.start()
        html = requests.get(url, headers=headers).text
        doc = pq(html)
        comment_num = doc('.search-content').find('.item-header').items()
        # names = doc('.search-content .item-header').find('.title').items()
        code_num = 0
        for c_num in comment_num:
            code_num += 1
            name = c_num('.title').find('b').text()
            num = c_num('span').text()
            lable = c_num('.title').find('div').text()
            print("这是第%d页的第%d段代码" % (page_num, code_num))
            print("作者 / 代码段名为：%s     其中他的标签是%s" % (name, lable))
            print("代码段数:%s  评论数:%s   点赞数：%s" % (num[0], num[2], num[4]))
            if num[2] is not "0":
                comment_url = c_num.find('a').attr('href')
                str1 = "https://gitee.com"
                str2 = "#git-issue-comments"
                comment_url = str1 + comment_url + str2
                print("他的评论的地址是 %s" % comment_url)
                # last(comment_url)
                q.put(comment_url)
            else:
                continue
        q.put("这是终极测试")


if __name__ == '__main__':
    # url = "https://gitee.com/search?page=2&q=coding&type=code"
    # page_num = 1
    # second(page_num, url)
    start = time.time()
    print("这是开始的时间%s " % str(start))
    q = Queue()
    keyword = input("请输入查找的关键词")
    # first(keyword)
    url = r"https://gitee.com/search?q=" + keyword + "&type=code"
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    # f = open('./9.html', mode='w', encoding='utf-8')
    # f.write(html)
    page_list = []
    nums = doc('.search-footer').find('.item').items()
    if nums is None:
        page_num = 1
    else:
        for num in nums:
            num = re.findall('page=(.*?)&q=', str(num.attr("href")), re.S)
            # print(num)
            page_list.append(num)
        index = page_list.index(max(page_list))
        page_num = page_list[index]
        print("这是共有%s页" % page_num[0])
    pw = Process(target=first, args=(q, page_num[0],))
    pr = Process(target=second, args=(q, ))
    pw.start()
    pr.start()
    pr.join()
    end = time.time()
    print("这是最后的时间%s" % str(end - start))

"""
