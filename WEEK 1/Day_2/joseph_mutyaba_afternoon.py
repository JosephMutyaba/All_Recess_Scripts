# Dictionaries->store elements in ket-Value pairs and don't allow duplicates
area_code = {
    256: 'Uganda',
    1: 'USA',
    44: 'Asia',
    254: 'Kenya'
}

print(area_code)
print(len(area_code))  # length of a dictionary
print(type(area_code))  # dictionary data type
print(area_code.get(254))  # accessing items in the dictionary
print(area_code[1])

codes = area_code.keys()
print(codes)


capitals = {
    'Uganda': 'Kampala',
    'USA': 'Washington',
    'Egypt': 'Accra',
    'UK': 'London'
}

# Ex1: Use the values() method to return a list of all values in a dictionary.
print("\n\n")
countries = area_code.values()
print(countries)


# Ex2: check if an item exists in the dictionary
print("\n\n")
response = int(input("Enter your country code: "))
if response in area_code.keys():
    print("the area code provided exist in our dictionary: ")
    print("the corresponding country is: "+area_code[response])
else:
    print("Sorry!!!\nthe area code provided is not in our dictionary")


# Ex3: How to change and update the dictionary items
area_code[44] = 'UK'
print("Updated dictionary items\n:")
print(area_code)


# Ex4: How to add dictionary items, How to remove dictionary items
# Adding keys values pair to dictionary
area_code[27] = 'SouthAfrica'
# Output: {'key1': 'value1', 'key2': 'new value', 'key3': 'value3', 'key4': 'value4'}
print(area_code)

# Removing keys value pair from dictionary
del area_code[1]
print("New area_code dictionary:\n")
print(area_code)


# Ex5: How to loop through a dictionary
# loop through the dictionary keys
print("\n\n")
print("Keys :")
for key in area_code.keys():
    print(key)

# loop through the dictionary values
print("\n\n")
print("Values:")
for value in area_code.values():
    print(value)


# combination->loop through the dictionary keys and values
print('\n\n')
print("Keys -> values")
for key, value in area_code.items():
    print(str(key)+"->" + value)


# Ex6: How to nest a dictionary
    # Creating a nested dictionary
print('\n')
Persons = {
    'person1': {
        'name': 'John',
        'age': 25,
        'country': 'USA'
    },
    'person2': {
        'name': 'Emma',
        'age': 30,
        'country': 'UK'
    }
}

# Accessing values in the nested dictionary
print(Persons['person1']['name'])  # Output: John
print(Persons['person2']['age'])   # Output: 30

# Modifying values in the nested dictionary
Persons['person1']['age'] = 26
print(Persons['person1']['age'])  # Output: 26

# Adding a new nested dictionary
Persons['person3'] = {
    'name': 'Mike',
    'age': 35,
    'country': 'Canada'
}

# Accessing the new nested dictionary
print(Persons['person3']['name'])  # Output: Mike


# datatypes
print('\n')
a = 12  # integers
a1 = -3
print(type(a))
print(type(a1))

b = 2.34  # floats
b1 = -3.2
print(type(b))
print(type(b1))

c = 5j  # complex numbers
c1 = -3j
c2 = 9+2j
print(type(c))
print(type(c1))
print(type(c2))

# datatypes conversion
print('\n')
v = '23'
v1 = int(v)
print(type(v))
print(type(v1))

print('\n')
w = 32
w1 = complex(v)
print(type(w))
print(type(w1))

print('\n')
# casting
p = int(1)
p1 = int(20000)
p3 = int('123')
print(type(p))
print(type(p1))
print(type(p3))


# Strings
name = 'Peter'
print(name+"\n")

q = """
    this
    is
    a
    multiline 
    string
"""
print(q+"\n")

# string as arrays tyg
name12 = "Raphael"
print(name12[0])
print(name12[1])
print(name12[2])
print(name12[3])


# Exercise1 Use len() to determine length of string
sName = "Louis"
print("\n", len(sName))

# Exercise2 Example of a for loop through a string
print('\n')
for i in sName:
    print(i)


# Exercise3 Example slicing a string
name16 = "Joseph Maximillian"
name15 = name16[0:6]
name14 = name16[7:]
print('\n'+name15)
print(name14)


# methods on strings
lName = 'MaKxwell'
fName = '     Alex    '

print('\n')
print(lName.upper())
print(lName.lower())
print(fName.strip())

# string concatenation
f1 = 'Sports'
f2 = 'galla'

print('\n'+f1+' '+f2)

# String formatting
d = 'you are {} years old'
age = 23
print('\n')
print(d.format(age))


# Booleans
bool1 = 30 < 20
bool2 = 30 == 30
bool3 = 30 == 35
print('\n', bool1)
print(bool2)
print(bool3)

owasp = '222werd'
num2 = 22
print(bool(owasp))
print(bool(num2))

# Exercise : Use a condition to show how to use booleans.
print('\n')
is_cold = True
if is_cold:
    print("It's a cold day!")
else:
    print("It's not cold today.")
