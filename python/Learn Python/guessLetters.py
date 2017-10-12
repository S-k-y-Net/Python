import os
import sys
import random
import string
file = 'sowpods.txt'

def pick_word():
	with open(file, 'r') as _f:
		content = []
		for line in _f:
			content.append(line.replace('\n',''))
		picks = content[round(random.random()*int(len(content)))] 
		return picks

def guess_word():
	c = pick_word() 
	#print(c)
	user_input = input("Guess a word=) : ")
	_str = list("_"*len(c))
	while True:
		if user_input.upper() in c:
			for i, alf in enumerate(c):
				if alf == user_input.upper():
					_str[i] = alf
			print(" ".join(_str))
			if _str == list(c):
				break
			user_input = input("... : ")
		else:
			user_input = input("Incorrect ^^ : ")
	return " ".join(_str)
if __name__ == '__main__':
	# print(user_input.upper())
	# print(list(c))
	c = guess_word() 
	print("Yes is " + str(c))