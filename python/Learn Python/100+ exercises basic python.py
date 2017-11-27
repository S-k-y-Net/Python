from __future__ import print_function
from hurry.filesize import size
from inspect import getmodule
import itertools
import urllib
import bs4
import json
import random
import numpy as np
import collections
import glob
import traceback
from stat import S_ISREG, ST_CTIME, ST_MODE
import http.client
import cProfile
import socket
import ipaddress
import multiprocessing
import site
import struct
import re
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
#print(check_certain_number_of_list([10,4,1,3,100,23,52,31,3]))

#84
def check_occurence_of_char(n,string):
	return string.count(n)
#print(check_occurence_of_char("q", "qqqqq"))

#85
def check_is_file_or_directory(_path):
	if os.path.isdir(_path):
		return "is dir"
	elif os.path.isfile(_path):
		return "is file"
	else:
		return " not exits"
#print(check_is_file_or_directory("birthday.json"))

#86
def get_ascii_code(n):
	return ord(n)
#print(get_ascii_code("n"))

#87
def get_size_of_file(_file):
	return size(os.path.getsize(_file))
#print(get_size_of_file("birthday.json"))

#88
def print_some_bullshit(x,y):
	return "\n%d + %d = %d"%(x,y,x+y)
#print(print_some_bullshit(1,3))

#89
def second_bullshit(n):
	return "Is the first dat of Month" if n ==1 else " "
#print(second_bullshit(2))

#90
#print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())

#91
def swap_two_var(a,b):
	a, b = b, a
	return a, b
#print(swap_two_var(3,10))

#93
def return_id_of_obj(obj):
	return id(obj)
#print(return_id_of_obj(object()))

#94
x = b'Abc'
#print(list(x))

#95
def check_if_string_is_numeric(string):
	try:
		int(string)
	except (ValueError, TypeError):
		print("Not numeric")
	else:
	 return True
#print(check_if_string_is_numeric("12a"))	

#96
def print_traceback():
	check_if_string_is_numeric("111")
	traceback.print_stack()
#print(print_traceback())

#97
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
#print(s_var_names)

#98 
def system_time():
	print(time.ctime())
	return datetime.datetime.now()
#print(system_time())

#99
def clear_screen():
	return os.system('cls')

#100
def get_host_name():
	return socket.gethostname()
#print(get_host_name())

#101
def get_html_content(url):
	conn = http.client.HTTPConnection(url)
	conn.request("GET","/")
	result = conn.getresponse()
	return result.read()
#print(get_html_content("akaptur.com"))

#102
def get_cmd_output():
	subprocess.check_output("dir", shell=True, universal_newlines=True)

#print(get_cmd_output())

#103
def extract_filename_from_path(_path):
	return _path[_path.rfind("\\") + 1::]
#print(extract_filename_from_path("C:\\scripts\\aaa.xts"))

#104
#Only for Unix

#105
#print(os.environ)

#106
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
	pass
	#print('"%s" :' % path, os.path.splitext(path))

#107
def some_kids_use():
	for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
		print('File        :', file)
		print('Absolute    :', os.path.isabs(file))
		print('Is File?    :', os.path.isfile(file))
		print('Is Dir?     :', os.path.isdir(file))
		print('Is Link?    :', os.path.islink(file))
		print('Exists?     :', os.path.exists(file))
		print('Link Exists?:', os.path.lexists(file))
#some_kids_use()	    
#108
def second_kids_use():
	print('File         :', __file__)
	print('Access time  :', time.ctime(os.path.getatime(__file__)))
	print('Modified time:', time.ctime(os.path.getmtime(__file__)))
	print('Change time  :', time.ctime(os.path.getctime(__file__)))
	print('Size         :', os.path.getsize(__file__))

#second_kids_use()

#109
def check_is_number_positive_negative_zero(n):
	if n > 0:
		return "Positive"
	elif n == 0:
		return "Zero"
	else:
		return "Negative"
#print(check_is_number_positive_negative_zero(2))

#110
def use_anonymous_function(_list):
	selection = list(filter(lambda s: (s%15==0), _list))
	return selection
#print(use_anonymous_function([15,30,45,2,3]))

#111
def wildcard_list_of_files(pattern):
	return glob.glob(pattern)
#print(wildcard_list_of_files("*.*"))

#112
def remove_first_item_from_list(_list):
	del _list[0]
	return _list
#print(remove_first_item_from_list([1.23,415,12,3,42,3,512,3]))

#113
def check_if_it_number(n):
	try:
		int(n)
	except (TypeError, ValueError) as e:
		print(e)
#print(check_if_it_number("ga3"))

#114
def filter_positive_numbers(_list):
	return [x for x in _list if x >= 0]
#print(filter_positive_numbers([1,-3,4,6,10,23,-77,0,234,1000,-1000]))

#115
def compute_two_list(_listone,_listtwo):
	a = np.array(_listone)
	b = np.array(_listtwo)
	return a * b
