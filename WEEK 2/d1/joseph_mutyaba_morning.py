# Object Oriented Programming
# class
import math


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


car1 = Car("tesla", "model s", 2022)
print(car1.make)
print(car1.model)
car1.start_engine()
car1.stop_engine()


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of $%.2f successful. New balance: $%.2f" %
              (amount, self.balance))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of $%.2f successful. New balance: $%.2f" %
                  (amount, self.balance))
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def display_balance(self):
        print("Account holder: %s" % self.account_holder)
        print("Account number: %s" % self.account_number)
        print("Current balance: $%.2f" % self.balance)


# Creating a bank account
account = BankAccount("123456789", "John Alexander", 1000.0)

# Displaying account information
account.display_balance()

# Making a deposit
account.deposit(500.0)

# Withdrawing money
account.withdraw(200.0)

# Trying to withdraw more than the available balance
account.withdraw(1500.0)

# Displaying final account balance
account.display_balance()


# Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating a rectangle object
rectangle = Rectangle(5, 7)

# Calculating and printing the area
area = rectangle.calculate_area()
print("Area:", area)

# Calculating and printing the perimeter
perimeter = rectangle.calculate_perimeter()
print("Perimeter:", perimeter)


# University student
class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def print_details(self):
        print(self.name)
        print(self.course)
        print(self.year)


student1 = Student("Joseph Maximillian", "BSSE", 2023)
student1.print_details()


# Exercise 1


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


# Creating a circle object
circle = Circle(3)

# Calculating and printing the circumference
circumference = circle.calculate_circumference()
print("Circumference:", circumference)

# Calculating and printing the area
area = circle.calculate_area()
print("Area:", area)

# exercise 2: Calculate and display employee bonuses(0.15) of salary: Employee1->150000, Employee2->230000


class Emp_Bonus:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        bonus = (0.15)*self.salary
        print("your bonus is:", bonus)


emp1 = Emp_Bonus(150000)
emp1.calculate_bonus()

emp2 = Emp_Bonus(230000)
emp2.calculate_bonus()


# Encapsulation
# Example with a bank account class
class BankAcoount:
    def __init__(self, acc_number, balance):
        self._acc_number = acc_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print("Withdrawal of $%.2f successful. New balance: $%.2f" %
                  (amount, self._balance))
        else:
            print("Insufficient funds. Withdrawal canceled.")


my_account = BankAccount("223838493022", 30000)
my_account.deposit(1000)
print(my_account.balance)

my_account.withdraw(100)
print(my_account.balance)


class Temp_converter:
    def __init__(self, celsius):
        self._celsius = celsius

    def celsius_to_fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Creating a TemperatureConverter object
converter = Temp_converter(37)

# Converting Celsius to Fahrenheit
fahrenheit = converter.celsius_to_fahrenheit()

# Printing the converted value
print("37 degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.")


# ------------ ------------- Assignment-----------
"""
    Assignment1:  
    Show encapsulation with employee information to give 
    pay increamentation (Salary with employee information to new_salary)
    e.g from 850000 to 1000000
 
"""


class SalaryInrease:
    def __init__(self, employee_name, current_salary):
        self.__employee_name = employee_name
        self.__current_salary = current_salary

    def increase_salary(self):
        if self.__current_salary < 1000000:
            self.__current_salary = 1000000
            print(
                f"\nCongratulations {self.__employee_name} !!!!!!!!!! \nyour salary has been increased")
            print(f"your new salary is {self.__current_salary}")
        else:
            print(
                f"\n{self.__employee_name} your salary is {self.__current_salary}")


# employee instantiation
employee1 = SalaryInrease("Louis", 850000)
employee1.increase_salary()

employee2 = SalaryInrease("Kolin", 50000)
employee2.increase_salary()

employee3 = SalaryInrease("Maxwell", 1550000)
employee3.increase_salary()

employee4 = SalaryInrease("Doris", 3250000)
employee4.increase_salary()
