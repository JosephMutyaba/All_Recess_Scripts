# Basic Operators
# 1: Arithmetic operators
"""
    %
    + addition
    - subtraction
    * multiplication
    / division
    // division which returns quotient without the remainder.
    ** Exponentiation(used for raising a value to power e.g, a**2)
    
"""
# 2: Comparison operators
"""
    ==
    <=
    >=
"""

# 3Logical operators
"""
    and
    or
    not
"""

# 4: Assignment operators
"""
    =
    +=
    -=
    /=
    *=
    %=
    **=
"""

# 5: Membership operators
"""
    in -> checks if a value exists in a sequence
    not in ->checks if a value does not exist in a sequence.
    
"""

# 6: Identity operator
"""
    is      -> checks if two values are the same
    is not
"""

#  %    modulus
import tkinter as tk
a = 15 % 4
print(a)


#     + addition
a = 5 + 3
print(a)

#     - subtraction
b = 10 - 4
print(b)


#     * multiplication
c = 2 * 6
print(c)


#     / division
d = 15 / 5
print(d)


#     // division which returns quotient without the remainder.
e = 17 // 4
print(e)


#     ** Exponentiation
f = 2 ** 3
print(f)


# Comparison operators
num = 5
if num > 0:
    print("Number is positive")
else:
    print("Number is negative")


# example 2
n = 5
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

k = 2
r = 9
if k > r:
    print("k is larger than r")
else:
    print("r is larger than k")

if k <= 17:
    print("you are a child")

if r >= 18:
    print("you are an adult")

if r != k:
    print("r and k are different")

# Example with logical operators
a1 = True
a2 = False
print(a1 and a2)
print(a1 or a2)

print(not a1)
print(not a2)


c1 = 2
c2 = 34
c3 = 4
c4 = 5
c5 = 3

c1 += 34
c2 *= 2
c3 /= 4
c4 %= 3
c5 **= 2


print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

# membership assignment operators
cars = ['rolls-royce', 'Pajero', 'Prado', 'awudi', 'cadillac']

if 'rolls-royce' in cars:
    print("rolls-royce in cars' list")
else:
    print("rolls-royce is not in cars list.")

# identity operators
x1 = 2
x2 = 4
print(x1 is x2)
print(x1 is not x2)
print(x1 == x2)
print(x1 != x2)
print(x1 < x2)
print(x1 > x2)
print(x1 <= x2)

z1 = [1, 2, 3, 4, 5]
z2 = [1, 2, 3, 4, 5]
print(z1 is z2)
print(z1 is not z2)

# bitwise operator
"""
    used to perform operations on individual bits of binary numbers.
    Bitwise AND('&')
    Bitwise OR('|') 
    Bitwise XOR('^')
    Bitwise NOT('~')
    Bitwise left shift('<<')
    Bitwise right shift('>>')
    
"""
aer = 10
aer1 = 2

#     Bitwise AND('&')
aer2 = aer & aer1
print(aer2)

#     Bitwise OR('|')
aer3 = aer | aer1
print(aer3)

#     Bitwise XOR('^')
aer4 = aer ^ aer1
print(aer4)

#     Bitwise NOT('~')
aer5 = ~aer
print(aer5)

#     Bitwise left shift('<<')
aer6 = aer << 3
print(aer6)

#     Bitwise right shift('>>')
aer7 = aer >> 3
print(aer7)


#################################### Example Calculator in class ##############################
def add(x, c):
    return x+c


def divide(x, c):
    return x/c


def multiply(x, c):
    return x*c


def subtract(x, c):
    return x-c


def main():
    print("A simple Calculator")
    h1 = int(input("Number 1: "))
    h2 = int(input("Number 2: "))
    h3 = input("Operator-> +, -, /, * ")

    chars = ['+', '*', '-', '/']
    if h3 in chars:
        if h3 == "*":
            print("Answer: "+str(multiply(h1, h2)))

        if h3 == "+":
            print("Answer: "+str(add(h1, h2)))

        if h3 == "-":
            print("Answer: "+str(subtract(h1, h2)))

        if h3 == "/":
            print("Answer: "+str(divide(h1, h2)))

    else:
        print("Invalid Operator, plz try again!")


if __name__ == "__main__":
    main()


