import requests
from lxml import etree # 是一个专门用于xml的库

res = requests.get("https://www.qiushibaike.com/8hr/page/1/")

res

res_xpath = etree.HTML(res.text)

res_xpath

res_xpath.xpath('/html/head/title/text()') # 绝对路径的提取

res_xpath.xpath('//title/text()') # 相对路径的提取

res_xpath.xpath("//a[@class='recmd-content']/text()") # 批量提取指定属性，两个指定属性之间可以用and连接

res_xpath.xpath("//*[@class='recommend-article']/ul/li//a[@class='recmd-content']/text()") # 批量提取指定属性，两个指定属性之间可以用and连接

res_xpath.xpath("//ul/li//a[@class='recmd-content']/text()") # 批量提取指定属性，两个指定属性之间可以用and连接

res_xpath.xpath("//) # 批量提取指定属性，两个指定属性之间可以用and连接ul/li//a[@class='recmd-content']/text()")