#print(compute_two_list([1,2,3],[4,3,2]))

#116
def unicode_character(char):
	return char.encode('utf-8')
#print(unicode_character('gasdaакфыв'))

#117
def prove_string_in_same_memory_location(str1,str2):
	return hex(id(str1)), hex(id(str2))
#print(prove_string_in_same_memory_location("gar","gar")) 

#118
def byte_array_from_list(_list):
	return [bytearray(x,'utf-8') for x in _list]
#print(byte_array_from_list(["пфв","ter","wrq"]))


#119
#print("The float with spec number %.2f" % 1.34232) 

#120
def string_limit_by_six(string):
	for i in range(6,len(string),7):
		string = string[:i] + ' ' + string[i:]
	return string

#print(string_limit_by_six("123456789012345678901234567890"))


#121
# try:
# 	y
# except NameError:
# 	print("Variable not defined")

#122
def empty_variable_without_destryoed(n):
	return type(n)()
#print(empty_variable_without_destryoed([1,3,42,5]))

#123
def min_max_number(_list):
	print(sys.maxsize)
	return "min = " + str(min(_list)) + " max = " + str(max(_list))
#print(min_max_number([1.3,6.2,9]))

#124
def multiple_var_have_the_same_value(n1, n2):
	return set(list(str(n1)))&set(list(str(n2)))
#print(multiple_var_have_the_same_value("1423","1523"))

#125
def sum_of_collections(collection):
	return sum(collections.Counter(collection).values())
#print(sum_of_collections([2,2,4,6,6,8,6,10,4]))

#126
def get_module(module):
	return getmodule(module)
#print(get_module(sys))

#127
def get_bit_lengh():
	return (-2**63).bit_length(), (2**63).bit_length() 
#print(get_bit_lengh())

#128
def check_if_lowercase_in_string(string):
	return "Have lowercase" if string.upper() != string else "All letters upper"
		
#print(check_if_lowercase_in_string("GASDFSFG"))

#129
def add_zeroes_to_string(string):
	return string.ljust(10, "0")
#print(add_zeroes_to_string("gasds"))

#130.1
def double_quotes_to_display_string(string):
	return '\"' + string + '\"'
#print(double_quotes_to_display_string("tasdaf"))

#130.2
def double_quotes_to_display_string_2(string):
	return json.dumps(string)
#print(double_quotes_to_display_string_2({'cafe': 2, 'tera': 1}))  good function

#131
# var_list = ['a', 'b', 'c']
# x, y, z = (var_list)
# print(x, y, z)

#132
#print(os.path.expanduser('~'))

#133
#repeat 57

#134
# x, y = map(int, input().split())

# print(x**y,y**x)

#135
# x = 30
# print('Value of this is "{}"'.format(x))

#136
def find_files_without_directories(path):
	return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#print(find_files_without_directories("c:/scripts/"))

#137
def extract_single_key_value_from_dict(_dict):
	(x,y), =_dict.items()
	return x,y
#print(extract_single_key_value_from_dict({"key":23}))

#138
def convert_true_and_false(sequence):
	return 1 if sequence == True else 0
#print(convert_true_and_false(False))

#139
def check_ip_address(ip_address):
	return True if re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip_address) else "Incorrect IP address"
#print(check_ip_address("123.167.215.123"))

#139.2
def check_ip_address2(ip_address):
	return True if socket.inet_aton(ip_address) else "Incorrect ip address"
#print(check_ip_address2("5123.512.32.5"))

#140
def convert_decimal_to_binary(numb):
	return format(numb, "08b")
#print(convert_decimal_to_binary(1))

#141
def decimal_to_hex(numb):
	return hex(numb)
#print(decimal_to_hex(16))

#142
def system_os_info():
	return "operation system name \n" + os.name + "\n" + "Platform name \n" + platform.system() + "\n" + "Platform release \n" + platform.release()
#print(system_os_info())

#143
#repeat 42

#144
def check_variable(var):
	if isinstance(var, int):
		return "Integer"
	elif isinstance(var, str):
		return "String"
	else:
		"Cannot check type"
#print(check_variable("1"))
#145,146 repeat 142

#147
def if_multiply():
	n, m = map(int, input("Enter n, m: ").split(","))
	return True if n%m == 0 else False
#print(if_multiply())

#148
def custom_max_min(sequence):
	#buble sort
	for i in range(len(sequence) - 1):
		for j in range(len(sequence) - 1):
			if sequence[j] > sequence[i]:
				n = sequence[j]
				sequence[j] = sequence[i]
				sequence[i] = n
	return sequence[0], sequence[len(sequence) - 1]
#print(custom_max_min([5,4,2,8,11,23]))

#149
def sum_of_cube_positive_int_below(n):
	sum_of_all = 0
	for i in range(n, 1, -1):
		sum_of_all += i**3
	return sum_of_all
#print(sum_of_cube_positive_int_below(10))

