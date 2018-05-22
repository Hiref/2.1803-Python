#要创建一个生成器,有很多方法  第一种方法很简单, 只要把一个列表生成的[]改成()

L = [x*3 for x in range(5)]
print(L)

G = (x*2 for x in range(3))

#print(G)
#print(next(G))
#print(next(G))
#print(next(G))
for i in G:
	print(i)







