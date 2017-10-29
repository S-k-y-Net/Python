import os
import sys
import datetime
import calendar

#2
def get_python_version():
	version = os.system("Python -V")
	sys_version = sys.version 
	sys_verions_info = sys.version_info
	return sys_version, sys_verions_info
#print(GetPythonVersion())

#3
def current_data_and_time():
	curent_date = datetime.datetime.now()
	return curent_date
#print(CurrentDataAndTime())

#4
def area_by_radius(radius):
	return radius * 3.14 * 2 
#print(AreaByRadius(5))

#5
def first_last_name():
	user_input_surname = input("Print your first name: ")
	user_input_name = input("Print your last name: ")
	print(user_input_name[::-1])
	print(user_input_surname[::-1])
#FirstlastName()

#6
def list_and_tuple():
	_input = input("Input some more number with delimeter ',': ")
	input_list = _input.split(',')
	input_tuple = tuple(input_list)
	return input_list, input_tuple
#print(ListAndTuple())

#7
def extention_of_file():
	user_input = input("input filname with extention: ")
	try:
		user_input = user_input.split(".")
		print(user_input[:len(user_input) - 2:-1])
	except sys.stderr:
		print(sys.stderr)
#ExtentionOfFile()

#8
def last_and_first_element(_list):
	if _list == [] or _list == None:
		print("Error")
	else:
		print(_list[0],_list[-1])
color_list = ["Red","Green","White" ,"Black"]
#LastAndFirstElemet(color_list)

#9
def examination_shedule(_tuple):
	print("The examination will start in " + "%i / %i / %i"%_tuple)
exam_st_date = (11, 12, 2014)
#ExaminationShedule(exam_st_date)

#10
def compute_N_NN_NNN(n):
	print(n + int('%s%s'%(n,n)) + int('%s%s%s'%(n,n,n)))
#ComputeN_NN_NNN(5)

#11
def function_info(name):
	print(name.__doc__)
#FunctionInfo(abs)

#12
def month_and_year_calendar(year, month):
	print(calendar.month(year,month))
#MonthAndYearCalendar(2007, 8)

#13
def print_something_bullshit():
	print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')
#PrintSomethingBullshit()

#14
def days_between(date_one, date_two):
	print(abs(datetime.date(date_one[0],date_one[1],date_one[2]) - datetime.date(date_two[0],date_two[1],date_two[2])))
#DaysBetween([2015,8,12],[2011,3,2])

#15
def volume_of_sphere(radius):
	return radius**3*4/3*3.14
#print(volume_of_sphere(6))

#16
def difference_between_seventeen(numb):
	return abs(numb - 17)*2 if numb > 17 else abs(numb - 17)
#print(difference_between_seventeen(1))

#17
def whether_1000_2000_100(numb):
	if abs(1000 - numb) < 100 or abs(2000 - numb) < 100:
		return True
	else:
		return False
#print(whether_1000_2000_100(1190))

#18
def sum_of_three(one,two,three):
	return 3*(one + two + three) if one == two == three else one + two + three
#print(sum_of_three(2,2,-2))

#19
def add_is_function(mystr):
	return mystr if mystr[0:2:1] == 'Is' else 'Is ' + mystr
#print(add_is_function("I Some sting"))

#20
def print_n_copies(n,string):
	return n*(string+"\n")
#print(print_n_copies(2,"t  22 ff as"))

#21
def odd_or_even():
	user_input = int(input('Enter number: '))
	return 'Even' if user_input%2 == 0 else 'Odd'
#print(odd_or_even())

#22
def count_four(_list):
	return len([x for x in _list if x == 4])
#print(count_four([4,2,3,4,5,1,4,3,4]))

#23
def first_two_characters_copies(n,_str):
	return n*_str[0:2:1] if _str.__len__() > 2 else n*_str
#print(first_two_characters_copies(3,'taae'))

#24
def vowel_or_not(_srt):
	return True if _srt in 'aeiou' else False
#print(vowel_or_not('a'))

#25
def assert_value_in_data(value,_data):
	return True if value in _data else False
#print(assert_value_in_data(5,[5,2,3,1]))

#26
def simple_histogram(_data):
	_list = []
	for i in _data:
		n = '*'*i
		_list.append(n)
	return _list
#print(*simple_histogram([2,5,1,20]), sep = '\n')

#27
def list_to_string(_list):
	return ''.join((str(x) for x in _list))
#print(list_to_string(['ga','2','23']))

#28
def even_number_until_237(_list):
	for x in _list:
		if x%2 == 0 and x <= 237: 
			print(x)
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
#even_number_until_237(numbers)

#29
def set_colors(list_one, list_two):
	return set(set(list_one)^set(list_two))
#print(set_colors(["White", "Black", "Red"],["Red", "White", "Green"]))

#30
def triangle_area(base,height):
	return 1/2*(base * height)
#print(triangle_area(1,1))