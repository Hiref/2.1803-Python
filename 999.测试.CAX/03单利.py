class Animal(object):

	def move(self):
		print("走")

class Dog(Animal):

	def move(self):
		print("狗用四条腿")

class Person(Animal):

	def move(self):
		print("人用两条腿")

def w(o):
	o.move()

dog = Dog()

#dog.move()
w(dog)


person = Person()

#person.move()
w(person)


