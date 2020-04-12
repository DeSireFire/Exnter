# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 16:14
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: main.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire


from handlers.bookHen import GetBooksInfo
from handlers.downLoadHen import downLoaderSave


def main():
    # 实例化本子对象
    # book = GetBooksInfo('https://exhentai.org/g/805026/5b64afef99/')
    book = GetBooksInfo('https://exhentai.org/g/1488373/eaa261cf13/')
    book.get_img_url()
    print(book.bookInfo)
    downLoaderSave(book.bookInfo)


if __name__ == '__main__':
    main()