#150
def distinct_pair_of_number_product_odd(sequence):
	t = set(sequence)
	_list = []
	for i, num in enumerate(t):
		for j, b in enumerate(t):
			if b * num & 1 and b != num:
				_list.append(b)
	return set(_list)
#print(distinct_pair_of_number_product_odd([25,23,1,2,3,6,23,10,7,47,102]))

#151
def determine_if_all_numbers_is_different(sequence):
	return True if len(set(sequence)) == len(sequence) else False
#print(determine_if_all_numbers_is_different([1,23,5,6,2,3,7,3,0]))    	

#152
def possible_strings_with_characters(*args):
	_list = list(args)
	random.shuffle(_list)
	#return list(map(''.join, itertools.product(_list, repeat = 3) ))
	return "".join(_list)
#print(possible_strings_with_characters('a', 'e', 'i', 'o', 'u'))

#153
def print_only_third_nembers(_list):
	if len(_list) <= 3:
		print(_list)
		return _list
	_r_list = [x for x in range(len(_list)) if (x + 1)%3 == 0 and len(_list) > 3]
	#print(_r_list)
	print([_list[l] for l in _r_list])
	#print(_list)
	print_only_third_nembers([_list[item] for item in range(len(_list)) if item not in _r_list])
#print_only_third_nembers([10,20,30,40,50,60,70,80,90])

#154
def sum_of_three_number_is_zero(_array):
	_list = []
	for x in _array:
		for y in _array:
			for z in _array:
				if x + y + z == 0 and x != y != z and (x not in _list or y not in _list or z not in _list):
					_list.append([x,y,z])
	return _list
#print(sum_of_three_number_is_zero([1,6,-6,10,22,-9,-1,-5]))

#155
def three_digit_combo():
	numbers = []
	for num in range(1000):
		num=str(num).zfill(3)
		print(num)
	numbers.append(num)
#three_digit_combo()

#156
def long_text_string_convert_and_frequency(): #copypaste
	string = '''United States Declaration of Independence
	From Wikipedia, the free encyclopedia
	The United States Declaration of Independence is the statement
	adopted by the Second Continental Congress meeting at the Pennsylvania State
	House (Independence Hall) in Philadelphia on July 4, 1776, which announced
	that the thirteen American colonies, then at war with the Kingdom of Great
	Britain, regarded themselves as thirteen independent sovereign states, no longer
	under British rule. These states would found a new nation – the United States of
	America. John Adams was a leader in pushing for independence, which was passed
	on July 2 with no opposing vote cast. A committee of five had already drafted the
	formal declaration, to be ready when Congress voted on independence.

	John Adams persuaded the committee to select Thomas Jefferson to compose the original
	draft of the document, which Congress would edit to produce the final version.
	The Declaration was ultimately a formal explanation of why Congress had voted on July
	2 to declare independence from Great Britain, more than a year after the outbreak of
	the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
	Second Day of July 1776, will be the most memorable Epocha, in the History of America."
	But Independence Day is actually celebrated on July 4, the date that the Declaration of
	Independence was approved.

	After ratifying the text on July 4, Congress issued the Declaration of Independence in
	several forms. It was initially published as the printed Dunlap broadside that was widely
	distributed and read to the public. The source copy used for this printing has been lost,
	and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
	with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
	by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
	is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
	popularly regarded as the official document. This engrossed copy was ordered by Congress on
	July 19 and signed primarily on August 2.

	The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
	The Declaration justified the independence of the United States by listing colonial grievances against
	King George III, and by asserting certain natural and legal rights, including a right of revolution.
	Having served its original purpose in announcing independence, references to the text of the
	Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
	(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
	on human rights, particularly its second sentence:

	We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
	Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

	This has been called "one of the best-known sentences in the English language", containing "the most potent
	and consequential words in American history". The passage came to represent a moral standard to which
	the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
	Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
	through which the United States Constitution should be interpreted.

	The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
	being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
	(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
	Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
	19th century.'''
	_list_strings = string.split(' ')
	words_list = [_list_strings.count(n) for n in _list_strings]
	return list(zip(_list_strings, words_list))
#print(long_text_string_convert_and_frequency())

#157
def number_of_characters(_file):
	with open(_file) as f:
		text = f.read()
		text_split = text.split()
		convert_to_text = "".join(text_split)
		return len(convert_to_text)
#print(number_of_characters("C:\\Max\\nameslist.txt"))

#158
def gooole_news_rss_titles():
	url = "http://news.google.com/rss"
	_title_list = []
	Client=urllib.request.urlopen(url)
	xml_page=Client.read()
	Client.close()
	
	xml_content_from_site = bs4.BeautifulSoup(xml_page, "xml")
	for titles in xml_content_from_site.findAll('item'):
		_title_list.append([titles.title.text + "  " + titles.link.text + "  " + titles.pubDate.text])
	return _title_list
print(gooole_news_rss_titles())


























