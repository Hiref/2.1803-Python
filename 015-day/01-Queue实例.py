from multiprocessing import Process , Queue
import os
import time
#import random

def write(q):
	for value in ['A-TH','B-TL','C-SE']:
		print("Put %s to QUEUE ..."% value)
		q.put(value)
		time.sleep(0.8)

def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("Get %s from queue"%value)
			time.sleep(0.8)
		else: 
			break
if __name__=='__main__':
		#父进程创建Queue,并传给各子进程
		q = Queue()
		pw = Process(target = write,args = (q,))
		pr = Process(target = read,args = (q,))
		pw.start()
		pw.join()
		pr.start()
		pr.join()
		print(' ')
		print("读取完毕")














