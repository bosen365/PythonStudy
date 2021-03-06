#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'进程线程'
__author__ = 'click'
__date__ = '2018/7/20 下午6:02'
import os, time, random

from multiprocessing import Process, Pool

print("当前进程的ID %s" % (os.getpid()))

print('fork进程')

pid = os.fork();
if pid == 0:
    print('我是子进程我的编号是%1s,我的父进程的编号是%2s' % (os.getpid(), os.getppid()))
else:
    print('我是父进程我的编号是%1s,我刚刚创建了一个子进程,编号是%2s' % (os.getpid(), pid))


# 使用process对象进行创建进程

def run_proc(name):
    print('创建进程的名字为%s' % (name))


if __name__ == '__main__':
    print('-----------------------')
    print('创建子进程的父进程ID是%s' % (os.getpid()))
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print('执行完了')


# 多进程代码实现

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 必须要先进行close,然后才能进行join()
    p.close()
    p.join()
    print('All subprocesses done.')
