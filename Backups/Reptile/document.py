import re
import json
import requests
from pyquery import PyQuery as pq
import random

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
# theme 读txt/分dict/写json
"""
dict = {}
with open('傣族.txt', 'r') as f:
    lists = f.readlines()
    
start_url = lists[0].split("/")
for i, list in enumerate(lists):
    list = re.sub('\n', '', list)
    dict.setdefault(list.split("/")[2], []).append(list)

with open('傣族_list', 'w') as f:
    f.write(json.dumps(dict)+'\n')
"""


def crawl(key, url, str):
    html = requests.get(url, headers=headers)
    if key == "zhidao.baidu.com":
        html.encoding = 'GBK'
        print("解码方式是:GBK")
    else:
        html.encoding = 'utf-8'
        print("解码方式是:utf-8")
    html = html.text
    doc = pq(html)
    content = doc(str).text()
    print(content)
    if content is "":
        num = input("爬去内容为空是否继续爬取,输入将继续,:1,输入重爬:2.....:输入:|")
        if num == 2:
            crawl(key, url, str)
        else:
            pass
    else:
        with open(key, 'a+') as f:
            f.write(content + '\n')
            print("写入成功")


# theme 读json/
with open("傣族_list", 'r') as f:
    dict = f.read()
dic = json.loads(dict)
keys, lenght = list(dic.keys()), len(dic.keys())

for key in keys:
    key_list = dic.get(key)
    num = input("当前正在爬取这种网站 %s,如果不爬输入:1,继续输入:2......: 输入|" % key_list[0])
    if num == "1":
        continue
    else:
        print("key: %s" % key)
        str = input("请输入你要爬去的内容标签名:   |")
        for i, key_url in enumerate(key_list):
            crawl(key, key_url, str)
            print("将要爬去这种网站的第%d个: %s" % (i, key_url))
