from threading import Thread
import time

def sing():
	for i in range(1):
		print("正在唱歌")

def dance():
	for i in range(1):
		print("正在跳舞")



for i in range(500):
	t1 = Thread(target = sing)
	t2 = Thread(target = dance)

	t1.start()
	t2.start()


























