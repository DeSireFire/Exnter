# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 16:14
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: config.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire
import os
BASEPATH = os.path.abspath(os.path.dirname(__file__))

COOKIES = 'ipb_member_id=715432; ipb_pass_hash=e05c94c921a9ed3aa93f7937553febc5; igneous=3472f6fa9; sk=6gyz6cmjzamaftpgbfwvcnzpdgpq'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': COOKIES,
    'Host': 'exhentai.org',
    'Referer': 'https://exhentai.org',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

TIMEOUT = 60

RETRY_TIME = 5
