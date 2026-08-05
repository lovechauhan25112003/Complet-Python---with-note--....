'''FEATURES OF OOPS-1.
Class - Class is a blueprint , templet or prototype for create object with pre-defined property and method. 
            It does  not take any space on memory. Class is not a real world entity
    eg- 
    class Student:
        pass
'''
# class Car:
#     def __init__(self,brand, color):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"{self.color} {self.brand} is driving") 
# car1 = Car("BMW","Black")
# car2 = Car("Ford", "Red")
# car1.drive()


# class Men:
#     def about(self):
#         print(f"Name of men is : {self.name}")
#         print(f"Age of men is :{self.age}")
# men = Men()
# men.name="Love Kumar"
# men.age=22
# men.about()



'''class attribute:a attribute that blong to the class rather then a particular object'''
# class Emloyee:
#     company = "Google"
#     salary = 10000

# love = Emloyee()
# sumit = Emloyee()
# print(love.company)
# print(sumit.company)
# Emloyee.company="YouTube"# class attribute
# print(love.company)
# print(sumit.company)
# love.company="micro"  #rather than a particular object hence it is not a class attribut
# print(love.company)

# love.salary=18000  #instance variable
# sumit.salary = 35000











'''FEATURES OF OOPS-2
Object  : Object is an instance of class that execute the class. Once the object is created . It takes up the space like other variable in memory '''

# class Student:
#     name = "Love"
#     age = 22

# s1 = Student()
# print(s1.name)
# print(s1.age)

'''
Student -> class
s1      -> object
'''






'''Self -  self refer to the instance of class. It is automatically passed with a function call from an object
or 
a reference to the current instance of the class. It is used to access variables and methods associated with the current object.'''
# class Emp:
#     company = "Google"
#     def getSalary(self):
#         print("Salary is look")
# love = Emp()
#  love.getSalary()
# # or
# Emp.getSalary(love)







'''Constructor : A constructor is a special type of method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class. In Python, the constructor method is defined using the __init__() method.

Types of constructor - 

1.Default Constructor: 
A constructor that takes no parameters other than self'''
# class Student:
#     def __init__(self):
#         self.name = "unknown"
#         self.grade = "N/A"
# s1 = Student()
# print(s1.name)

'''2. Parameterized Constructor- A constructor that accept costom values when instantiated, allowing each object to have unique initial states
or a const which has  parameter is called a parameter constructor '''

class User:
    def __init__(self,username, email, role="Memberr"):
        self.username = username 
        self.email = email
        self.role = role   #Default parameter value

u1 = User("alex99", "alex@exaple.com")
u2 = User("admin_sam", "sam@example.com")

'''Technically , __init__() is not the method that creates the object - it only initializes it
__new__()- Responsible for creating the object in memory and returning it

while __init__()- receives the newly created objects (as self) and assigns its attributes'''

# class BankAccount:
#     def __init__(self, account_holder, balance=0, account_type="Savings"):
#         self.account_holder = account_holder
#         self.balance = balance
#         self.account_type = account_type
#     def show_details (self):
#         print(f"Holder: {self.account_holder} | Balance: ${self.balance} | Type : {self.account_type}")   
        
# user1 = BankAccount("Rahul")
# user1.show_details()

# user2 = BankAccount("Love", 5000)
# user2.show_details()

# user3 = BankAccount("Ritik",50000,"Current")
# user3.show_details()







'''Instance Variable - Object-specific
An instance variable is a variable that belongs to an object. Each object has its own copy of instance variables.
eg - name and age are instance variable'''
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Love",24)
# s2 = Student("Riku",16)

# print(s1.name)
# print(s2.age)

'''Class variable - share/common across objects
A class variable is shared among all objects of a class. It belongs to the class rather than individual objects.
eg - college is a class variable'''

# class Student:
#     college = "ABC College"
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Rahul")
# s2 = Student("Rahul")

# print(s1.college)
# print(s2.college)



