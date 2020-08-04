import time
import json
import requests
from selenium import webdriver

for num in range(0,50000):
    URL_BIG = 'https://www.jufaanli.com/album/tanwutryout/lawyerSearch?TypeKey=&Page={}'.format(num)
    post = {}
    user = "15949527066"
    password = "mxd66ilove"
    driver = webdriver.Firefox()
    driver.get(URL_BIG)
    time.sleep(3)
    # driver.find_element_by_xpath("//div[@id='login-Reg']/span[@id='loginReg']/a[@id='loginObj']/span").click()
    # time.sleep(3)
    print("正在输入用户名和密码")
    # 清空登录框
    driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='userObj']").clear()
    # 自动填入登录用户名
    driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='userObj']").send_keys(user)
    # 清空密码框
    driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='pwdObj']").clear()
    # 自动填入登录密码
    driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='pwdObj']").send_keys(password)

    time.sleep(1)
    # 点击登录按钮进行登录
    driver.find_element_by_xpath("//div[@class='col-sm-offset-2 col-sm-9 jufa-col-lg-9']/button[@id='subLogin']").click()
    time.sleep(1)
    driver.get(URL_BIG)
    # 获取cookies
    cookie_items = driver.get_cookies()

    # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
    for cookie_item in cookie_items:
        post[cookie_item['name']] = cookie_item['value']
    cookie_str=json.dumps(post)
    with open('cookie.txt', 'w', encoding='utf-8') as f:
        f.write(cookie_str)
    f.close()
    print("登录完成")

    url1 = "https://www.jufaanli.com/home/search/searchJson"
    res = requests.get(url1).text
    result = json.loads(res)
    search_list = result['info']
    search_list = search_list['searchList']['list']
    for i in search_list:
        dict = {}
        uuid = i['uuid']
        id = i['id']
        title = i['title']
        lable = i['label']
        type = i['type']
        fayuan = i['add']
        num = i['num']
        date= i['date']
        ctype = i['ctype']
        presname = i['presname']
        jresult = i['jresult']
        judgeRole = i['judgeRole']
        attitude_for_prevround = i['attitude_for_prevround']
        focus = i['focus']
        listTag = i['listTag']
        case_textlen = i['case_textlen']
        money = i['money']
        yqtx = i['yqtx']
        gjc = i['gjc']

        dict['uuid'] = uuid
        dict['id'] = id
        dict['title'] = title
        dict['lable'] = lable
        dict['type'] = type
        dict['fayuan'] = fayuan
        dict['num'] = num
        dict['date'] = date
        dict['ctype'] = ctype
        dict['presname'] = presname
        dict['jresult'] =jresult
        dict['judgeRole'] = judgeRole
        dict['attitude_for_prevround'] = attitude_for_prevround
        dict['focus'] = focus
        dict['listTag'] = listTag
        dict['case_textlen'] = case_textlen
        dict['money'] = money
        dict['yqtx'] = yqtx
        dict['gjc'] = gjc

        url_i = "https://www.jufaanli.com/album/tanwutryout/wenshu/{}/?q=&src=search".format(uuid)
        time.sleep(3)
        user = "15949527066"
        password = "mxd66ilove"
        driver = webdriver.Firefox()
        driver.get(url_i)
        time.sleep(3)
        # driver.find_element_by_xpath("//div[@id='login-Reg']/span[@id='loginReg']/a[@id='loginObj']/span").click()
        # time.sleep(3)
        print("又一次输入用户名和密码")
        # 清空登录框
        driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='userObj']").clear()
        # 自动填入登录用户名
        driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='userObj']").send_keys(user)
        # 清空密码框
        driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='pwdObj']").clear()
        # 自动填入登录密码
        driver.find_element_by_xpath("//div[@class='col-lg-9 jufa-col-lg-9']/input[@id='pwdObj']").send_keys(password)
        time.sleep(1)
        # 点击登录按钮进行登录
        driver.find_element_by_xpath(
            "//div[@class='col-sm-offset-2 col-sm-9 jufa-col-lg-9']/button[@id='subLogin']").click()
        time.sleep(3)
        driver.get(url_i)
        # 获取cookies
        cookie_items = driver.get_cookies()
        # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
        for cookie_item in cookie_items:
            post[cookie_item['name']] = cookie_item['value']
        cookie_str = json.dumps(post)
        with open('cookie.txt', 'w', encoding='utf-8') as f:
            f.write(cookie_str)
        f.close()
        print("登录二级完成")

        data = driver.find_element_by_xpath("//html").text
        data1 = data.replace('可视化搜索\n案例搜索\n法规搜索\n刑事HOLO搜索\n全部内容\n159495...\n目录\n基本信息\n下载Word\n下载PDF\n收藏\n手机看\n','')
        content = data1.replace('意见反馈\n指南\n引导\n微信\nAPP\n置顶\n关于聚法\n了解我们\n媒体报道\n合作伙伴\n使用指南\n友情链接\n吉大法学院\n最高人民法院\n中国裁判文书网\n吉大司法数据应用研究中心\n联系我们\n联系我们\n意见反馈\n商务合作：  hezuo@jufaanli.com\n地址：  长春市高新区前进大街2326号创展国际大厦2101室\n微信公众平台\n手机登录：m.jufaanli.com\nAndroid\niOS\n© 2019 Jufaanli.com.All Rights Reserved 吉ICP备16004680号-1 \n聚法科技（长春）有限公司','')
        dict['content'] = content
        print(dict)
        # path = 'data.json'
        # with open(path,'a',encoding='utf8') as f_write:
        #     json.dump(dict, f_write,ensure_ascii = False)
        f = open("data.json", "a",encoding='utf8')
        data_string = json.dumps(dict,ensure_ascii=False)
        f.write(data_string)
        f.write('\n')
        time.sleep(3)
        driver.quit()
    driver.quit()