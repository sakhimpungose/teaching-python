# Single line comment
'''
This is a multiline comment
'''

# Variables
'''
age = 14
name = "John"
isMarried = False
favColor = ("Red", "Blue", "Yellow")
'''

# Data Types
'''
string
number
boolean
tuple
list
'''

'''
favColor = ["Red", "Blue", "Yellow"]
print(favColor)
# 0, 1, 2
favColor[1] = "Black"
print(favColor)
favColor.append("Gold")
print(favColor)
'''


# Functions
# y = x + z
'''
def sum(x, y):
    return x + y

def intro(name, surname, age):
    return "Hi, my name is " + name + " " + surname + " and I am " + str(age) + " years old. I am learning Python" 

print(intro("John", "Cena", 77))
print(intro("Stan", "Peterson", 68))
'''

'''
Quadratic equation
x^2 - 4x - 5 = 0

(x + 1) (x - 5) = 0

(x + 1) = 0
x = -1

(x - 5) = 0
x = 5

thus, x = -1, or x = 5
'''
def problem1(x):
    return x**2 - (4 * x) - 5

# print(problem1(-1))
# print(problem1(5))

problemSpace = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9]

for i in range(-3,100):
    answer = problem1(i)
    if answer == 0:
        print("(" + str(i) + ")^2 - 4(" + str(i) + ") - 5 = " + str(answer))
