import requests
from Request_Header import headers

url = "https://www.csdn.net/"
headers1 = {
'Host': "www.csdn.net",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.2 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "uuid_tt_dd=10_30693706620-1598163561351-120675; dc_session_id=10_1598163561351.513398; announcement=%257B%2522isLogin%2522%253Afalse%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fyzkskaka%252Fats4dBdZ%253Futm_source%253D908346557%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; Hm_up_facf15707d34a73694bf5c0d571a4a72=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; Hm_ct_facf15707d34a73694bf5c0d571a4a72=6525*1*10_30693706620-1598163561351-120675; c_adb=1; dc_sid=c5ae49e07304d8a165136952ce7330ca; csrfToken=xvI0OSbU-4cOCvbZavorHcpm; c_segment=3; Hm_lvt_facf15707d34a73694bf5c0d571a4a72=1598163568,1598163624; c-login-auto-interval=1598163727958; c_first_ref=www.baidu.com; c_ref=http%3A//www.baidu.com/link; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30693706620-1598163561351-120675; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; c_first_page=https%3A//blog.csdn.net/qq_35912490/article/details/104229930; c_page_id=default; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1598166426,1598166454; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1598166454; dc_tos=qfi97l; Hm_lpvt_facf15707d34a73694bf5c0d571a4a72=1598166564"
}


r = requests.get(url, verify=False)




print(r.text)


