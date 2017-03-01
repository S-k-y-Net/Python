#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
class Fibonacci(int):
	"""docstring for Fibonacci"""
	def listFibonacci(self,arg):
		arrayFibonacci = []
		standartArray = []
		for i in range(1,arg):
			standartArray.insert(i,i)
		for j in standartArray:
			if j > 2:
				fibonacciVar = arrayFibonacci[j-2] + arrayFibonacci[j-3]
			else:
				fibonacciVar = j	
			arrayFibonacci.insert(j,fibonacciVar)
		return arrayFibonacci	
value = int(input())
a = Fibonacci().listFibonacci(value)
print (a)
class evenNumbers(int):
	"""docstring for evenNumber"""
	def FindevenValues(self,array):
		evenList = []
		j = 0
		for i in array:
			cBool = i%2
			if cBool==0:
				evenList.insert(j, i)
				j += 1
		return evenList
	def sumOfList(self,array):
		self = sum(array)
		return self			

b = evenNumbers().FindevenValues(a)
print (b)

c = evenNumbers().sumOfList(b)
print(c)