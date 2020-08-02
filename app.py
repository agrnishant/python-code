#/usr/local/bin/python3
# Primitive types in Python are - number(int, float), string, bool

import math

print("Hello World")
print ("+" * 20)

count = 10
rating = 3.99
bool = True
name = "Nish\"Agr\"ant" # \" will use " as part of the string now..Similarly we can have newline \n etc
message = """ Hi John, "Double quotes work here without backslash"
I am writing this email to connect with you
Pls write back to me at nish@gmail.com
Thx,
Nishant
""" # Do note that triple quotes """ is like multiline string or backtick literals and can span multiple lines

first = "  aaditya"
last = " agrawal "
full = first + " " + last   # aaditya  agrawal
Full = f"{len(first)} {last} {5+6}" # 7 Agrawal 11 - another way of formatting string by putting a "f" or "F" at start
print(full, full.upper(), full.title()) #  aaditya  agrawal   AADITYA  AGRAWAL   Aaditya  Agrawal 
print(full.strip()) # strips any spaces at the beg or end - try using "lstrip" or "rstrip" as well
print(full.find("adi")) # 3  - note that we have given 2 spaces before aaditya - find() returns the index
print("adi" in full) # True - find() returns the index while "in" returns boolean
print("adi" not in full) # False - find() returns the index while "in" or "not in" returns boolean
print(full.replace("aadi", "ADI")) #   ADItya  agrawal (with 2 spaces at start)
print(Full) # 9  agrawal  11
print(count, rating, bool, name, message, len(message))
print(10*3, 10**3, 10/3, 10//3, 10%3) # 30 1000 3.3333333333333335 3 1 - note we use // for integer division

x = 10
x += 5; # we can leave a semi-colon at the end too without a problem
print (x)
print (round(2.5), abs(-2.1) ) #2 2.1 - these are limited mathematical inbuild fns here - import math object for more
print(math.ceil(2.5), math.factorial(x), math.floor(2.5)) #3 1307674368000 2

temp = input("Enter the room temperature: ")
print(type(temp)) # <class 'str'>
actualTemp = int(temp) + 1 # converts temp to int type and then does math op; without this math op will fail - as - string + num
print(f"temp: {temp}, actualTemp: {actualTemp}") # temp: 11, actualTemp: 12 (inputted temp as 11)

print(name[1:-1]) # ish"Agr"an - note -1 refers to the first char from the end of string
print(name[0], name[-1], name[0:3], name[:3], name[0:], name[:]) # N t Nis Nis Nish"Agr"ant Nish"Agr"ant

print("bag" > "BAG") # True
print(ord("b"), ord("B")) # 98 66 - gives out ASCII values

if actualTemp > 30:
    print("Its hot") #note indentation here determines what is part of if/elif/else block
    print("Drink Water more hence") #this statement is also part of if block
elif actualTemp > 20:
    print("Its nice weather")
    print("Go out and play") #this statement is also part of elif block
else:
    print("Its cold out there")
    print("Have something hot to drink") #this statement is also part of elif block
print("Done") # this will always be executed irrespective of which ever if-else block executes

msg = "Cold" if actualTemp <= 20 else "Hot" # ternary operator example - similar to ? : in C/JS
print("Appears that it is very " + msg) #Appears that it is very Hot

highIncome = False
goodCredit = True
student = False
if (highIncome or goodCredit) and not student: # example of Logical operators (and or not)
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

age = 6
if age >= 18 and age < 65:
    print ("Eligible to vote")
elif 0 <= age < 18 :  # example of chaining comparison operators (instead of using and/or)
    print ("Just a kid")
else:
    print ("Enjoy the retirement")

success = False # below is the example of for-else loop
for num in range(3): # here num is taken as a variable automatically and is assigned an "int" type - range is 0 to 2
    print(["Attempt", num])
    if success:
        print("Successful")
        break
else: # note the indentation for the else if not going to be in line with the if above
    print("UnSuccessful even after 3 attempts")

for num in range(1, 10, 3): # here - range is 1 to (10-1) - and it skips each by 3 (or say adds 3 starting from 1) - 1,4,7
    print(["Attempt", num, num * "."]) # num * "." prints . as many times as the num

for x in range(3): # outer loop x - Nested Loops example
    for y in range(2): # nested loop y in x - outputs (0,0), (0,1), (1,0), (1,1), (2,0), (2,1)
        print(f"({x}, {y})")

for z in range(2): # Note range is an iterable type in python
    print(z, type(z), type(range), type(range(z))) # 0 <class 'int'> <class 'type'> <class 'range'>

for z in "Python": # Note string is another iterable type in python
    print(z, type(z)) # P <class 'str'>

someNum = 100
while someNum > 0: # while loop keeps going till someNum is positive no.
    print(someNum)
    someNum//=2 #outputs integer value of someNum

# example similar to run python3 ($ python3) >>> - where the I/P doesn't terminate until Ctrl+D
cmd = "" # while loops
while cmd.lower() != "quit":  # press some combination of quit to terminate (as Quit or quit or QUit)
    cmd = input(">")    # >1+1
    print("..", cmd)    # .. 1+1

cmd = "" # while loops
while cmd.lower() != "quit":  # press some combination of quit to terminate (as Quit or quit or QUit)
    cmd = input(">")    # >1+1
    print("..", cmd)    # .. 1+1

# infinite-while loops
while True:  # This loop keep running infinitely until someone presses some combination of "quit"
    if cmd.lower() == "quit":
        break
    cmd = input(">")    # >1+1
    print("..", cmd)    # .. 1+1

# 
# Nishants-MacBook-Pro:python-code nishantagrawal$ python3 app.py 
# Hello World
# ++++++++++++++++++++
# 10 3.99 True Nish"Agr"ant  Hi John, "Double quotes work here without backslash"
# I am writing this email to connect with you
# Pls write back to me at nish@gmail.com
# Thx,
# Nishant
#  150
# 30 1000 3.3333333333333335 3 1
# 15
# 2 2.1
# 3 1307674368000 2
# x: 11
# <class 'str'>
# x: 11, y: 12
# ish"Agr"an
# N t Nis Nis Nish"Agr"ant Nish"Agr"ant
# True
# 98 66

######## note that name[-1] corresponds to going back from the end of string as in circular list
######## also note that name[0:3] is same as name[:3]
######## also note that name[0:] is same as name[:], and gives out the entire string
