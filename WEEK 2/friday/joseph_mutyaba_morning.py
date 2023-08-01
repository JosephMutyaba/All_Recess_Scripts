from tkinter import ttk
from tkinter import font
from fpdf import FPDF
from tkinter import messagebox, filedialog
import tkinter as tk
from abc import ABC, abstractmethod
import math


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, 'is barking')


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is barking")


animal = Animal('generic Animal')
dog = Dog('generic Dog')
cat = Cat('generic Cat')

animal.eat()
dog.bark()
cat.meow()


# Exercise


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


circle = Circle(5)
print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())


# multiple inheritance                             tyg
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat_plants(self):
        print(f"{self.name} is eating plants.")


class Carnivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat_meat(self):
        print(f"{self.name} is eating meat.")


class Omnivore(Herbivore, Carnivore):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating both plants and meat.")


# Example usage:
lion = Omnivore("Lion")
lion.eat()  # Output: Lion is eating both plants and meat.
lion.eat_plants()
lion.eat_meat()

rabbit = Herbivore("Rabbit")
rabbit.eat()  # Output: Rabbit is eating.

eagle = Carnivore("Eagle")
eagle.eat()  # Output: Eagle is eating meat.


# method overriding
class Vehicle:
    def drive(self):
        print("Vehicle is being driven.")


class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")


class Bike(Vehicle):
    def drive(self):
        print("Bike is being ridden.")


def make_vcle_move(vehicle):
    vehicle.drive()


# Example usage:
car1 = Car()
car2 = Car()
bikes = Bike()

make_vcle_move(car1)
make_vcle_move(car2)
make_vcle_move(bikes)

vehicle = Vehicle()
vehicle.drive()  # Output: Vehicle is being driven.

car = Car()
car.drive()  # Output: Car is being driven.


# Polymorphism
# "Method overridding"
"""
    Method overriding occurs when a subclass provides its own 
    implementation of a method that is already defined in its superclass.
    This allows objects of different classes to have different behaviors 
    while being treated uniformly based on their common superclass.
"""


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# "Method overloading
"""
    Method overloading is the ability to define multiple methods 
    with the same name but different parameters. 
    Python does not natively support method overloading like 
    some other languages, but we can achieve similar functionality 
    using default parameter values or variable-length argument lists.
"""


# class MathUtils:
#     def add(self, x, y):
#         return x + y

#     def add(self, x, y, z):
#         return x + y + z


# # Example usage:
# math_utils = MathUtils()

# # print(math_utils.add(2, 3))  # Output: 5
# print(math_utils.add(2, 3, 4))  # Output: 9


#   -----------------Abstraction------------------------------------------------


class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print(f"{self.name} starts the car.")

    def stop(self):
        print(f"{self.name} stops the car.")


class Motorcycle(Vehicle):
    def start(self):
        print(f"{self.name} starts the motorcycle.")

    def stop(self):
        print(f"{self.name} stops the motorcycle.")


# Example usage:
car = Car("John")
car.start()  # Output: John starts the car.
car.stop()  # Output: John stops the car.

motorcycle = Motorcycle("Mike")
motorcycle.start()  # Output: Mike starts the motorcycle.
motorcycle.stop()  # Output: Mike stops the motorcycle.


#     ---------------------------------tyg-----------------
# Exercise 1
"""
Demonstrate abstraction using calculation of area oc a circlea nd rctangle
"""


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


# usage:
rectangle = Rectangle(4, 6)
rectangle_area = rectangle.calculate_area()
print("Rectangle Area:", rectangle_area)

circle = Circle(5)
circle_area = circle.calculate_area()
print("Circle Area:", circle_area)


#  --------------------------------Assignment------------------------------------------------
"""
    Create a receipt printing program with GUI interface.
    A more advanced detail wins more points.
"""

# Create the main window
root = tk.Tk()
root.title("Joseph Mutyaba Receipt Printing Program")
root.geometry("600x600")

# Function to add an item to the list


def add_item():
    item = item_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if item and quantity and price:
        items_listbox.insert("", tk.END, values=(item, quantity, price))
        item_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Information",
                               "Please enter item details.")


# Function to remove an item from the list
def remove_item():
    selected_item = items_listbox.focus()
    if selected_item:
        items_listbox.delete(selected_item)


# Function to generate the receipt preview
def generate_preview():
    receipt_text = ""
    receipt_text += "<b>Date: " + get_current_date() + "</b>\n\n"
    receipt_text += "<b>Seller:</b>\n" + seller_name_entry.get() + "\n" + \
                    seller_address_entry.get("1.0", tk.END) + "\n\n"
    receipt_text += "<b>Buyer:</b>\n" + buyer_name_entry.get() + "\n" + \
                    buyer_address_entry.get("1.0", tk.END) + "\n\n"
    receipt_text += "<b>Items:</b>\n"

    for item in items_listbox.get_children():
        item_values = items_listbox.item(item)["values"]
        receipt_text += f"{item_values[0]} - Quantity: {item_values[1]} - Price: ${item_values[2]}\n"

    receipt_text += "\n<b>Subtotal:</b> $" + str(get_subtotal()) + "\n"
    receipt_text += "<b>Tax:</b> $" + str(get_tax(get_subtotal())) + "\n"
    receipt_text += "<b>Total:</b> $" + \
        str(get_subtotal() + get_tax(get_subtotal()))

    preview_dialog = tk.Toplevel(root)
    preview_dialog.title("Receipt Preview")

    receipt_preview = tk.Label(
        preview_dialog, text=receipt_text, font=("Arial", 12), justify=tk.LEFT)
    receipt_preview.pack(padx=20, pady=20)


