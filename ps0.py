#Author: Luke Ittycheria
#Date: 3/28/16
#Program: Problem Set 0 Functions


#Function 0
def is_even(number):

	'''Returns a value if the number is even or odd'''
	
	if number % 2 == 0:
		evenOrOdd = "Even"
	else:
		evenOrOdd = "Odd"
	
	return evenOrOdd

###########################################################################	

#Function 1
def num_digits(y):
	
	'''Calculates the amount of digits in a given number'''
    
	count = 0
	while y > 0:
		if y == 0:
			count += 1
		count += 1
		y = y/10

	return count
	
###########################################################################	

#Function 2
def sum_digits(n):

	'''Calculates the sum of the digits in a given number'''
   
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s
		
		
	
###########################################################################	

#Function 3
def sum_less_digits(num):

	'''Calculates the sum of all the numbers below the given number'''
	
	sum = 0
	while(num > 0):
		sum += num
		num -= 1
	return sum
		
	
###########################################################################
		
#Function 4
def factorial(z):

	'''Finds the factorial of a given number'''
	if z == 0:
		numero = 1
		return numero
	numero = 1
	while z >= 1:
		numero = numero * z
		z = z - 1
	return numero		
    
############################################################################

#Function 5
def factor(baseNum,factor2):

	'''Takes two positive integers and sees if the second number is a factor of the first'''
	
	if baseNum % factor2 == 0:
		return True
	else:
		return False

############################################################################

#Function 6
def primeNum(primeNum):
	
	'''Determines whether a number is prime or not (must be greater than 2)'''
	
	if primeNum == 2:
		return True
	for i in range(3, primeNum):
		if primeNum % i == 0:
			return False
	return True
	
############################################################################

#Function 7
def isperfect(n):

	'''Determines whether a number is perfect of not'''
	
	sum = 0
	
	for x in xrange(1, n):
		if n % x == 0:
			sum += x
	return sum == n

############################################################################

#Function 8
def sumfactor(n):
	
	'''Takes the sum of the numbers digits and determines if it is a factor of the original number'''
	
	sum = sum_digits(n)
	factorNum = factor(n, sum)
	
	return factorNum

###########################################################################
	
	
	
	
	
	
	
	
	
	

