from threading import Thread
import time
import threading
def work():
	name = threading.current_thread().name
	print(name)
	num = 1
	time.sleep(1)
	if name == "Thread-1":
		num += 1
		time.sleep(1)
		print("厉害咯%d"%num)
	else:
		time.sleep(1)
		print("呵呦，有趣　%d"%num)

Q = Thread(target = work)
Q.start()

Q1 = Thread(target = work)
Q1.start()





