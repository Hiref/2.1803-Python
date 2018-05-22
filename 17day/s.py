from socket import *
from threading import Thread

s = None
ip = ''
port = ''

#发信息
def send():
	while True:
		content = input("请输入内容:\n")
		s.sendto(content.encode("gb2312"),(ip,port))

#接信息
def recv():
	while True:
		msg = s.recvfrom(1024)
		print("\r收到消息: %s___%s\n请输入内容"%(msg[0].decode('gb2312'),msg[1][0],end = ""))


#初始化
def main():
	global s
	global ip
	global port
	ip = input("请输入ip地址:\n")
	port = int(input("请输入端口号:\n"))
	s = socket(AF_INET,SOCK_DGRAM)

	#绑定端口
	s.bind(('',8081))

	t = Thread(target = send)
	t1 = Thread(target = recv)

	t.start()
	t1.start()

	t.join()
	t1.join()

if __name__ == '__main__':
	main()




