"""
We can use docstring for multiline comment purpose
print('hello')
a = 10
print(10)
#---------------------------
OOP -  Object Oriented Programming

What is Class and Object??

Def class =  properties(compoments/items) + behaviour (action)
Class is a blueprint, template, structure of a How user expect the
 thinfs in the program
To represent the class we need to refer some rules
use class keyword
then if class name is single word then prefer Title case
if class name is 2 or more words then prefer Pascal case
ex. class Car, class FlipkartOnline
#------------------------------------------
class Car:
    # Properties
    doors = 4
    wheels = 4
    engine = 'quadrajet'
    maker = 'BMW'

    # behaviour/action
    # method -  function written inside a class
    def start_engine(self):
        print('Engine started')

# to execute above plan we  need an OBJECT
#  To create an object we need to call class
d_501 = Car()  #  __init___, __new__
# here d_501 is ur object
# Def- Object is an Instance of a class, means  using an object
# user can access members of a class, outside it. 
d_501.start_engine()
print(d_501.doors)      
#-------------------------------------
# Assignment: Create a class for Human with few properties and nbehaviour and 
# Try to access all the members of class Human using object.   
#-------------------------------------------------
"""
class Car:
    # Properties
    doors = 4
    wheels = 4
    engine = 'quadrajet'
    maker = 'BMW'

    # behaviour/action
    # method -  function written inside a class
    def start_engine(self):
        print('Engine started')

c1 = Car()
c1.maker = 'ferrari'
c1.doors = 2
c1.engine = 'f1'
print(c1.maker,c1.doors,c1.engine)
#--------------------------
b1 = Car()
print(b1.maker,b1.doors,b1.engine)