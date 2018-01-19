import os

#1. Write a Python program to calculate the length of a string
def string_length(_str):
	count = 0
	for i in _str:
		count += 1
	return count

#2. Write a Python program to count the number of characters (character frequency) in a string. 

def characters_frequency(_str):
	_dict = {} 
	for i in _str:
		if i in _dict:
			_dict[i] += 1
		else:
			_dict[i] = 1
	return _dict
#print(characters_frequency("sgas.gh.asdr"))

