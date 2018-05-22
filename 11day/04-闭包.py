def counter(a):

	def test_in(s):
		print(a+s)

	return test_in

y = counter(1)
y(5)

print("_".center(30,"_"))

def line(c,v):
	def line2(x):
		print(c*x+v)

	return line2
y = line(2,3)
z = line(4,5)
print(y(5))
print("_".center(30,"_"))
print(z(5))









