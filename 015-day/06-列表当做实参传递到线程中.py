from threading import Thread
import time
import threading


g_num = 0

def work():
	global g_num
	for i in range(1000000):
		g_num +=1

	print("---in work , g_num is%s %d"%(threading.current_thread().name,g_num))

def work2():
	global g_num
	for i in range(1000000):
		g_num += 1
	print("---in work2 , g_num is %d ---"%g_num)

print("---线上创建之前ｇ＿num is %d---"%g_num)


t1 = Thread(target = work)
t1.start()
t1.join()
#time.sleep(2)

t2 = Thread(target = work2)
t2.start()
