from Request_Header import request_py, write, nav_details, file_name
from multiprocessing import Queue, Process
import threading

total_url = "http://www.minzu56.net"
dict_url = {}
url_list = []
list_url = []


def thread(q):
    i = 0
    while True:
        url = q.get(True)
        i += 1
        print("正在爬去第%d个网址: %s" % (i, url))
        if url == "这是终极测试":
            print("这是终极测试——————说明读进程应该终止")
            break
        else:
            t = threading.Thread(target=details, args=(url,))
            t.start()
            t.join()
    print("爬取的评论列表已经完成")


def details(url):
    doc = request_py(url)
    path = file_name(url)
    contents = doc('.article').find('p').items()
    title = doc(".article h1").text()
    write("****************" + "\n" + title, path)
    for content in contents:
        content = content.text()
        write(content, path)


def content_list(url):
    next_page = []
    doc = request_py(url)
    url_lists = doc('.leftwrap').find('a').items()
    for url_context in url_lists:
        url_html = url_context.attr("href")
        url_list = url_html.split("/")[-1][:-5]
        title = url_context.text()
        if url_html[-5:] == ".html" and url_list.isdigit() and title != "":
            url = total_url + url_html
        else:
            if title == "下一页":
                url = url + url_html
                next_page.append(url)
            continue
        dict_url[url] = title
    if next_page:
        content_list(next_page[0])
    return dict_url


def main(q):
    for key1 in list_url:
        url = total_url + key1
        key2_list = nav_details(url)
        print(key2_list)
        if key2_list:
            for key2 in key2_list:
                url = total_url + key2
                url_list.append(url)
        else:
            url_list.append(url)
    for url in url_list:
        if url[-5:] == ".html":
            details(url)
        else:
            content_list(url)
    for key in dict_url.keys():
        q.put(key)
    q.put("这是终极测试")


if __name__ == "__main__":
    q = Queue()
    doc = request_py(total_url)
    contents = doc('#nav').find('a').items()
    for content in contents:
        str = content.attr("href")
        if len(str.split("/")) > 2:
            list_url.append(str)
    pw = Process(target=main, args=(q,))
    pr = Process(target=thread, args=(q,))
    pw.start()
    pr.start()
    pr.join()
