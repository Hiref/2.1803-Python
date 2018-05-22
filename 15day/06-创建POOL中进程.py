from multiprocessing import Pool
import time
import os
def work():
	for i in range(3):
		time.sleep(1)
		print("FEDUJKCGAUSI —— GFUYSD %d"%os.getpid())


p = Pool(3)

for i in range(6):
	p.apply_async(work)

p.close()
p.join()









