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


#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
def two_last_adn_two_first_chars_of_string(_str):
	if len(_str) >= 2:
		return _str[:2:] + _str[len(_str) -2::] 
	else:
		return "Empty string"
#print(two_last_adn_two_first_chars_of_string("f"))

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
def change_all_occurrances(_str):
	_str_list = list(_str)
	for i, item in enumerate(_str_list):
		if item in _str_list[:i:]:
			_str_list[i] = '$'
	return ''.join(_str_list)
#print(change_all_occurrances('gasgtg'))


#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
def swap_two_first_characters(_str):
	string_words = _str.split(' ')
	return str(string_words[0][:2:] + string_words[1][2::]), str(string_words[1][:2:] + string_words[0][2::])  
#print(swap_two_first_characters('gast tera'))

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_ing_and_ly_to_str(_str):
	if _str[len(_str) - 3::] == 'ing' and len(_str) > 3:
		_str = _str + 'ing'
	elif len(_str) > 3:
		_str = _str + 'ly'
	else:
		return _str
	return _str
#print(add_ing_and_ly_to_str('gng'))

