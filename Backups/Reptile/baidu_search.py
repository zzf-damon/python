#-*-coding:utf-8-*-

import requests,re
from bs4 import BeautifulSoup
from multiprocessing import Pool

headers = {  
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
	'Accept-Encoding': 'gzip, deflate, compress',  
	'Accept-Language': 'en-us;q=0.5,en傣族;q=0.3',  
	'Cache-Control': 'max-age=0',  
	'Connection': 'keep-alive',  
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'  
}

def gain_url(url):
	f=open("url.txt","a+")
	try:
		msg=requests.get(url,headers=headers)
		a=msg.text.encode("utf-8", "ignore").decode('utf-8')
		#p=r"(?=URL=\').+?(?=\'\"></noscript>)"
		#result = re.compile(p)
		#url_list=result.findall(a)
		f.write(msg.url+'\n')
		f.close()
		print(msg.url)
	except:
		print("页面无法访问")
	
def gain_result(q,page):
	url="https://www.baidu.com/s?wd="+str(q)+"&pn="+str(page)+"0&oq=inurl%3Aphp%3Fid%3D&ie=utf-8&rsv_idx=1&rsv_pq=9b97f395000066c1&rsv_t=d7cawxJPu0sWL9GdZrVerLepGX%2Bm%2B8Gz%2BP%2BCna7MCI7Ji%2FJwpzkV0uwY7D4"
	
	msg=requests.get(url,headers=headers)
	#a=msg.text.encode("gbk", "ignore").decode('gbk')
	soup=BeautifulSoup(msg.content,"html.parser")
	url_list=soup.find_all(class_="c-tools")
	for url in url_list:
		url=str(url)
		start=url.find("url\":")
		end=url.find("}")
		end_url=url[start+6:end-1]
		gain_url(end_url)

def chongfu():
	url_list=[]
	f=open("url.txt","r")
	for url in f.readlines():
		url_list.append(url)
		
	url_list=list(set(url_list))
	f=open("new_urls.txt","a+")
	for url in url_list:
		f.write(url)
	f.close()
	
if __name__=="__main__":	
	# q=input("请输入你要百度的内容: ").encode('utf-8')
	# m=input("请输入要爬取的总页数: ")
	q = "傣族"
	m = 2
	# pnums=input("请输入线程池的个数: ")
	pnums = 1
	p=Pool(int(pnums))
	for i in range(0,int(m)):
		p.apply(func=gain_result,args=(q,i,))		#i为百度搜索结果的页数

	p.close()
	p.join()
	chongfu()