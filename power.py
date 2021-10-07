# import math that module permit to calculate some mathematical functions
import math

# function named introProgram to introduce the program
def introProgram():
    print("Welcome on my program")
    print("follow the instructions")

# function named menu to make a choice!
def menu():
    print("Enter ")
    print("1) For the perimeter of a Square")
    print("2) For the area of a Square")
    print("3) For the perimeter of a Triangle")
    print("4) For the area of a Triangle")
    print("5) For the perimeter of a Rectangle")
    print("6) For the area of a Rectangle")
    print("7) For the perimeter of a Circle")
    print("8) For the area of a Circle")
menu()    
    
    
ask = int(input(":"))  

def perimeter_of_square():
    a = int(input("Enter the dimension value: "))
    p = a * 4
    return p
    
def area_of_square(): 
    c = int(input("Enter the dimension value: "))
    a = c * c
    return a
    
 
def perimeter_of_triangle():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    p = a + b + c
    return p
    
def area_of_triangle(): 
    b = int(input("Enter the first number: "))
    h = int(input("Enter the second number: "))
    a = b * h**2
    return a
    

def perimeter_of_rectangle():
    L = int(input("Enter the first number: "))
    l= int(input("Enter the second number: "))
    p = 2 * (L + l)
    return p
    
def area_of_rectangle(): 
    L = int(input("Enter the first number: "))
    l = int(input("Enter the second number: "))
    a = L * l
    return a
    

def perimeter_of_circle():
    radius = int(input("Enter the radius of the circle: "))    
    p = 2 * math.pi * radius
    return p
    
def area_of_circle(): 
    radius = int(input("Enter the radius of the circle: "))
    a = math.pi * (radius**2)
    return a    
    
# conditions    
if ask == 1:
    print(perimeter_of_square())
elif ask == 2:
    print(area_of_square())
elif ask == 3:
    print(perimeter_of_triangle())
elif ask == 4:
    print(area_of_triangle())
elif ask == 5:
    print(perimeter_of_rectangle())
elif ask == 6:
    print(area_of_rectangle())
elif ask == 7:
    print(perimeter_of_circle())
elif ask == 8:
    print(area_of_circle())
else:
    print("Error, please try again")
