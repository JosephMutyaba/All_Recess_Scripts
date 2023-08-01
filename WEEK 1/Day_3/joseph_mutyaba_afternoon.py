# Exercise1 (Lists)
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ['Kevin', 'Julius', 'Lawrence', 'John', 'hHellen']
print(names[1])

# 2. Write a python program to change the value of the first item to a new value
names[0] = "Emmanuel"
print("Modified List:", names)

# 3. Write a python program to add a sixth item to the list
names.append("Maxiwell")
print("Modified List:", names)

# 4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print("Modified List:", names)

# 5. Write a python program to remove the 4th item from the list
del names[3]
print("Modified List:", names)

# 6. Use negative indexing to print the last item in your list
print(names[-1])


# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
print("\n")
fruits = ["Apple", "Banana", "Orange", "papal", "Elderberry", "Fig", "Grape"]
for i in range(2, 5):  # Use a range of indexes to print the 3rd, 4th, and 5th items
    print(fruits[i])


# 8. Write a list of countries and make a copy of it.
countries = ["Brazil", "Canada", "Australia", "Chile", "France"]
copy = countries.copy()  # Making a copy
print("Original List:", countries)
print("Copy of the List:", copy)


# 9. Write a python program to loop through the list of countries
for country in countries:
    print("Country:", country)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["Lion", "Elephant", "Cow", "Giraffe", "Rhino"]
ascending_order = sorted(animals)  # Sort the list in ascending order
# Sort the list in descending order
descending_order = sorted(animals, reverse=True)

# Print the original list and the sorted lists
print("Original: ", animals)
print("Ascending: ", ascending_order)
print("Descending: ", descending_order)


# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
print('\n')
print("Animal names with 'a':")
for animal in animals:
    if 'a' in animal:
        print(animal)


# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["Joseph", "Emma", "Michael", "Sophia"]
second_names = ["Maximillian", "Smith", "Louis", "Brown"]

# Join the two lists
full_names = [first + " " + second for first,
              second in zip(first_names, second_names)]

# Print the full names
print("Full Names:", full_names)


# Exercise2 (Tuples)
# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print("Favorite phone brand:", favorite_brand)


# 2. Use negative indexing to print the 2nd last item in your tuple.
second_last_item = x[-2]
print("Second last item:", second_last_item)

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
x = list(x)
x[1] = "itel"
x = tuple(x)
print("Updated tuple:", x)


# 4. Write a python program to add “Huawei” to your tuple.
x = x + ("Huawei",)
print("Updated tuple:", x)


# 5. Write a python program to loop through the tuple above.
for j in x:
    print(j)


# 6. Write a python program to remove/delete the first item in your tuple.
x = x[1:]  # here I create a new tuple excluding the first item
print("Updated tuple:", x)


# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
ugandan_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print("Uganda cities tuple:", ugandan_cities)


# 8. Write a python program to unpack your tuple.
city1, city2, city3, city4 = ugandan_cities   # Unpacking the tuple
# Print the unpacked variables
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)


# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
for lm in range(1, 4):
    print(ugandan_cities[lm])

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Emma", "Michael")
second_names = ("Louis", "Raphael", "Johnson")
full_names = first_names + second_names
print("Full names tuple:", full_names)


# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied colorse: ", multiplied_colors)


# 12. Return the number of times 8 appears in this tuple
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print("times 8 appears:", count)


# Exercise3 (Sets)
# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
favorite_beverages = set(["Coffee", "Tea", "Passion"])
print("Favorite beverages:", favorite_beverages)


# 2. Use the correct method to add 2 more items to the beverages set.
favorite_beverages.add("Water")
favorite_beverages.add("Soda")
print("Updated beverages set:", favorite_beverages)

# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is in.")
else:
    print("Microwave is not in.")


# 4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print("Updated set:", mySet)


# 5. Write a python program to loop through the set above.
for K in mySet:
    print(K)


# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in
# the list to elements in the set.
fruits = {"apple", "banana", "orange", "mango"}
new_fruits = ["grape", "pineapple"]
fruits.update(new_fruits)
print("Updated set:", fruits)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 40}
first_names = {"Josephine", "Emmanuel", "Michael"}
joined_set = ages.union(first_names)
print("Joined set:", joined_set)


# Exercise4 (Strings)
# 1. Declare two variables, an integer and a string and use the correct method to concatenate
# the two variables.
num = 10
text = "You are {} years old "
print(text.format(num))


# 2. Consider the example below;
# txt = “ Hello,    Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = "       Hello,            Uganda!         "
no_space = " ".join(txt.split())
print("Trimmed string:", no_space)


# 3. Write a python program to convert the value of ‘txt’ to uppercase.
upper_case = txt.upper()
print(upper_case)


# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
altered = txt.replace('U', 'V')
print("Replaced string:", altered)


# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
x = y[1:4]
print("Returned range of characters:", x)


# 6. The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)


# Exercise5 (Dictionaries)
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.
# Add this dictionary to your .py file
# Shoes = {
# “brand” : “Nick”,
# “color” : “black”,
# “size” : 40
# }
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Shoe size:" + str(Shoes["size"]))


# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print("Update:", Shoes)


# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)


# 4. Write a python program to return a list of all the keys in the dictionary above.
keys = list(Shoes.keys())
print(keys)


# 5. Write a python program to return a list of all the values in the dictionary above.
values = list(Shoes.values())
print("Values: ", values)


# 6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("A key named 'size' exists.")
else:
    print("A key named 'size' does not exist.")


# 7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, "->", value)


# 8. Write a python program to remove “color” from the dictionary.
del Shoes["color"]
print("New Shoes:", Shoes)


# 9. Write a python program to empty the dictionary above.
Shoes.clear()
print("Empty Shoes dictionary:", Shoes)


# 10. Write a dictionary of your choice and make a copy of it.
attributes = {"fname": "John", "lname": "Kevin", "age": 30}
attributes_copy = attributes.copy()
print("Attributes_copy:", attributes_copy)


# 11. Write a python program to show nested dictionaries
# Define a nested dictionary
Personal_info = {
    "address": {
        "street": "123 Fake St",
        "city": "Old York",
        "country": "Brazil"
    },
    "contacts": {
        "email": "pedic@mail.com",
        "phone": "+256 772404901"
    }
}
# Access and print values from the nested dictionary
print("Street:", Personal_info["address"]["street"])
print("City:", Personal_info["address"]["city"])
print("Country:", Personal_info["address"]["country"])
print("Email:", Personal_info["contacts"]["email"])
print("Phone:", Personal_info["contacts"]["phone"])
