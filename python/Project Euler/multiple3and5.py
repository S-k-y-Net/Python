#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000

arrayOf3 = []
arrayOf5 = []
i = 0
j = 0
chooseValue = int(input())
chooseValue = chooseValue - 1
while chooseValue > 2:
	localVarA = chooseValue%3
	if localVarA==0:
		i = i + 1
		arrayOf3.insert(i,chooseValue)
	localVarB = chooseValue%5
	if localVarB==0:
		j = j + 1
		arrayOf5.insert(j,chooseValue)
	chooseValue = chooseValue - 1
summary = sum(arrayOf3) + sum(arrayOf5)
print(summary)