file_name = input("请输入文件名and后缀")
old_file = open(file_name,"r")
conrent = old_file.read()

postion = file_name.rfind(".")
file_name[0:postion]
file_name[postion]

new_file = open(file_name+"复制"+"1.txt","w")
new_file.write(content)

old_

