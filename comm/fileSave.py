# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 17:36
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: fileSave.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire

import os
from config import BASEPATH
import re


def clean(text):
    """
    文件名清洗
    :param text:
    :return:
    """
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\[\S+\]", "", text)      # 去除表情符号
    # text = re.sub(r"#\S+#", "", text)      # 保留话题内容
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)       # 去除网址
    text = re.sub(r"\s+", " ", text)        # 合并正文中过多的空格
    return text.strip()

def save_file_byte(dirName, fileName, fileByte):
    '''
    保存非文本文件
    :param dirName: 文件夹名
    :param fileName: 文件名
    :param fileByte: 文件数据
    :return:
    '''
    pathName = os.path.join(BASEPATH, "save", clean(dirName), fileName)
    if not os.path.exists(os.path.join(BASEPATH, "save", clean(dirName))):
        os.makedirs(os.path.join(BASEPATH, dirName))
    print(pathName)
    with open(pathName, "wb") as code:
        print('正在保存'+fileName)
        code.write(fileByte)


def save_text(dirName, text):
    """
    文本文件保存
    :param dirName: 文件夹名
    :param fileName: 文件名
    :param fileByte: 文件数据
    :return:
    """
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    pathName = os.path.join(dirName, 'temp')
    with open(pathName, "wb") as code:
        code.write(text)

if __name__ == '__main__':
    dirName = 'DEMO'
    fileName = '1.jpg'
    save_file_byte(dirName, fileName, b'3253534')