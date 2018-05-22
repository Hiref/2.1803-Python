from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
	print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid))
	for i in range(q.qsize()):
		print("reader从Queue获取到消息:%s"%(os.getpid,os.getppid))
		for i in "laowang":
		q.put(i)

def writer(q):
	print("writer")




if __name__=="__main__":
	print("(%s) start"%os.getpid())
	q=Manager().Queue()
#使用Manager中的Queue来初始化
	po = Pool()

	po.apply(writer,ages(q,))
	po.apply(reader,ages(q,))
	po.close()
	po.join()
	print("(%s) End"%os.getpid())














