# Functions

# Standard Functions:
# These are the regular functions defined using the def keyword.
from math import *
import math


def greet(name):
    print("Hello, " + name + "!")


greet("LAWRENCE")


# Functions with Return Values:
# Functions can return values using the return statement.
def add_numbers(a, b):
    sum = a + b
    return sum


result = add_numbers(3, 5)


# Functions with Default Parameters:
# Functions can have parameters with default values.
def power(base, exponent=2):
    return base ** exponent


result1 = power(3)  # 3^2 = 9
result2 = power(3, 4)  # 3^4 = 81


# Variable Number of Arguments:
# Functions can accept a variable number of arguments using the *args syntax.
def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


result = add_numbers(1, 2, 3, 4, 5)  # 1 + 2 + 3 + 4 + 5 = 15


# Keyword Arguments:
# Functions can accept keyword arguments using the **kwargs
def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with keyword arguments
print_person_details(name="Joseph Maximillian", age=30, city="Kampala")

# modules in python
x = 16
print(sqrt(x))
print(pow(x, 2))
print(sqrt(139))


# input and output in python
fname = input("Enter your first name: ")
sname = input("Enter your second name: ")
year = int(input("Enter your year of birth: "))
age = 2023-year


print(f"Hello {fname} {sname}\nYou are now {age} years old")
print("\n")

a, r, f = map(int, input("Enter values: ").split())
print(f"{a} -> {r} -> {f}")

# capture input fronm a tuple.
w = (2, 1, 3, 2)
e = list(w)
e.append(int(input("Enter a value: ")))
w = tuple(e)
print(w)

nums = list(map(int, input("enter numbers: ").split()))
print(nums)

nums2 = set(map(int, input("enter set numbers: ").split()))
print(nums2)
