from multiprocessing import Process
import time
class Dog(Process):

	def __init__(self):
		Process.__init__(self)

	def run(self):
		for i in range(3):
			time.sleep(0.5)
			print("RFJJD-[关羽] STAE| 8432")



dog = Dog()
dog.start()














