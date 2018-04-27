import os
file_name = input("请输入要修改的文件夹")
old_f = os.listdir("file_name")
for emmp in file_name:
	position = file_name.rfind(".")
	file_name[0:position]
	file_name[position:]
	new_file = open(file_name+"寒月瑞"+'1.txt',"w")
	new_file.write(content)

	old_f.close()
	new_file.close()












