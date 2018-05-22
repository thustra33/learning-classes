from time import sleep

class User:
	def __init__(self, name, age, height, weight):
		self.name = name 
		self.age = age
		self.height = height
		self.weight = weight
	def introduce_self(self):
		print("Hi, my name is " + self.name)
		print("I am", self.age, "years old")
		print("I am", self.height, "feet tall, and weigh", self.weight, "pounds")


u1 = User("Bob", 25, 6, 175)
u2 = User("Billy", 43, 5.6, 143)
u3 = User("Jean", 32, 5.3, 131)
u4 = User("Katie", 28, 5.8, 146)

u1.introduce_self()
sleep(2)
u2.introduce_self()
sleep(2)
u3.introduce_self()
sleep(2)
u4.introduce_self()
