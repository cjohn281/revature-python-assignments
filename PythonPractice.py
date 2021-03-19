##### Run Python Programs #####

# Make a Python program that prints your name.
print("Chris Johnson")
print()

# Make a program that displays the lyrics of a song.
verse_1a = "There once was a ship that put to sea, The name of the ship was the Billy of Tea"
verse_1b = "The winds blew up, her bow dipped down, Oh blow, my bully boys, blow"
chorus_a = "Soon may the Wellerman come, To bring us sugar and tea and rum"
chorus_b = "One day, when the tonguing is done, We'll take our leave and go"
print(verse_1a)
print(verse_1b)
print()
print(chorus_a)
print(chorus_b)
print()


##### Variables #####

# Make a program that displays several numbers.
num1 = 5
num2 = 17.5
num3 = -25
print(num1)
print(num2)
print(num3)
print()

# Make a program that solves and shows the summation of 64 + 32
sum = 64 + 32
print(sum)
print()

# Do the same as in 2 (previous question), but make it sum x + y
x = 64
y = 32
sum = x + y
print(sum)
print()


##### Strings #####

# Make a program that displays your favorite actor/actress
print("Al Pacino")
print()

# Try to print the word 'lucky' inside s.
s = "lucky"
print(s)
print()

# Try to print the day, month, year in the form "Today is 2/2/2016"
day = 16
month = 3
year = 2020
print("Today is %d/%d/%d" % (month, day, year))
print()


##### String Replace #####

# Try the replace program
text = "one two four."
x = text.replace("four", "three")
print(x)


# Can string be replaced twice?
# Yes

# Does replace only work with words or also phrases?
# Replace works with both words and phrases


##### String Find #####

# Find out if a string is case sensitive
import re
text = "this is teXt."
if re.search('[A-Z]', text):
  print('Yes')
else:
  print('No')

# What if a query string appears twice in a string?
# Only the index of the first occurence is returned.

# Write a program that asks console input and searches for a query.
text = input("Enter text: ")
if (text.find("hello") > -1):
  print("The input contains hello")
else:
  print("the input does not contain hello")


##### String Join #####

# Create a list of words and join them
animals = ["cat", "dog", "elephant", "armadillo"]
print(" ".join(animals))

# Try changing the separator string from a space to an underscore
print("_".join(animals))


##### String Split #####

# Can a string be split on multiple characters?
# Yes, you can define a separator that consists of multiple characters

# Can you split this string: 'World,Earth,America,Canada'
locations = 'World,Earth,America,Canada'
print(locations.split(","))

# Given an article, can you split it based on phrases?
# Yes, you can define the separator to be a phrase.


##### Random numbers #####

# Make a program that creates a random number and stores it into x.
import random
x = random.randrange(1, 100)

# Make a program that prints 3 random numbers.
print(random.randrange(1, 100))
print(random.randrange(1, 100))
print(random.randrange(1, 100))

# Create a program that generates 100 random numbers and find the frequency of each number.
import random
random_list = []
for i in range(0,100):
  n = random.randint(1,100)
  random_list.append(n)

count_list = [0] * 100
for x in random_list:
  count_list[x-1] = count_list[x-1] + 1

counter = 1
for x in count_list:
  print("%d occured %d time(s)" % (counter, x))
  counter = counter + 1


##### Keyboard input #####

# Make a program that asks a phone number.
number = input("Enter your phone number: ")

# Make a program that asks the users preferred programming language.
prefLang = input("Enter your preferred language: ")

##### If statements #####

# Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.
num = input("Enter a number betwee 1 and 10: ")
if num < 0 or num > 10: 
	print("The number is not valid") 
else: 
	print("You entered %d" % (num))

# Make a program that asks a password.
password = raw_input("Password: ") 
if password == "password": 
	print("Correct") 
else: 
	print("Incorrect password") 


##### For loops #####

# 1. Make a program that lists the countries in the set clist = ['Canada','USA','Mexico','Australia']
for country in clist: 
	print(country) 

# 2. Create a loop that counts from 0 to 100
for x in range(101):
	print(x)

# 3. Make a multiplication table using a loop
for num1 in range(1, 11):
  for num2 in range(1, 11):
    print("%d " % (num1 * num2), end='')
  print()

# 4. Output the numbers 1 to 10 backwards using a loop
for x in range(10, 0, -1):
	print(x) 

# 5. Create a loop that counts all even numbers to 10
for x in range(0, 11, 2):
	print(x)

# 6. Create a loop that sums the numbers from 100 to 200
sum = 0
for x in range(100, 201):
	sum = sum + x
print(sum)


###### While loops #####

# 1. Make a program that lists the countries in the set below using a while loop. clist = ["Canada","USA","Mexico"]
size = len(clist) 
i = 0 
while i < size: 
	print(clist[i]) 
	i = i + 1 

# 2. What‟s the difference between a while loop and a for loop?
# A for loop will run for a certain number of iterations, a while loop will run until a certain condition is met

# 3. Can you sum numbers in a while loop?
# Yes, but it usually makes more sense to use a for loop

# 4. Can a for loop be used inside a while loop?
# Yes


##### Functions #####

# 1. Make a function that sums the list mylist = [1,2,3,4,5]
def sum(list): 
	sum = 0 
	for e in list: 
		sum = sum + e 
	return sum 
print(sum(mylist)) 


# 2. Can functions be called inside a function?
# Yes

# 3. Can a function call itself? (hint: recursion)
# Yes

# 4. Can variables defined in a function be used in another function? (hint: scope)
# No


##### Lists #####

# Make a program that displays the states in the U.S. states = [ 'Alabama', .. ,'Wyoming' ]
for state in states: 
	print(state) 

