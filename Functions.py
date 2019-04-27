def myFunction():
	print("hello")
	
def addNums(x, y, z):
	print("x + y = " + str(x+y+z))

def substractNums(x,y,z):
	print("x - y = " + str(x-y-z))
	
def squareNums(z):
	print("squared product of z = " + str(z*z))
	
	
myFunction()
m = float(input("x : "))
n = float(input("y : "))
s = int(input("z : "))
addNums(m,n,s)
substractNums(m,n,s)
squareNums(s)

