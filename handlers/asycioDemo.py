# coding=utf8
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 0:42
# @Author  : RaXianch
# @project: exDownloader.py
# @FileName: downLoadHen.py
# @Software: PyCharm
# @github    ：https://github.com/DeSireFire

from comm.webGet import Html_Downloader
# from config import *
import asyncio
import random
async def demo():
    test = {'name':'demo'}
    for i in range(1,10):
        print('Hello ...')
        ts = random.randint(1,10)
        await asyncio.sleep(ts)
        print('... World!')
        test[i] = ts
    print(test)

async def dem2o():
    test = {'name':'dem2o'}
    for i in range(1, 10):
        print('bye ...')
        ts = random.randint(1, 10)
        await asyncio.sleep(ts)
        print('... World!')
        test[i] = ts
    print(test)


# 创建协程对象
co = demo()
co2 = dem2o()

# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(co,co2))