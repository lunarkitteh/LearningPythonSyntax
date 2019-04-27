import math
x = int(input("Please enter your first number:"))
y = int(input("Please enter your second number:"))
z = int(input("Please enter your third number:"))
print("The sum of those 3 number is "+ str(x+y+z)) # cast x+y into string
print("the square root of those 3 numbers is "+str(math.sqrt(x+y+z)))

# NOTE :
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)


#if x > 10:
	# Don't forget to indent
	#print('you entered a number greater than 10')
#else:
	#print('you entered a number less than 10.')
