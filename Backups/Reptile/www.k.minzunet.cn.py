import re
import Request_Header
import pyquery as pq
total_url = "http://www.k.minzunet.cn"
url = "http://www.k.minzunet.cn/mzwhzyk/674771/index.html"
# url = "http://www.k.minzunet.cn/mzwhzyk/674771/682366/682367/f4ff9f9f-1.html" # 二级列表页
# url ="http://www.k.minzunet.cn/mzwhzyk/674771/682366/682367/672476/index.html" # 详情
key_list = ["宗教","文化","艺术","建筑","饮食","歌舞","语言","风俗","节日"]
Secondary_url_dict = {}


# with open("1.html","r",encoding="utf-8") as f:
#     html = f.read()
doc = Request_Header.request_py(url)
# print(doc)
# doc = pq(html)


# contents = doc(".class_nav li").find("a").items() 首页

# 二级列表页
# contents = doc(".easysite-list-modelone li").find("a").items()
# next_pages = doc(".easysite-page-wrap a").filter(lambda i,this: pq.PyQuery(this).attr("title") == "下一页")
# print(next_pages.attr("tagname")) # 获取下一页网址
#
#
# # 详情页
# # title = doc(".detail_con").find("h2").text()   //*[@id="tw_lb"]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/a[3]
# # print(title)
# # contents = doc(".detail_inner").find("p").items()
# for content in contents:
#     print(content.text())
#     print(content.attr("href"))

def content_list(url):
    doc = Request_Header.request_py(url)
    contents = doc(".classification li").items()
    for content in contents:
        if content.find(("a")) == 1:
            continue
        else:
            name = content("a").filter(lambda i, this: pq.PyQuery(this).attr("href") == "javascript:void(0);")
            if name.text()[2:4] in key_list:
                ass = content('.second-nav').find("a").items()
                for a in ass:
                     url = a.attr("href")
                     print(url)
    #     print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    #     names = content.find("a").items()
    #     for name in names:
    #         key = name.text()
    #         name_list.append(key)
    #         # if key[2:4] in key_list:
    #         #     print(key)
    #     print(name_list[0][2:4],name_list)
    #     if name_list[0][2:4] in key_list:
    #         print("&&&&&")
    #         for name in names:
    #             print(name)
    #             url = name.attr("href")
    #             title = name.text()
    #             Secondary_url_dict[url]=title
    # print(Secondary_url_dict)

    #     title = content.text()
    #     url = content.attr("href")
    #     secdond_url = total_url + url
    #     if title[2:4] in key_list:
    #         Secondary_url_dict[secdond_url] = title
    # print(Secondary_url_dict)

if __name__ == '__main__':
    content_list(url)