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

def hangman():
	c = pick_word() 
	tryes = 0
	i = 0
	user_input_incorrect = []
	#print(c)
	user_input = input("Guess a word=) : ")
	_str = list("_"*len(c))
	while True:
		tryes += 1
		if user_input.upper() in c and not user_input.upper() in _str:
			tryes = 0
			for i, alf in enumerate(c):
				if alf == user_input.upper():
					_str[i] = alf
			print(" ".join(_str))
			if _str == list(c):
				print("Yes is " + " ".join(_str))
				break
			user_input = input("... : ")
		else:
			if tryes == 6:
				print("You lose! T_T")
				break
			user_input_incorrect.append(user_input)
			i += 1
			user_input = input("Incorrect ^^ You have only " + str(6 - tryes) + " tryes \n")
			if user_input in user_input_incorrect:
				tryes -= 1

	print("Do you want try again? (Y,N) ")
	user_answer = input()
	if user_answer.upper() == "Y":
		hangman()
	else:
		print("GoodBay")
	return " ".join(_str)



if __name__ == '__main__':
	# print(user_input.upper())
	# print(list(c))
	c = hangman() 
	