# Assignment ###############################:
"""
    Create a simple calculator program with a gui interfacem doing addition, subtraction, division and multiplication using tkinter
    Make title of calculator program window with your name eg "jeff geoff simple calculator"
"""

# Function to clear the entry field


def clear():
    entry_num.delete(0, tk.END)


# Function to delete the last character in the entry field
def delete_entry():
    current = entry_num.get()
    entry_num.delete(len(current)-1)


# Function to update the number entry field
def update_entry(number):
    current = entry_num.get()
    entry_num.delete(0, tk.END)
    entry_num.insert(tk.END, current + str(number))


# Function to perform calculation
def calculate():
    expression = entry_num.get()
    try:
        result = eval(expression)
        entry_num.delete(0, tk.END)
        entry_num.insert(tk.END, str(result))
    except:
        entry_num.delete(0, tk.END)
        entry_num.insert(tk.END, "Invalid expression")


#           Main window
window = tk.Tk()
window.title("Joseph Mutyaba Simple Calculator")  # Setting the window title

# Create the number entry field
entry_num = tk.Entry(window, width=20, font=("Arial", 12))
entry_num.grid(row=0, column=0, columnspan=4, pady=10)

# Create clickable buttons for numbers
but_1 = tk.Button(window, text="1", command=lambda: update_entry(
    1), width=5, height=2, font=("Arial", 12))
but_1.grid(row=1, column=0)

but_2 = tk.Button(window, text="2", command=lambda: update_entry(
    2), width=5, height=2, font=("Arial", 12))
but_2.grid(row=1, column=1)

but_3 = tk.Button(window, text="3", command=lambda: update_entry(
    3), width=5, height=2, font=("Arial", 12))
but_3.grid(row=1, column=2)

but_4 = tk.Button(window, text="4", command=lambda: update_entry(
    4), width=5, height=2, font=("Arial", 12))
but_4.grid(row=2, column=0)

but_5 = tk.Button(window, text="5", command=lambda: update_entry(
    5), width=5, height=2, font=("Arial", 12))
but_5.grid(row=2, column=1)

but_6 = tk.Button(window, text="6", command=lambda: update_entry(
    6), width=5, height=2, font=("Arial", 12))
but_6.grid(row=2, column=2)

but_7 = tk.Button(window, text="7", command=lambda: update_entry(
    7), width=5, height=2, font=("Arial", 12))
but_7.grid(row=3, column=0)

but_8 = tk.Button(window, text="8", command=lambda: update_entry(
    8), width=5, height=2, font=("Arial", 12))
but_8.grid(row=3, column=1)

but_9 = tk.Button(window, text="9", command=lambda: update_entry(
    9), width=5, height=2, font=("Arial", 12))
but_9.grid(row=3, column=2)

but_0 = tk.Button(window, text="0", command=lambda: update_entry(
    0), width=5, height=2, font=("Arial", 12))
but_0.grid(row=4, column=1)

# Buttons for arithmetic operations
but_addition = tk.Button(window, text="+", command=lambda: update_entry("+"),
                         width=5, height=2, font=("Arial", 12))
but_addition.grid(row=1, column=3)

but_subtraction = tk.Button(
    window, text="-", command=lambda: update_entry("-"), width=5, height=2, font=("Arial", 12))
but_subtraction.grid(row=2, column=3)

but_multiplication = tk.Button(
    window, text="*", command=lambda: update_entry("*"), width=5, height=2, font=("Arial", 12))
but_multiplication.grid(row=3, column=3)

but_division = tk.Button(
    window, text="/", command=lambda: update_entry("/"), width=5, height=2, font=("Arial", 12))
but_division.grid(row=4, column=3)

# Create button for delete and clear operations
# delete
but_delete = tk.Button(
    window, text="DEL", command=delete_entry, width=5, height=2, font=("Arial", 12))
but_delete.grid(row=4, column=0)

# clear all
but_clear = tk.Button(window, text="CL", command=clear,
                      width=5, height=2, font=("Arial", 12))
but_clear.grid(row=4, column=2)

# '=' button for calculation
but_equal = tk.Button(window, text="=", command=calculate,
                      width=16, height=2, font=("Arial", 12))
but_equal.grid(row=5, column=0, columnspan=4, pady=10)

# Starting the main loop
window.mainloop()
