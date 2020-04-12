# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 15:57
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: webGet.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire

import requests
import random
import config
import chardet
import json
import re


class Html_Downloader(object):

    @staticmethod
    def download(url):
        """
        获取网页
        :param url: 请求的网页地址
        :return: 返回网页内容
        """
        try:
            # 网页请求成功
            r = requests.get(url=url, headers=config.HEADERS, timeout=config.TIMEOUT)
            print("请求url: %s" % url)

            # 获取网页编码格式，并修改为request.text的解码类型
            r.encoding = chardet.detect(r.content)['encoding']
            if r.encoding == "GB2312":
                r.encoding = "GBK"

            # 网页请求OK或者请求得到的内容过少，判断为连接失败
            if (not r.ok) or len(r.content) < 500:
                raise ConnectionError
            else:
                return r

        except Exception as E:
            print(E)
            count = 0  # 重试次数

            while count < config.RETRY_TIME:
                try:
                    r = requests.get(url=url, headers=config.HEADERS, timeout=config.TIMEOUT)
                    r.encoding = chardet.detect(r.content)['encoding']
                    if (not r.ok) or len(r.content) < 500:
                        raise ConnectionError
                    else:
                        return r
                except Exception:
                    count += 1

        return None

    @staticmethod
    def reglux(html_text, re_pattern, nbsp_del=True):
        '''
        正则过滤函数
        :param html_text: 字符串，网页的文本
        :param re_pattern: 字符串，正则表达式
        :param nbsp_del: 布尔值，控制是否以去除换行符的形式抓取有用信息
        :return:
        '''
        pattern = re.compile(re_pattern)
        if nbsp_del:
            temp = pattern.findall("".join(html_text.split()))
        else:
            temp = pattern.findall(html_text)
        if temp:
            return temp
        else:
            return ['暂无数据']

