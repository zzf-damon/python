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

url= "https://zh.glosbe.com/my/zh/၁၂၃၂page=4&tmmode=MUST"

def request_py(url):
    html = requests.get(url, headers=headers)
    html.encoding = 'UTF-8'  # document.charset
    html = html.text
    # print(html)
    doc = pq(html)
    # f = open('./1.html', mode='w', encoding='utf-8')
    # f.write(html)
    return doc



if __name__ == '__main__':
    for i in range(100):
        url = "https://zh.glosbe.com/my/zh/၁၂၃၂page="+ str(int(i)+1) + "&tmmode=MUST"
        doc = request_py(url)
        content = doc("#phraseHeaderId").find("span:first-child").text()
        text = doc("#tm-tab-cont #tmTable").find("div:first-child .span6:last-child .tm-p-").text()
        print(content)
        print(text)
        




