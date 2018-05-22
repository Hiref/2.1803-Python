from multiprocessing import Process
import os


def Test(name): 
	for i in range(3):
		print("子进程【1】运行中 NAME = %s, PID = %d"%(name,os.getpid()))

def Test2(name): 
	for i in range(3):
		print("子进程【2】运行中 NAME = %s, PID = %d"%(name,os.getpid()))

print("————————————————————————————————————————")
print("FU进程为%d."%os.getpid())
p = Process(target = Test, args=("关羽",))

print("————————————————————————————————————————")
print("ZI TUNING")
p.start()
p.join()
print("————————————————————————————————————————")
print("运行结束")

p2 = Process(target = Test2, args=("李白",))








