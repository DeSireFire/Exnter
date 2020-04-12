# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 18:37
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: demo.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire

import requests
import re
import os
import chardet
import asyncio
import copy







def requests_handler(url):
    cookies = 'ipb_member_id=715432; ipb_pass_hash=e05c94c921a9ed3aa93f7937553febc5; igneous=3472f6fa9; sk=6gyz6cmjzamaftpgbfwvcnzpdgpq'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookies,
        'Host': 'exhentai.org',
        'Referer': 'https://exhentai.org',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    proxies = {
        'http': "127.0.0.1:10808",
        'https': "127.0.0.1:10808",
    }
    try:
        response = requests.get(url, headers=headers, timeout=60)
        return response
    except Exception as T:
        count = 0  # 重试次数
        RETRY_TIME = 10
        while count < RETRY_TIME:
            print('%s 重试 %s 次' % (url, count))
            try:
                r = requests.get(url=url, headers=headers, timeout=60)
                r.encoding = chardet.detect(r.content)['encoding']
                if (not r.ok) or len(r.content) < 500:
                    raise ConnectionError
                else:
                    return r
            except Exception:
                count += 1
    return None


def down_img(url):
    img_re = '<img id="img" src="(.*?)" style="'
    img_re_title = '<title>(.*?)</title>'
    html = requests_handler(url).text
    tempList = reglux(html, img_re, False)
    nameList = reglux(html, img_re_title, False)
    imgUrl = ''.join(tempList)
    bookName = ''.join(nameList)
    imgName = imgUrl.split('/')[-1]
    pathName = os.path.join(bookName, imgName)
    if not os.path.exists(pathName):
        imgByte = requests_handler(imgUrl).content
        if imgByte:
            save_file(url, bookName, imgName, imgByte)


def save_file(url, dirName, fileName, fileByte):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    pathName = os.path.join(dirName, fileName)
    with open(pathName, "wb") as code:
        print('正在保存'+fileName)
        code.write(fileByte)


def img_urls(tempStr):
    re_rule = '<a href="https://exhentai.org/s/(.*?)">'
    tempList = reglux(tempStr, re_rule, False)
    return ['https://exhentai.org/s/'+i for i in tempList]


def main():
    html = requests_handler('https://exhentai.org/g/805026/5b64afef99/').text
    imgUrlList = img_urls(html)
    print(len(imgUrlList))

    img_re_title = '<title>(.*?)</title>'
    dirName = ''.join(reglux(html, img_re_title, False))


    for i in imgUrlList:
        print('检索 %s 分页图片' % i)
        down_img(i)



if __name__ == '__main__':
    main()
    # Python 3.7+
    # asyncio.run(main())