# Display all states starting with the letter M
for state in states: 
	if state[0] == 'M': 
		print(state)


##### List operations #####

# Given the list y = [6,4,2] add the items 12, 8 and 4.
y.append(12) 
y.append(8) 
y.append(4)

# Change the 2nd item of the list to 3.
y[1] = 3


##### Sorting list #####

# Given a list with pairs, sort on the first element
#     x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort()

# Now sort on the second element
from operator import itemgetter 
x.sort(key=itemgetter(1))


##### Range function #####

# Create a list of one thousand numbers
nums = list(range(1,1001))

# Get the largest and smallest number from that list
print(min(nums)) 
print(max(nums))

# Create two lists, an even and odd one.
evens = list(range(2, 101, 2))
odds = list(range(1, 100, 2))


##### Dictionary #####

# Make a mapping from countries to country short codes
words = {}
words["US"] = "United States"
words["UK"] = "United Kingdom"
words["AUS"] = "Australia"
words["CA"] = "Canada" 

# Print each item (key and value)
for key, value in words.items():
	print(key + " = " + value)


##### Read file #####

# Read a file and number every line
filename = "test.py"

with open(filename) as f: 
	lines = f.readlines() 
	i = 1 
	for line in lines: 
 		print(str(i) + " " + line),  i = i + 1


# Find out what the program does if the file doesn‟t exist.
# A FileNotFoundError will be thrown

# What happens if you create a file with another user and try to open it?
# You may not be able to open it if you don't have the correct read permissions


##### Write file #####

# Write the text “Take it easy” to a file
file = open("test.txt","w") 
file.write("Take it easy\n") 
file.close()

# Write the line open(“text.txt”) to a file
file = open("test.txt","w") 
file.write("open(\"text.txt\")\n") 
file.close() 


##### Nested loops #####

# Given a tic-tac-toe board of 3x3, print every position
for x in range(1,4): 
	for y in range(1,4): 
	print(str(x) + "," + str(y)) 

# Create a program where every person meets the other
#     persons = [ “John”, “Marissa”, “Pete”, “Dayton” ]
for p1 in persons: 
	for p2 in persons: 
		print(p1 + " meets " + p2)

# If a normal for loop finishes in n steps O(n), how many steps has a nested loop?
# O(n)^2


##### Slices #####

# Take a slice of the list below:
#     pizzas = [“Hawai”,”Pepperoni”,”Fromaggi”,”Napolitana”,”Diavoli”]
slice = pizzas[0:3] 

# Given the text “Hello World”, take the slice “World”
slices = text.split(" ") 
print(slices[1])


##### Multiple return #####

# Create a function that returns a,b and a+b
def sum(a,b): 
	return a, b, a+b 

# Create a function that returns 5 variables
def test():
	name = "name"
	age = "age"
	address = "address"
	phone = "phone"
	email = "email"
	return name, age, address, phone, email


##### Scope #####

# Add a function reduce amount that changes the variable balance
balance = 10 
def reduceAmount(x): 
	global balance 
	balance = balance - x 

# Create a function with a local variable
def localVar():
	x = 5
	return x


##### Time and date #####

# Print the date in format year-month-day
import time
current = time.localtime(time.time()) 
year,month,day,hour,minute = current[0:5] 
print(str(year) + "-" + str(month) + "-" + str(day)) 


##### Try except #####

# Can try-except be used to catch invalid keyboard input?
# Yes

# Can try-except catch the error if a file can‟t be opened?
# Yes

# When would you not use try-except?
# You shouldn't use try-except to catch errors that you can't or wont handle properly


#########################
##### OOP Exercises #####
#########################


##### Class #####

# Can you have more than one class in a file?
# Yes

# Can multiple objects be created from the same class?
# Yes

# Can objects create classes?
# No

# Using the code above, create another object
example = Website('archive.org') 
example.showTitle() 

# Add a method to the class: location()
def getLocation(self): 
    print(self.location)


##### Getter and setter #####

# Add a variable age and create a getter and setter
class Person: 
  def __init__(self, name, age): 
    self.name = name
    self.age = age

  def get_age(self):
    return self.age

  def set_age(self, age):
    self.age = age

# Why would you use getter and setter methods?
# Allows for accessing and mutating fields of a class safely


##### Modules #####

# Import the math module and call the sin function
import math 
print(math.sin(5))

# Create your own module with the function snake()
# save the snake function in animals.py
def snake():
	print("hssss")

import animals
animals.snake()

##### Inheritance #####

# Create a new class that inherits from the class App
class newClass(App): 
	def getVersion(self): 
	print('This is a new class')

# Try to create a class that inherits from two super classes (multiple inheritance)
class newerClass(firstClass, secondClass):
	def getVersion(self)
	print("This class extends 2 super classes")


##### Static method #####

# Can a method inside a class be called without creating an object?
# Yes

# Why does not everybody like static methods?
# Because accessing methods without instantiating a class goes against the object oriented paradigm


##### Iterable #####

# What is an iterable?
# an object that can be used as a sequence 

# Which types of data can be used with an iterable?
# lists, strings, dictionaries and sets


##### Classmethod ######

# What is a classmethod?
# A classmethod is method that has access to the state of the class object, but not the states of any specific objects created from that class.

# How does a classmethod differ from a staticmethod?
# staticmethod does not have access to the state of the class object, or the states of any objects instantiated from the class.


##### Multiple inheritance #####

# Do all programming languages support multiple inheritance?
# No

# Why would you not use multiple inheritance?
# It increases the cohesion of the classes in your code, making them less reusable for other projects.

# Is there a limit to the number of classes you can inherit from?
# No