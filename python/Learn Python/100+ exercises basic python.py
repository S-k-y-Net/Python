from __future__ import print_function
import glob
from stat import S_ISREG, ST_CTIME, ST_MODE
import cProfile
import socket
import ipaddress
import multiprocessing
import site
import struct
import os
import sys
import datetime
import calendar
import math
import platform
import subprocess
import getpass
import time
from ctypes import windll, create_string_buffer


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

#31
def evklid_algorithm(a,b):
	while True:
		if a > b:
			if 0 == a%b:
				return b
			else:
				a = a%b
		else:
			if 0 == b%a:
				return a
			else:
				b = b%a
#print(evklid_algorithm(320,115))

#32
def lcm(a,b):
	return 	abs(a*b)/evklid_algorithm(a,b)
#print(lcm(30,18))

#33
def sum_of_three_special(a,b,c):
	return 0 if c == a or b == c or b == a else a + b + c
#print(sum_of_three_special(5,5,3))

#34
def sum_of_two_special(a,b):
	return 20 if 15 <= a + b <= 20 else a + b
#print(sum_of_two_special(9,9)) 

#35
def eq_sum_diff_for_five(a,b):
	return True if a + b == 5 or abs(a - b) == 5 or a == 5 or b == 5 else False 
#print(eq_sum_diff_for_five(-1,6))

#36
def if_int_check(a,b):
	return a + b  if isinstance(a,int) and isinstance(b, int) else print("ERROR")
#print(if_int_check(5,'a'))

#37
def person_details(age,name,address):
	return age + '\n' + name + '\n' + address
#print(person_details('43','adsd','rereremott 123')) 

#38
def simple_solution_of_formula(x,y):
	return (x + y)**2
#print(simple_solution_of_formula(4,3))

#39
def future_value(amount, rate_of_return, number_of_period):
	return amount*(1 + 0.01*rate_of_return)**number_of_period
#print(future_value(20000,3.5,7))

#40
def distance_between_two_points(a,b):
	return math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)
#print(distance_between_two_points((5,2),(3,20)))

#41.1
def if_file_exist(_filepath):
	try:
		open(_filepath)
	except Exception as e:
		print(e)
	else:
		print('file open successfully')

#if_file_exist('file.txt')

#41.2
def if_file_exist2(_filepath):
	return os.path.isfile(_filepath)	
#print(if_file_exist2('te.xtx'))

#42.1
def os_architecture():
	return platform.platform()
#print(os_architecture())	
#42.2
def os_architecture2():
	return struct.calcsize("P") # 'P' - pointer
#print(os_architecture2())

#43
def os_info():
	return platform.platform() + ' ' +platform.system() +' '+ platform.version() + ' ' + platform.release()
#print(os_info())

#44
def site_packages():
	return site.getsitepackages()
#print(site_packages())

#45
def call_enemy_function(command):
	return subprocess.call([*command])
#print(call_enemy_function(['ipconfig']))

#46
def get_current_file_path_name():
	return "Current file name : " + os.path.realpath(__file__)
#print(get_current_file_path_name())

#47
def number_of_CPU():
	return multiprocessing.cpu_count()
#print(number_of_CPU())

#48
def parse_string_to_int(n):
	return int(n)
#print(parse_string_to_int('5'))

#49
def all_files_in_directory():
	onlyfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
	return onlyfiles
#print(all_files_in_directory())

#50
def cut_spaces(string):
	return string.replace(" ", "").replace("\n", "")
#print(cut_spaces("teg sd asdg fdas \n"))

#51
def determine_profiles(profile):
	return cProfile.run("'"+profile+"'")
#determine_profiles('all_files_in_directory()')

#52
def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)
#eprint('abc','rga','sfsf', sep= " -- ")

#53
def environment_vars(var = None):
	return os.environ[var] if var != None else os.environ
#print(environment_vars('SYSTEMROOT'))

#54
def get_username():
	return getpass.getuser()
#print(get_username())

#55
def get_ipaddress():
	return socket.gethostbyname(socket.gethostname())
#print(get_ipaddress())

#56
#not working in windows((

#57
def function_time():
	start_time = time.time()
	for i in range(1000000):
		i +=1
	end_time = time.time()
	return end_time - start_time
#print(function_time())

