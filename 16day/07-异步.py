from multiprocessing import Pool
import time
import os

def test():
	for i in range(3):
		print("＂肚子别叫了＂".center(30,' '))
		time.sleep(0.5)
	return '饿死了'

def test2(args):
	time.sleep(0.8)
	print("时间".center(30,' '))
	time.sleep(0.8)
	print("一年一年".center(30,' '))
	time.sleep(0.8)
	print("过去了".center(30,' '))
	time.sleep(1)
	print(args)
	for i in range(5):
		time.sleep(1)
		print("....".center(30,' '))
pool = Pool(3)
pool.apply_async(func=test,callback = test2)

time.sleep(10)
for i in range(5):
	time.sleep(0.5)
	print('＂饭做好了＂'.center(30,' '))
time.sleep(0.3)
print("＿＿＿＿＿＿＿".center(30,' '))









