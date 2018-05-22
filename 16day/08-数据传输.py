from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto('bvhjfvsaiev'.encode('gb2312'),('192.168.19.123',8080))

s.close()







