import os
import sys
import random
import string
file = 'sowpods.txt'

with open(file, 'r') as _f:
	content = []
	for line in _f:
		content.append(line.replace('\n',''))
	picks = content[round(random.random()*int(len(content)))] 
	print(picks)