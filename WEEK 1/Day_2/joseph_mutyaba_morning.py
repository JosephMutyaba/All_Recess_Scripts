# control flow
# If statements
condition1 = True

if condition1 == True:
    print("This condition is true\n")
else:
    print("This condition is false\n")

# Alternatively
if not condition1:
    print("this condition is false\n")
else:
    print("this condition is true\n")


temperature = 23
if temperature > 30:
    print("It is hot outside\n")
elif temperature < 15:
    print("it is cold outside\n")
else:
    print("the weather is very normal\n")

# Exampple on age;
age = 23
if age < 18:
    print("You are underage\n")
elif age >= 18 and age <= 65:
    print("you are an adult\n")
else:
    print("you are a senior citizen\n")


# for loops
names = ['Kevin', 'John', 'Joseph', 'Julius']
for name in names:
    print(name)

# printing all items in one line
for i in names:
    print(i, end=" ")


# while loops
number = 12
while number >= 0:
    print(number)
    number -= 1


# break and continue statements
print("\n\n\n")
num = 0
while True:
    if num == 21:
        break
    else:
        print(num)
    num += 1

print("\n\n")
for i in range(12, 23):
    if i == 18:
        continue  # skip 18 and proceed with next statement
    else:
        print(i)


# Exception handling

try:
    num1 = int(input("Number one:"))
    num2 = int(input("Number two:"))
    num3 = num1/num2
    print("Result: " + str(num3))
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("Please enter numbers only")
finally:
    print("the finally code block will always execute irrespective of the occurence of an error\n\n")


# emotions
print("\n\n")
emotions = {
    'happy': 'Wow, its great your happy',
    'sad': 'thats bad, what is the problem',
    'angry': 'calm down please',
    'moody': 'Pray !!!!!!!!!'
}

emotional_input = input("Please enter your emotions: ")
emotional_input = emotional_input.lower()
if emotional_input in emotions.keys():
    print(emotions[emotional_input])
else:
    print("Sorry!, I can't understand your emotions")


# Exercise
# mental health
print("\n\n")
# Prompt students on a scale of 1:10 to rate their mental health
health_status = {
    1: 'Extremely poor',
    2: 'Very poor',
    3: 'Poor',
    4: 'Below average',
    5: 'Average',
    6: 'Above average',
    7: 'Good',
    8: 'Very good',
    9: 'Excellent',
    10: 'Exceptional'
}

try:
    response = int(input("On a scale of 1:10, rate your mental health: "))
    if response in health_status.keys():
        print("that's "+health_status[response])
    else:
        print("that's out of range!!!!!!")

except ValueError:
    print("Please enter numbers only")
except Exception:
    print("Something went wrong")
finally:
    print("thanks for your response ):")
