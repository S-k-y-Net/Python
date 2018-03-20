#Python List [71 exercises with solution]

#1  Write a Python program to sum all the items in a list
def sum_of_item_list(int_list):
	if len([s for s in int_list if isinstance(s, int)]) == len(int_list):
		return sum(int_list)
	else:
		return "List have not integer item or items"
#print(sum_of_item_list(["1","2","3","4"]))

#2. Write a Python program to multiplies all the items in a list.
def multiple_all_items_int_list(_list):
	return [s*2 for s in _list]
#print(multiple_all_items_int_list(["1","2","3","4"]))

#3. Write a Python program to get the largest number from a list
def return_the_lager_numb(int_list):
	if len([s for s in int_list if isinstance(s, int)]) == len(int_list):
		return max(int_list)
	else:
		return "List have not integer item or items"
#print(return_the_lager_numb([1,2,3,4]))

#4. Write a Python program to get the smallest number from a lis
def return_the_smaller_numb(int_list):
	if len([s for s in int_list if isinstance(s, int)]) == len(int_list):
		return min(int_list)
	else:
		return "List have not integer item or items"
#print(return_the_smaller_numb([1,2,3,4]))

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
def count_strings_if_first_and_last_same(_list):
	count = 0
	for i in _list:
		if i[:1] == i[-1:] and len(i) > 2:
			count += 1
	return count
#print(count_strings_if_first_and_last_same(["fas","wqtw","234","12314"]))

#6 Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def sort_list_by_second_tuple_item(_list): #from w3resousre solution
	def last(n): return n[-1]
	return sorted(_list, key = last)
#print(sort_list_by_second_tuple_item([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7 Write a Python program to remove duplicates from a list
def remove_duplicates(_list):
	for i in _list:
		if _list.count(i) >= 2:
			_list.remove(i)
	return _list
#print(remove_duplicates([1,2,4,3,4,4]))

#8. Write a Python program to check a list is empty or not
def check_if_list_empty(_list):
	if _list == []:
		return True
	else:
		return False
#print(check_if_list_empty([]))

#9. Write a Python program to clone or copy a list
def copy_list(_list):
	return _list
#print(copy_list([1,2,4,3,4,4]))

#10. Write a Python program to find the list of words that are longer than n from a given list of words
def find_long_words_in_list(_list, n):
	new_list = []
	for i in _list:
		if len(i) > n:
			new_list.append(i)
	return new_list
#print(find_long_words_in_list(["agsd","tqwe","qq","1","ggggggggg"], 2))


