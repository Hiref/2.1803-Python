import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
	std = local_school.student
	print("Hello,%s (Then in %s . withing)"
           %(std,threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread,args = ('月寒',), name = 'BeiJing')
t2 = threading.Thread(target = process_thread,args = ('清落',),name = 'NanChang')

t1.start()
t2.start()
t1.join()
t2.join()





























