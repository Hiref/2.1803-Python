import os
i = input("请输入文件名字")
s = os.listdir(i)

for a in s:
	s = i + "/" + a
	d = i + "/" + "寒日" + a
	os.rename(s,d)









