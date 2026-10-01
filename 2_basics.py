"""
what is self?
Self is a reference variable inside a method declaration
It helps user to access members of a class inside a method
Also it helps the object to access the members associated with self
---------------------------------------
# global variables- which we can access inside a class, inside a method and outside
# outside the class as well
# name = 'SBI'
# IFSC = 'sbi123123'
class Bank:
    # class level/static variable
    name = 'SBI'
    IFSC = 'sbi123123'
    
    def online(self):
        # # local variables
        # name = 'SBI'
        # IFSC = 'sbi123123'
        print('Bank name:',self.name)
        print('IFSC is:',self.IFSC)
b1 = Bank()
b1.online()
============================================
class Test:
    a = 100 # class level var. 

    def item(self):
        print('Item method')

    def m1(self):
        b = 200 # local var. 
        print(self.a,b)
        self.item()
        
t1 = Test()
t1.m1()
-----------------------------
name = 'AXIS Bank'
IFSC = 'AXIS123456'
class Bank:
    # class level/static variable
    name = 'SBI'
    IFSC = 'sbi123123'
    
    def online(self):
        # # local variables
        name = 'ABC Bank'
        # IFSC = 'sbi123123'
        print('Bank name:',self.name)
        print('Bank :', name)
        print('IFSC is:',self.IFSC)
b1 = Bank()
b1.online()
------------------------------
# name = 'SBI'
# IFSC = 'sbi123123'
# class Bank:
#     # class level/static variable
#     name = 'SBI'
#     IFSC = 'sbi123123'
#     name1 = 'hdfc'
    
#     def online(self):
#         # # local variables
#         # name = 'SBI'
#         # IFSC = 'sbi123123'
#         print('Bank name:',self.name)
#         print('IFSC is:',self.IFSC)
        
#         def on(): # it is working like a normal function
#             print('bank is:',self.name1)
#             # self is active as this calling is inside a method
#         on()


# b1 = Bank()
# b1.online()


# class Test:
#     a = 100 # class level var. 

#     def item(self):
#         print('Item method')
#         self.m1()
#         print('m1 method')

#     def m1(self):
#         b = 200 # local var. 
#         print(self.a,b)
#         self.item()

# t1 = Test()
# t1.m1()   


def sample():
    sample()

sample()
# Recursion is a property of a function in which
# function call itself again n again
# But in python we have recursion limit of 1000 iterations
# if that call exeeds then u will get RecursionError. 
-------------------------------
def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # 4 * factorial(3)*factorial(2)*factorial(1)
result = factorial(5)
print(result)
--------------------------------------
n=5
fact=1

for i in range(1,n+1):
    fact=fact*i

print(fact)

"""