#58
def sum_first_n_positive(n):
	return n*(n + 1)/2
#print(sum_first_n_positive(10))

#59
def feet_and_inches_to_centm(n):
	return str(n) + " inches = " + str(n * 2.54) + " centimeters and " + str(n) + " feet = " + str(n * 30.48) + " centimetres"
#print(feet_and_inches_to_centm(5))

#60
def hypotenuse_of_triangle(a,b):
	return math.sqrt(a**2 + b**2)
#print(hypotenuse_of_triangle(3,4))

#61
def convert_distance(n):
	return str(n) + " feets: " + str(n * 12) + " inches, " + str(n * 0.3333) + " yards, " + str(n * 0.000189394) + " miles."
#print(convert_distance(100)) 

#62
def convert_to_seconds(h = 0, m = 0, s = 0):
	return h*60*60 + m * 60 + s
#print(convert_to_seconds(0,3,1))

#63
def get_absolute_file_path(_file):
	return os.path.abspath(_file)
#print(get_absolute_file_path('AssemblyList_4_client.xml'))

#64
def get_file_info(_file):
	return time.ctime(os.path.getmtime(_file)) + ' ' + time.ctime(os.path.getctime(_file))
#print(get_file_info('birthday.json'))

#65
def convert_seconds_to_utc(seconds):
	days = seconds // (3600*24)
	seconds = seconds%(3600*24)
	hour = seconds // 3600
	seconds %= 3600
	minute = seconds // 60
	seconds %= 60
	return str(days) + "d : " + str(hour) + "h : " + str(minute) + "m : " + str(seconds) + "s"
#print(convert_seconds_to_utc(10000000))

#66
def body_mass_index(weight, height):
	return round(weight/(height/100*height/100),2)
#print(body_mass_index(100,180))

#67
def convert_from_kilopascal(n):
	return str(n * 0.145038) + " pounds per square " + str(n * 7.50062) + " millimeter of mercury " + str(n * 0.00986923) + " atmosphere pressure"
#print(convert_from_kilopascal(100))

#68
def sum_of_digits(n):
	return sum(int(i) for i in list(str(n)))
#print(sum_of_digits(1123))

#70
def glob_module_sort_files_by_date(_files):
	_file = glob.glob(_files)
	_file.sort(key=os.path.getmtime)
	return ("\n").join(_file)
#print(glob_module_sort_files_by_date("*.py"))

#71
def list_of_directories_sort_by_date():
	dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

	#all entries in the directory w/ stats
	data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
	data = ((os.stat(path), path) for path in data)

	# regular files, insert creation date
	data = ((stat[ST_CTIME], path)
	           for stat, path in data if S_ISREG(stat[ST_MODE]))

	for cdate, path in sorted(data):
	    print(time.ctime(cdate), os.path.basename(path))

#list_of_directories_sort_by_date()

#72
def info_math_module(name):
	return dir(name)
#print(info_math_module(math.asin))

#73
def midpoint_of_line(x, y):
	return (x + y)/2
#print(midpoint_of_line(6,3))

#75
def copyright_info():
	return sys.copyright
#print(copyright_info())

#76
def sys_argv_info():
	return str(sys.argv[0]) + " " + str(sys.argv) + "  " + str(len(sys.argv))
#print (sys_argv_info())

#77
def info_endian_point():
	return sys.byteorder
#print(info_endian_point())

#78
def return_builtin_modules():
	return ("\n").join(sorted(sys.builtin_module_names))
#print(return_builtin_modules())

#79 
def return_size_of_obj(obj):
	return sys.getsizeof(obj)
#print(return_size_of_obj("1234"))

#80
def recursion_limit():
	return sys.getrecursionlimit()
#print(recursion_limit())

#81
def conatinate_strings(*args):
	return "".join(args)
#print(conatinate_strings("gaga","adada", "adaew", "dawes"))

#82
def return_sum(*args):
	return [sum(x) for x in args] 
#print(return_sum([10,20,30],[10,20,15],[11,2,3,5,123,51,23]))

#83
def check_certain_number_of_list(_list):
	return True if len([x for x in _list if x <= _list[round(len(_list)/2)] ]) == len(_list) else False
print(check_certain_number_of_list([10,4,1,3,100,23,52,31,3]))
