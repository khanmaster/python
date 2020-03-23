# # What is a function
# # It's a special relationship where each input has a single out put
# # Functions are a tool, within python, that allows you to embed particular actions using code and make them reusable.
# # The most important principle is  " Don't Repeat Yourself "
# # functions give you the facility of REUSING your code
#
# # Lets see how it works
# # function starts with key word def
# def hello():
#     # followed by the name of the function given by you
#     print("Hello")
#
#
# # you call the function with the name of the function as below
# hello()
#
#
# # function with arguments
# def func(a, b):
#     return a + b
#
#
# print("The sum is", func(10, 20))
# # what would be the outcome ?
# # Run the function to see the outcome

# third type of function are with default argument
# def func(a=10, b=30):
#     return a|b
# print("The sum is ", func())
# what would be the outcome now?

# # Last type of function is with default value and again passing the value
# def func(a=10, b=30):
#     return a | b
# print("The sum is ", func(20, 40))

# Lets create functions that we use in a calculator
# what functions do we use in a calculator
# add - minus divide etc.
# create an add function
# def add(a,b):
#     return a+b
# print(add(2,6))
# # I would like everyone to create functions for
# # multiplication, subtraction and division
#
# def sub(c,d):
#     return c-d
# print(sub(6,2))


# Class - Classes are a way of bringing both data and functionality together
# define a class
# Note class name should always start with capital
#
# class Dog:
#     animal_kind = "canine"  # class variable
#     def __init__(self, name, age): # initialising the class
#         self.name = name
#         self.age = age
#     # when a function is defined within the class classed as method
#     # let's define a method now
#     def bark(self):  # self refers to the current class
#         # print(self.animal_kind)
#         return "woof"
# # Now lets print class and the method within the class
# print(Dog.animal_kind)
# print(type(Dog))
# # create an object from a class
# name_age  = Dog('fido', 9)
# age_name = Dog('dido', 3)
# print("Name of my Dog", name_age.name)
# print("Age of my do is ", age_name.age)
# print(name_age.bark())
# print(age_name.bark())
# # instantiating an object from a class


# Lets create a class for students

# class Car:
#     car_type = "sports"  # class variable called car_type
#
#     def drive(self):
#         return "fast"
#
#
# print(Car.car_type)
# print(type(Car))


# create a student class
# have a method enrol
# pringt student type and some message in the method enrol

# class Student(object):
#     pass

#
# class Student:
#     student_type = "trainee"
#
#     def enrol():
#         return "trainee"
#
# print(Student.student_type())
# print(type(Student))
# #
# #
# # james = Student
# # print(james.enrol())
#
# class Student:
#     student_type = "Trainee"
#     def enrol():
#         return "Completed"
#
# print(Student.student_type)
# # print(Student.enrol())
# #-------------
# # Libraries and modules
# import random
# import math
# print(random.random())
# num_float = 23.44
# print(math.ceil((num_float)))
# print(math.floor(num_float))
