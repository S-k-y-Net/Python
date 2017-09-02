import datetime

i = 0

name = input("Give me your name: ")
age = input("Give me your age: ")
copies = input("How many I should print it? : ")
now = datetime.datetime.now().year + 100 - int(age)

while i < int(copies):
	print("You name is " + name + " your age is " + age + " you will 100 in " + str(now))
	i += 1
