# -*- coding:utf-8 -*-
from Queue import Queue
from random import randint
from time import sleep,ctime
import threading
#创建生产者线程
class writer(threading.Thread):
    def __init__(self,queue,nloops):
        threading.Thread.__init__(self)
        self.queue=queue
        self.nloops=nloops

    def run(self):
        print '生产者线程运行开始',ctime()
        sleep(1)
        for i in range(self.nloops):
            self.writerq()
        print '生产者线程运行结束',ctime()

    def writerq(self):
        self.queue.qsize()
        self.queue.put('xxx',1)
        sleep(randint(2,5))
        print '放入消息,结束放入消息,现在的消息深度',self.queue.qsize(),self.queue.empty()

#创建消费者线程
class reader(threading.Thread):
    def __init__(self,queue,nloops):
        threading.Thread.__init__(self)
        self.queue=queue
        self.nloops=nloops

    def run(self):
        print '消费者线程运行开始',ctime()
        sleep(1)
        for i in range(self.nloops):
            self.readerq()
        print '消费者线程运行结束',ctime()

    def readerq(self):
        self.queue.qsize()
        val=self.queue.get(1)
        sleep(randint(5, 10))
        print '读取消息,结束读取消息,现在的消息深度',self.queue.qsize(),self.queue.empty()


def main():
    print '处理开始',ctime()
    threads=[writer,reader]
    thread_list=[]
    q=Queue(32)
    #创建线程实例，并把线程加入到线程列表中
    for i in range(len(threads)):
        t=threads[i](q,randint(2,5))
        thread_list.append(t)
    #启动线程列表里面的线程
    for i in range(len(thread_list)):
        thread_list[i].start()
    #等待线程列表里面所有线程结束
    for i in range(len(thread_list)):
        thread_list[i].join()
    print '处理结束',ctime()

if __name__=='__main__':
    main()