# Function to generate the PDF
def generate_pdf():
    file_path = filedialog.asksaveasfilename(
        initialdir=".",
        title="Save Receipt as PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        if not file_path.endswith(".pdf"):
            file_path += ".pdf"

        c = FPDF()
        c.add_page()
        c.set_font("Arial", "B", 12)
        c.cell(0, 10, "Receipt", ln=True, align="C")
        c.ln(10)

        receipt_text = ""
        receipt_text += "Date: " + get_current_date() + "\n\n"
        receipt_text += "Seller:\n" + seller_name_entry.get() + "\n" + \
                        seller_address_entry.get("1.0", tk.END) + "\n\n"
        receipt_text += "Buyer:\n" + buyer_name_entry.get() + "\n" + \
                        buyer_address_entry.get("1.0", tk.END) + "\n\n"
        receipt_text += "Items:\n"

        for item in items_listbox.get_children():
            item_values = items_listbox.item(item)["values"]
            receipt_text += f"{item_values[0]} - Quantity: {item_values[1]} - Price: ${item_values[2]}\n"

        receipt_text += "\nSubtotal: $" + str(get_subtotal()) + "\n"
        receipt_text += "Tax: $" + str(get_tax(get_subtotal())) + "\n"
        receipt_text += "Total: $" + \
            str(get_subtotal() + get_tax(get_subtotal()))

        c.set_font("Arial", "", 10)
        c.multi_cell(0, 10, receipt_text)

        try:
            c.output(file_path)
            messagebox.showinfo(
                "PDF Generated", "Receipt saved as PDF successfully!")
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the PDF: {str(e)}")


# Helper function to get the current date
def get_current_date():
    import datetime
    return datetime.date.today().strftime("%Y-%m-%d")


# Helper function to calculate the subtotal
def get_subtotal():
    subtotal = 0.0
    for item in items_listbox.get_children():
        item_values = items_listbox.item(item)["values"]
        price = float(item_values[2])
        subtotal += price
    return subtotal


# Helper function to calculate the tax
def get_tax(amount):
    tax_rate = 0.07
    return amount * tax_rate


# Create the seller section
seller_frame = tk.Frame(root)
seller_frame.pack(pady=10)

seller_name_label = tk.Label(
    seller_frame, text="Seller Name:", font=("Arial", 12, "bold"))
seller_name_label.pack(side=tk.LEFT)

seller_name_entry = tk.Entry(seller_frame)
seller_name_entry.pack(side=tk.LEFT, padx=10)

seller_address_label = tk.Label(
    seller_frame, text="Seller Address:", font=("Arial", 12, "bold"))
seller_address_label.pack(side=tk.LEFT)

seller_address_entry = tk.Text(seller_frame, height=3, width=40)
seller_address_entry.pack(side=tk.LEFT, padx=10)

# Create the buyer section
buyer_frame = tk.Frame(root)
buyer_frame.pack(pady=10)

buyer_name_label = tk.Label(
    buyer_frame, text="Buyer Name:", font=("Arial", 12, "bold"))
buyer_name_label.pack(side=tk.LEFT)

buyer_name_entry = tk.Entry(buyer_frame)
buyer_name_entry.pack(side=tk.LEFT, padx=10)

buyer_address_label = tk.Label(
    buyer_frame, text="Buyer Address:", font=("Arial", 12, "bold"))
buyer_address_label.pack(side=tk.LEFT)

buyer_address_entry = tk.Text(buyer_frame, height=3, width=40)
buyer_address_entry.pack(side=tk.LEFT, padx=10)

# Create the items section
items_frame = tk.Frame(root)
items_frame.pack(pady=10)

items_label = tk.Label(items_frame, text="Items", font=("Arial", 12, "bold"))
items_label.pack()

item_frame = tk.Frame(items_frame)
item_frame.pack()

item_label = tk.Label(item_frame, text="Item:", font=("Arial", 12, "bold"))
item_label.pack(side=tk.LEFT)

item_entry = tk.Entry(item_frame)
item_entry.pack(side=tk.LEFT, padx=10)

quantity_label = tk.Label(item_frame, text="Quantity:",
                          font=("Arial", 12, "bold"))
quantity_label.pack(side=tk.LEFT)

quantity_entry = tk.Entry(item_frame, width=10)
quantity_entry.pack(side=tk.LEFT, padx=10)

price_label = tk.Label(item_frame, text="Price:", font=("Arial", 12, "bold"))
price_label.pack(side=tk.LEFT)

price_entry = tk.Entry(item_frame, width=10)
price_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(items_frame, text="Add Item", command=add_item)
add_button.pack(pady=10)

items_listbox = ttk.Treeview(items_frame, columns=(
    "Item", "Quantity", "Price"), show="headings")
items_listbox.heading("Item", text="Item")
items_listbox.heading("Quantity", text="Quantity")
items_listbox.heading("Price", text="Price")
items_listbox.pack(pady=10)

remove_button = tk.Button(items_frame, text="Remove Item", command=remove_item)
remove_button.pack(pady=10)

# Create the receipt preview frame
receipt_preview_frame = tk.Frame(root)
receipt_preview_frame.pack(pady=10)

receipt_preview_button = tk.Button(
    receipt_preview_frame, text="Preview Receipt", command=generate_preview)
receipt_preview_button.pack(side=tk.LEFT, padx=10)

generate_pdf_button = tk.Button(
    receipt_preview_frame, text="Generate PDF", command=generate_pdf)
generate_pdf_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()
