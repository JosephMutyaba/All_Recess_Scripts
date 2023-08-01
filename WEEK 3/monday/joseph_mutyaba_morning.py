"""
    Regular expressions (regex) are powerful tools for pattern matching and text manipulation. They allow you to define patterns and search for matches within strings. Here are some common regex patterns and their meanings:

1. Literal Characters:
- `abc`: Matches the exact sequence "abc" in the string.

2. Character Classes:
- `[abc]`: Matches any single character in the set "a", "b", or "c".
- `[a-z]`: Matches any lowercase letter.
- `[A-Z]`: Matches any uppercase letter.
- `[0-9]`: Matches any digit.
- `[^0-9]`: Matches any character that is not a digit.

3. Predefined Character Classes:
- `\d`: Matches any digit (equivalent to `[0-9]`).
- `\D`: Matches any non-digit character (equivalent to `[^0-9]`).
- `\w`: Matches any alphanumeric character (letters, digits, and underscores).
- `\W`: Matches any non-alphanumeric character.
- `\s`: Matches any whitespace character (spaces, tabs, newlines).
- `\S`: Matches any non-whitespace character.

4. Quantifiers:
- `*`: Matches zero or more occurrences of the preceding pattern.
- `+`: Matches one or more occurrences of the preceding pattern.
- `?`: Matches zero or one occurrence of the preceding pattern.
- `{n}`: Matches exactly n occurrences of the preceding pattern.
- `{n,}`: Matches n or more occurrences of the preceding pattern.
- `{n,m}`: Matches between n and m occurrences of the preceding pattern.

5. Anchors:
- `^`: Matches the start of a string.
- `$`: Matches the end of a string.

6. Groups and Capturing:
- `(pattern)`: Defines a group for capturing a matched pattern.
- `(?:pattern)`: Defines a non-capturing group.

7. Alternation:
- `pattern1|pattern2`: Matches either pattern1 or pattern2.

8. Escaping Special Characters:
- `\`: Escapes a special character, allowing it to be treated as a literal.

Regular expressions provide a powerful and flexible way to match
and manipulate text, and their usage can become more complex 
with the combination of different patterns and modifiers. 
Experimenting with regex and referring to the documentation for
the specific regex engine you are using can help you master this useful skill.
"""

import re
#tyg
text="Hello I am Joseph Maximillian with 24 years of experience in Programming"
match = re.search(r"\b\w+\b", text)

if match:
    print("Matches: ", match.group())
    
matches = re.findall(r"\d+", text)
print("Matches: ", matches)

# Example 2: Validate email address/Id
def validate_email(email):
    pattern=r'^[\w\.~`-]+@[\w\.~]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
    
email1='jobro@gmail.com'
email2='jobro@com'

print("email1: ",validate_email(email1))
print("email2: ",validate_email(email2))


# generators and iterators
def factorial(x):
    if x==0:
        return 1
        # yield 1
    else:
        return x * factorial(x - 1)
        # return x * factorial(x - 1)
    
    
for n in range(0,10):
    print(factorial(n))
    
    
    
def squares():
    for i in range(1, 10):
        yield i**2
        
#create an iterator object that yields the square of numbers from 1-10
squares_iterator =squares()

# prints the first 5 squares of numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))  
    
#Decorators @my_decorator
def my_decorator(func):
    def inner():
        print("this is the decorator")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("this is the outer decorator")
    
    
outer_decorator()