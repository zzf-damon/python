# -*- coding: utf-8 -*-
import os
import random
import time
import scrapy
import json
from datetime import datetime

from lxml import etree
import uuid
import re
import requests
from ..Utils import utilsModel
from ..items import ZhfycrawlItem, PlxxItem
from ..models import DateFormatHelper
# from ..time_source import Time_Source


class WeiboSpider1(scrapy.Spider):
    utils = utilsModel()
    name = 'weibo_1'
    uidIndex = 1  # 转到下一个关键词时uidindex从1开始
    page = 1
    cards = []
    keyuid, keyuidcount = utils.get_sinaweibo(name, 0)  # 入口链接取第一个关键词，index直接传0。
    # random.shuffle(RKLJ)

    base_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'.format(
        page=page, uid=keyuid)
    start_urls = [base_url]

    def parse(self, response):
        label_filter = re.compile(r'</?\w+[^>]*>', re.S)
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        try:
            data = response.text
            content = json.loads(data).get('data')
            self.cards = content.get('cards')
            if self.cards:
                for card in self.cards:
                    item = ZhfycrawlItem()
                    card_type = card.get('card_type')
                    if card_type == 9:
                        seedUrl = card.get('scheme')
                        mblog = card.get('mblog')
                        user = mblog.get('user')
                        yqly = user.get('screen_name')
                        # 时间
                        original_time = mblog.get('created_at')
                        # 博文ID
                        m_id = mblog.get('mid')
                        # text
                        if mblog.__contains__('retweeted_status'):
                            text = mblog.get('retweeted_status')['text']
                        else:
                            text = mblog.get('text')
                        # 标题
                        if "<br />" in text:
                            title_ = text.split('<br />')[0]
                            title = label_filter.sub('', title_)
                        elif '【' and '】' in text:
                            text_ = label_filter.sub('', text)
                            # 【】里面的内容一般为正文摘要，正则匹配到存在字段weibo_title
                            title_ = ''.join(re.findall(r'【(.*?)】', text_, re.S)).replace('#', ''). \
                                replace('\t', '').replace('\n', '').replace('\xa0', '').strip()
                            title = '【'+title_+'】'
                        elif mblog.__contains__('page_info'):
                            page_info = mblog.get('page_info')
                            title = page_info.get('page_title')
                        else:
                            title = label_filter.sub('', text)[:20]+"..."
                        # pagehtml = self.get_HTML(seedUrl)
                        pagehtml = text
                        # 正文
                        text_etree = etree.HTML(text)
                        content_origin = ''.join(text_etree.xpath("//text()")).replace('\t', '')\
                                        .replace('\n', '').replace('\xa0', '').strip()
                        # 去除正文中的表情
                        try:
                            # python UCS-4 build的处理方式
                            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
                        except re.error:
                            # python UCS-2 build的处理方式
                            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
                        content = highpoints.sub('', content_origin)
                        releaseTime, collectionTime = DateFormatHelper.parse_time(original_time)
                        item['FBSJ'] = releaseTime
                        item['YQURL'] = seedUrl
                        item['YQBT'] = title
                        item['SABZ'] = "0"
                        item['CLBZ'] = "00000000000000000000"
                        item['LXDM'] = "0"
                        item['ZQWZ'] = "新浪微博"
                        item['YQLY'] = yqly
                        item['SYBZ'] = "1"
                        item['ZQRQ'] = collectionTime
                        item['YQBH'] = uuid.uuid1()
                        item['URLID'] = self.utils.encrypt_url(str(seedUrl))
                        item['HTML'] = str(pagehtml)
                        # item['AJBH'] = ""
                        item['YQLX'] = "0"
                        item['YQNR'] = content
                        item['PLXX'] = ""
                        now_time = datetime.now()
                        releasetime = datetime.strptime(item['FBSJ'], "%Y-%m-%d %H:%M:%S")
                        item_days = (now_time - releasetime).days + 1
                        if item_days < 3 and item['YQNR'] != '':  # 爬取存储控制
                            yield item
                            '''每个mid去爬取评论信息，不用cookie只能爬2页
                               鉴于大多数博文的评论较少，只爬1页，加快爬虫速度
                            '''
                            # comment_page = 1
                            # head_url = "https://m.weibo.cn/api/comments/show?id={0}&page=1".format(m_id)
                            # yield scrapy.Request(url=head_url, callback=self.get_comment,
                            #                      meta={'info': item}, dont_filter=True)
                            # if comment_page < 2:
                            #     comment_page = comment_page + 1
                            #     head_url = "https://m.weibo.cn/api/comments/show?id={0}&page={1}".format(m_id, comment_page)
                            #     yield scrapy.Request(url=head_url, callback=self.get_comment,
                            #                          meta={'info': item}, dont_filter=True)

        except Exception as e:
            print(e)

        # 翻页
        if self.page < 3 and self.cards:
            self.page = self.page + 1
            time.sleep(3)
            yield scrapy.Request(
                'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'.format(
                    page=self.page, uid=self.keyuid), callback=self.parse, dont_filter=True)
        # 下一个大V号
        else:
            if self.uidIndex < self.keyuidcount:
                # 如果当前uid爬取结束，则发送爬取下一个uid的请求
                self.page = 1
                self.keyuid, _ = self.utils.get_sinaweibo(self.name, self.uidIndex)
                yield scrapy.Request(
                    'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'.format(
                        page=self.page, uid=self.keyuid), callback=self.parse, dont_filter=True)
                self.uidIndex = self.uidIndex + 1  # uidIdex自增应该放在底下，不然关键词列表索引会超出范围。
                time.sleep(5)

    def get_HTML(self, Url):
        resp = requests.get(Url)
        HTML = resp.text
        return HTML

    # 提取评论function
    def get_comment(self, response):
        label_filter = re.compile(r'</?\w+[^>]*>', re.S)
        plnr_list = []
        item_list = []
        try:
            resp = response.text
            comment_json = json.loads(resp)
            if comment_json['ok'] == 1:
                comment_dict = comment_json['data']
                comment_list = comment_dict['data']
                for comment_data in comment_list:
                    plxx_list = [0, 1, 2, 3, 4]
                    # try:
                    # 需新建一个舆情评论信息表，yd_plxx
                    if comment_data.__contains__('reply_text'):
                        # 1 评论内容
                        plnr_origin = label_filter.sub('', comment_data['reply_text'])
                        # reply_id = comment_data['reply_id']
                        # 2 微博评论日期
                        plrq_origin = comment_data['created_at']
                        # 3 评论人
                        plr = comment_data['user']['screen_name']
                        # 4 评论编号uuid
                        plbh = uuid.uuid1()
                    else:
                        # 评论内容
                        plnr_origin = label_filter.sub('', comment_data['text'])
                        # 微博评论日期
                        plrq_origin = comment_data['created_at']
                        # 评论人
                        plr = comment_data['user']['screen_name']
                        # 评论编号uuid
                        plbh = uuid.uuid1()
                    if plnr_origin != "":
                        # 去除表情
                        try:
                            # python UCS-4 build的处理方式
                            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
                        except re.error:
                            # python UCS-2 build的处理方式
                            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
                        plnr = highpoints.sub('', plnr_origin)
                        plnr_list.append(plnr)
                        # time_ = Time_Source.time_matching(plrq_origin)
                        plrq, not_used = DateFormatHelper.parse_time(plrq_origin)
                        plxx_list[0] = plnr
                        plxx_list[1] = plrq
                        plxx_list[2] = plr
                        plxx_list[3] = plbh
                        # 情感代码
                        plxx_list[4] = "0"
                        item_list.append(plxx_list)
                    else:
                        continue
                    # except KeyError:
                    #     pass
                # item是个字典
                item = response.meta['info']
                # 将plnr_list里的所有评论按'\n'拼接成字符串
                plxx = '\n'.join(plnr_list)
                item['PLXX'] = plxx
                yield item
                item_plxx = PlxxItem()
                for item_ in item_list:
                    item_plxx['PLNR'] = item_[0]
                    item_plxx['PLRQ'] = item_[1]
                    item_plxx['PLR'] = item_[2]
                    item_plxx['PLBH'] = item_[3]
                    item_plxx['QGDM'] = item_[4]
                    item_plxx['YQBH'] = item['YQBH']
                    yield item_plxx
            else:  # 'ok':0，当前页为空，跳到下一个ID   只传YQXX表
                item = response.meta['info']
                plxx = ""
                item['PLXX'] = plxx
                yield item
        except KeyError:
            pass
