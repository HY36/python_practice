# -*- coding: utf-8 -*-

# 协程的自动切换
import gevent
import time


def func1():
    print('\033[31:1m 正在执行 111...\033[0m')
    gevent.sleep(2)
    print('\033[31:1m 正在执行 444...\033[0m')


def func2():
    print('\033[32:1m 正在执行 222...\033[0m')
    gevent.sleep(3)
    print('\033[32:1m 正在执行 333...\033[0m')


start_time = time.time()
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2)
])
end_time = time.time()

print("spend ", (end_time - start_time), " second")
