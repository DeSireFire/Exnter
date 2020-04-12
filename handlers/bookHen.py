# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 20:13
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: imgHen.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire


from comm.webGet import Html_Downloader
# from config import *


class GetBooksInfo(object):
    def __init__(self, book_url=None):
        self.bookHtml = ''
        self.book_id = ""
        self.book_url = book_url

        # re
        self.book_idRE = "https://exhentai.org/g/(\d*?)/.*/"
        self.titleRE = "<title>(.*?)</title>"

        self.bookInfo = {
            "url": self.book_url,
            "id": self.book_id,
            "title": "unknown",
            "total": 0,
            "getTotal": 0,
            "groupPagesList": [self.book_url],
            "subPagesList": [],
            "imgUrlList": [],
        }
        if self.book_url:
            self.bookHtml = Html_Downloader.download(self.book_url).text or ''
            self.book_id = ''.join(Html_Downloader.reglux(self.book_url, self.book_idRE, False))
            self.bookInfo["title"] = ''.join(Html_Downloader.reglux(self.book_url, self.titleRE, False))

    def get_group_pages(self):
        '''
        获取本子所有g分页
        '''
        re_rule = '<a href="(%s\?p=\d*)" onclick="return false">' % self.book_url
        tempList = Html_Downloader.reglux(self.bookHtml, re_rule, False)
        self.bookInfo["groupPagesList"] = self.bookInfo["groupPagesList"] + sorted(set(tempList), key=tempList.index)
        return self.bookInfo["groupPagesList"]

    def get_sub_pages(self):
        '''
        获取本子所有s分页
        :return:
        '''
        # 检查G分页小于等于1时，自己启动get_group_pages方法获取所有G分页
        if len(self.bookInfo['groupPagesList']) <= 1:
            self.get_group_pages()

        # 获取当前G分页的所有S分页URL
        re_rule = '<a href="https://exhentai.org/s/(.*?)"><img alt='
        tempList = Html_Downloader.reglux(self.bookHtml, re_rule, False)
        for gp in self.bookInfo['groupPagesList'][1:]:
            temp_html = Html_Downloader.download(gp).text
            tempList += Html_Downloader.reglux(temp_html, re_rule, False)

        sortList = sorted(set(tempList), key=tempList.index)
        self.bookInfo['subPagesList'] = ['https://exhentai.org/s/'+i for i in sortList]
        return self.bookInfo['subPagesList']

    def get_img_url(self):
        '''
        获取本子所有s分页中图片的地址
        :return:
        '''
        # 检查G分页小于等于1时，自己启动get_group_pages方法获取所有G分页
        if len(self.bookInfo['subPagesList']) <= 1:
            self.get_sub_pages()

        # 获取当前G分页的所有S分页URL
        re_rule = '<img id="img" src="(.*?)" style='
        for sp in self.bookInfo['subPagesList']:
            temp_html = Html_Downloader.download(sp).text
            self.bookInfo['imgUrlList'] += Html_Downloader.reglux(temp_html, re_rule, False)

        return self.bookInfo['imgUrlList']


