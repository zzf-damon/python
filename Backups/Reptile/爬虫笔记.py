# class ChromePage():
#     def __init__(self, keyword, page):
#         self.browserC = webdriver.Chrome()
#         desired_capabilities = DesiredCapabilities.CHROME
#         desired_capabilities["pageLoadStrategy"] = "none"
#         self.waitC = WebDriverWait(self.browserC, 10)
#         self.keyword = keyword
#         self.page = page
#
#     def chrome_main(self):
#         self.browserC.get(
#             "https://weixin.sogou.com/weixin?query=" + self.keyword + "&type=2&page=" + self.page)
#         print(self.browserC.current_url)
#         page = int(self.page)
#         for i in range(page, 10):
#             i = i + 1
#             print("开始爬取第%d页" % i)
#             self.signC = list_url(self.browserC, self.waitC)
#             if signA is True:
#                 submit = self.waitC.until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, '#sogou_next'))
#                 )
#                 submit.click()
#         quit()



# 世界上常用的请求头
www.useragentstring.com/pages/useragentstring.php?typ=Browser