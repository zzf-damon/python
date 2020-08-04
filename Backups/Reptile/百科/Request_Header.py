import random
import requests
from pyquery import PyQuery as pq
import os
import json

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


def request_py(url):
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'  # document.charset
    html = html.text
    # print(html)
    doc = pq(html)
    # f = open('./1.html', mode='w', encoding='utf-8')
    # f.write(html)
    return doc


def file_name(url):
    lists = url.split("/")
    num_list = []
    for list in lists:
        if list != "":
            num_list.append(list)
    if len(num_list) > 4:
        path = num_list[2] + "/" + num_list[3]
    else:
        path = num_list[2]
    return path


def write(str, path):
    pre_path = path.split("/")
    if len(pre_path) > 1:
        if not os.path.exists(pre_path[0]):
            os.mkdir(pre_path[0])
    with open(path, 'a+') as f:
        f.write(str + '\n')


def nav_details(url):
    key2_list = []
    doc = request_py(url)
    contents = doc('#submenu p').find('a').items()
    for content in contents:
        str = content.attr("href")
        key2_list.append(str)
    return key2_list


def write_dict(filename, dict, code="utf-8"):
    with open(filename, 'a', encoding=code) as fp:
        # fp.writelines(dict)
        json.dump(dict, fp)
        # fp.write("\n")
    return True


def read_dict(filename, code="utf-8"):
    with open(filename, "r", encoding=code) as pf:
        datas = pf.readlines()
        # dict = json.loads(data)
    return datas  # 返回的是一个行列表



