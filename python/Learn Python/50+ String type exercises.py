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
	if _str[len(_str) - 3::] == 'ing' and len(_str) >= 3:
		_str = _str + 'ly'
	elif len(_str) >= 3:
		_str = _str + 'ing'
	else:
		return _str
	return _str
#print(add_ing_and_ly_to_str('gn'))

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def replace_string(_str):
	if 'not' in _str:
		if 'poor' in _str:
			index = _str.find('poor')
			_new_str = _str[index:]
			if 'bad' in _new_str:
				index2 = _str.find('not')
				return _str[:index2:] + "good!"
			else:
				return _str
	return _str
#print(replace_string('The lyrics is not that poor bad!'))

#8. Write a Python function that takes a list of words and returns the length of the longest one.
def longest_word(_list):
	max_len = 0
	for i in _list:
		if len(i) > max_len:
			max_len = len(i)
	return max_len
#Sprint(longest_word(['gasd', 'asgasdgasdgasdgqwew','gaa', 'qwerqs']))

#9. Write a Python program to remove the nth index character from a nonempty string.
def remove_characters(_str, n):
	return _str[n:]
#print(remove_characters('123456789ffffffff',6))

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def change_string(_str):
	return '$' + _str[1:len(_str) - 1:] + '$'
#print(change_string('calabok'))

#11. Write a Python program to remove the characters which have odd index values of a given string
def without_odd_index(_str):
	return _str[1::2]
#print(without_odd_index('1234567890'))

#12. Write a Python program to count the occurrences of each word in a given sentence
def count_words(_sentense):
	_dict = {}
	_list_words = _sentense.split(' ')
	for i in _list_words:
		if i in _dict.keys():
			_dict[i] += 1
		else:
			_dict[i] = 1
	return _dict
#print(count_words('Write a Python script that takes input from the user and displays that input back in upper and lower cases'))

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases
def upper_and_lower():
	print('Print string: ')
	_str = raw_input()
	return "Upper: " + _str.upper() + "\n Lower: " + _str.lower()

#print(upper_and_lower())




