from multiprocessing import Process ,Queue
import os , time , random

list = []

def write(q):
	list.append("a")
	print('write process' + str(list))
	for value in ['A','B','C']:
		print('Put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print("rand process" +str(list))
	if len(list) != 0:
		print('list')
	while True:
		if not q.empty():
			value = q.get(True)
			print('Get %s from queue.'%value)
			time.sleep(0.8)
		else:
			break

q = Queue()
pw = Process(target = write,args =(q,))
pr = Process(target = read,args = (q,))
pw.start()
pw.join()
pr.start()
pr.join()
print('＿＿＿＿＿运行完成＿＿＿＿＿')







