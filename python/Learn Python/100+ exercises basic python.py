import os
import sys
import datetime

def GetPythonVersion():
	version = os.system("Python -V")
	sys_version = sys.version 
	sys_verions_info = sys.version_info
	return sys_version, sys_verions_info
#print(GetPythonVersion())

def CurrentDataAndTime():
	curent_date = datetime.datetime.now()
	return curent_date
#print(CurrentDataAndTime())

def AreaByRadius(radius):
	return radius * 3.14 * 2 
#print(AreaByRadius(5))

def FirstlastName():
	user_input_surname = input("Print you first name: ")
	user_input_name = input("Print you last name: ")
	print(user_input_name[::-1])
	print(user_input_surname[::-1])
#FirstlastName()

def ListAndTuple():
	_input = input("Input some more number with delimeter ',': ")
	input_list = _input.split(',')
	input_tuple = tuple(input_list)
	return input_list, input_tuple
#print(ListAndTuple())
def ExtentionOfFile():
	user_input = input("input filname with extention: ")
	try:
		user_input = user_input.split(".")
		print(user_input[:0:-1])
	except sys.stderr:
		print(sys.stderr)
ExtentionOfFile()