'''Instance Method - An instance method is a method that operates on an instance of a class. It can access and modify the instance variables of the object. Instance methods are defined using the def keyword and take self as the first parameter.

or simple way- An instance method works with instance variables and uses the self parameter. It is declared using the def keyword.'''

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)

# s1 = Student("Love")
# s1.show()

'''Class Method - A class method is a method that operates on the class itself rather than an instance of the class. It can access and modify class variables. Class methods are defined using the @classmethod decorator and take cls as the first parameter.

or simple way-  A class method works with class variables and uses the cls parameter. It is declared using the @classmethod decorator.'''

# class Student:
#     college = "ABC College"

#     @classmethod
#     def show_college(cls):
#         print(cls.college)

'''Static Method - A static method is a method that does not operate on an instance of the class or the class itself. It is defined using the @staticmethod decorator and does not take self or cls as parameters. Static methods are used for utility functions that do not require access to instance or class variables.

or simple way- A static method does not work with instance or class variables. It is declared using the @staticmethod decorator.'''

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b
# print(Calculator.add(10, 20))









'''self-self is instance of the class 
it is automatically passed with the function call from the object'''

# class Emp :
#     def show():
#         print("I am love")    
# l = Emp()
# Emp.show(l)

# class Emp :
#     def show(self):
#         print("I am love")
# l = Emp()
# Emp.show(l)

'''static : A static method is a method inside a class that does not use the class instance (self) or the class itself (cls).'''
# class Emp:
#     @staticmethod
#     def greet():
#         print("Good Morning ")
# e = Emp()
# e.greet()

# class Math:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def multiply(a,b):
#         return a*b
# # static method ko call karne ke 2 method
# print(Math.add(10,20))  # class se
# m = Math()
# print(m.multiply(10,10)) #object se 

'''Encapsulation:Data + Methods ko ek class me bind karna → Encapsulation
       Data Hinding: data hiding is the process of protecting the member of the class from unintended changes
       '''
# Types of Encapsulation in Python
'''1. Public Members
Fully accessible from anywhere
No underscore'''

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand #public
#         self.model = model #public
#     def show(self):
#         print("Brand:",self.brand)
#         print("Model",self.model)
# c = Car("Toyota","Fortuner")
# print(c.brand) #allowed
# print(c.model) #allowed
# c.show()


# 2. Protected Members
'''Ek underscore _variable
Conventionally protected hote hain (matlab subclass use kar sakti hai)
Direct access discouraged, par roka nahi jaata'''

# class Person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age

# class Student(Person):
#     def show(self):
#         print("Name:",self._name) #allowed(subclass)
#         print("Age",self._age)
    
# s = Student("Love",22)
# s.show()
# print(s._age) #Access from outside (possible but not recommended)


'''Private Members'''
# Double underscore __variable
# Class ke bahar directly access not allowed
# Yeh real encapsulation deta hai

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amout):
#         if amout>0:
#             self.__balance = amout
#         else:
#             print("Invalid amount")
# acc = BankAccount(50000)

# print(acc.get_balance())
# acc.set_balance(6000)
# print(acc.get_balance())

'''python encapsulation'''
# class Student:
#     def __init__(self,name,marks):
#         self.name = name #public
#         self._marks = marks #protected
#         self.__fees = 20000 #private
#     def show_details(self):
#         print("Name:",self.name)
#         print("Marks:",self._marks)
#         print("Fees:",self.__fees) #allowed inside class
#     #Getter for private variable
#     def get_fees(self):
#         return self.__fees
#     def set_fees(self,amount):
#         if amount>0:
#             self.__fees = amount
#         else:
#             print("Invalide amount")

# s = Student("Love",44)
# #public
# print(s.name)

# #protected(allowed but not recommended)
# print(s._marks)

# #private(Not allowed - error)
# # print(s.__fees)

# #correct way to access private variable
# print(s.get_fees())

# #correct way to update private variable
# # s.set_fees(2000)
# # print(s.get_fees())












''' Abstraction: abstraction is the process of hiding the implementation details and showing only impotant/useful part to the user '''
