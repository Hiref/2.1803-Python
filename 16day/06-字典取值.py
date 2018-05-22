global_dict = {}

def std_thread(name):
	std = Student(name)
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()

def do_task_1():
	std = global_dict[]




