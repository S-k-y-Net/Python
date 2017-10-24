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