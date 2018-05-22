from threading import Thread
import time
def work():
	time.sleep(1)
	print("1 2 3 ")

for i in range(5):
	t = Thread(target = work)
	t.start()




























