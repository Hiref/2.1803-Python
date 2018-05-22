
from multiprocessing import Pool
import time
import os
def Work():
	for i in range(1):
		time.sleep(0.45)
		print("FED GEFUII GREOH CN UJKCGAUSI FEGYWUFGUU GY—— GFUYSD %d | %d"%(os.getpid(),os.getppid()))


p = Pool(10)

for i in range(48):
	time.sleep(0.5)
	print("FHEIU%d"%i)
	p.apply(Work)

p.close()
p.join()


from multiprocessing import Pool
import time
import os

def Worker():
	for i in range(1):
		time.sleep(0.5)
		print("FUEIW-vsi %d -BUIVD GUDIBSL"%os.getpid())

p = Pool(1)

for i in range(1):
	time.sleep(0.5)
	print(i)
	p.apply(Worker)

p.close()
p.join()



from multiprocessing import Pool
import time
import os

def Worker():
	for i in range(3):
		time.sleep(0.5)
		print("FEGUWGF %d -v DFS FTXA CSGYUDTY CSUIG FTA"%os.getpid())
p = Pool(3)

for i in range(6):
	time.sleep(0.3)
	print(i)
	p.apply(Worker)
p.close()
p.join()








