# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    # your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00
car3 = Vehicle()
car3.name = "zzz"
car3.color = "black"
car3.kind = "sedan"
car3.value = 100000.00
# test code
print(car3.name+" "+"is a "+car3.color+" "+car3.kind+" worths "+(str(car3.value)))

class Dogs:
	name = ""
	kind = ""
	weight = 0.00
dog1 = Dogs()
dog1.name = "zzzzz"
dog1.kind = "border collie"
dog1.weight = 5.37
print(dog1.name + "is a "+ dog1.kind+ " with a weight of "+(str(dog1.weight))+"Kg")
