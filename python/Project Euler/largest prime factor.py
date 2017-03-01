#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
PrimeFactor = []
i = 2
j = 0
getVariable = int(input())
variableLegacy = getVariable
sqrOfVariable = math.floor(math.sqrt(getVariable))
print(sqrOfVariable)
while i < sqrOfVariable :
	boolean = getVariable%i
	if (boolean==0):
		candidate = getVariable / i
		getVariable = candidate
		PrimeFactor.insert(j, i)
		j += 1
		print(candidate)
	else:
		i += 1 
print("There is Prime factors of " + str(variableLegacy) + ": " +str(PrimeFactor))
maxOfPrimeFactors = max(PrimeFactor)
print("Largest prime factor of number " + str(variableLegacy) + " is: " + str(maxOfPrimeFactors))
