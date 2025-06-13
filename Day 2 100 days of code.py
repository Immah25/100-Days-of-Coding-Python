#Today we'll be learning about Data Types, Numbers, Operations, Type Conversions and f-Strings
#Data Types :- Strings, Integers, Float and Boolean

#Strings
#This is a piece of Text or Character eg "world"
#Because we call them a string of characters, we can pull individual characters from the string eg: print("hello"[0]) to get "H"
#In programing we start couting from 0, because we work with binaries

#print("Hello"[0])

# "H" is in position 0 "E" is in position 1 "L" is in position 2 and so on
# The process of pulling a particuler element or charcter from the string is called Subscripting
#The number inside the brackets determines which character you are going to pull out


#Integers
#It consists of numbers with out any decimal places eg 0-9
#Lets say you are writing a big number like 123456789, nomarly we would seperate them with commas 123,456,789, 
#but in python programing we seperate them with underscores - 123_456_789


#Float
#Consists of decimal numbers or float point numbers eg 234.564


#Boolean
#A boolean consists of two possible values, True or Faulse
#The should start with a capital letter - True, Faulse
#We are going to use it alot in our programs to test if something is True or Faulse 


              #Type Error, Type Checking, Type Conversion

#point to note: len() function works with strings alone and also you can not Concatenate strings and variables

#Type() Fucntion
#num_char = len(input("what is your name? "))
#type(num_char)

#The type() function is used to help us identify the type of data that we are working with 
#for example in the example above, we are are working with an integer

#Type Casting or type conversion
#This is the process where we change a piece of data from one particular data type to another.
#For example num_char has a dta type of an integer and we wnat to turn it into a string:

#new_num_chur = str(num_char)
#type(new_num_chur)

#After converting them to string, we can easily work with them using the functions len() and also Concatenate

#print('Your Name has ' + new_num_chur + ' characters')

#The code above worked because all the data types are the same


#a = float(100)
#print(type(a))

#print(70 + float("100.5"))

#You can simply conver a data type from its original type to another type by 
#simply adding the name or shortform name of you disired data type Eg
# int(x), float(x), str(x)

#print(str(70)+str(100))

#Interactive coding exercise - Data types

# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit n2umber: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#My code
#print(int(two_digit_number[0]) +int(two_digit_number[1]))

#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]
#results = (int(first_digit)+int(second_digit))

#print(results)

#Breaking the problem into small chunks!



#Mathematical OPerations in python

#Addition
#A plus sign can eihter be used to Concatenate or add numbers - float and int.

#Subtraction
#In subtraction we use the following subtration sign, "-". eg 10 - 9

#Multiplacation
#In multiplacation we use the following asterics, "*" eg 45 * 65

#Division
#In division we use the following sign "/" forwar slash. eg 6 / 5

#Exponents, or Raising a number to a power
#we use two asterics - "**" eg 2 ** 2
# when working with such mathematical operations, it is important to note the order of 
# operations eg BODMAS which stands for:
#B= Brackets
#O= Of - Exponents
#D= Division
#M= Multiplacation
#A= Addition
#S= Subtraction

#3 * 3 + 3 / 3 - 3


#Interactive Coding Exercise- BMI Calculator

# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI = Weight(Kg)/Height**2 (m**2)

#BMI = int(weight) / float(height) ** 2
#BMI_as_int = int(BMI)
#print(BMI_as_int)


#Number Manipulation and F Strings in python

#print(8 / 3)

# If we want to round off the number or output we are going to get from 8/3, we 
#us the round function

#print(round(9 / 3))

#You can specify the nuber of digits you want to round them to, eg if we wanted to 
#rount it to two decimal places we could specifi:

#print(round(8 / 3, 2))

#print(round(2.6666666, 2))

#Lets say you wanted to get your out in int for unlike normally in float for
#while working with division, instead of converting it into an integer, you
# can use the flow division where you use use two division signs and you
#get your answer in int formart. eg : 

#print(8 // 3)

#Even if the out put has recurring decimals, the answer you get its an int. It
#cuts off the decimal numbers


#Lets say you are to devide a number by two and again by two, you can simply do 
#the following instead of having to divide the numbers again and again and again

#X = 20 / 2
#X /= 2

#print(X)

#Another example, you are tracking the score of a certain game

#score = 0

#score += 1

#score += 2

#print(score)

#Same applies to subtraction

#score2 = 30

#score2 -= 5

#score2 -= 10

#print(score2)

#Same applies to multiplacation

#Y = 5

#Y *= 2

#Y *= 6

#print(Y)

#f Strings
#The f String makes it easy for us to mix different strings and data types
#The f- String does all the converting for us and we dont have to worry about anything
#We place the f - String at the begining before the double or single quotes

#score = 0
#height = 1.8
#isWinning = True

#print(f"Your score is {score}, Your height is {height}, you are winning is {isWinning}")

#We can use carly braces to place variable into our strings as illustrated above above

#Interactive Coding Exercise - Life in weeks

# 🚨 Don't change the code below 👇
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#1 year hase 365 days, 52 weeks, and 12 months
#Days = 365 * (90 - age)
#Weeks = 52 * (90 - age)
#Months = 12 * (90 - age)

#My code
#age_left = 90 - int(age)
#print(age_left)

#Days = 365 * age_left
#Weeks = 52 * age_left
#Months = 12 * age_left

#Message = (f"You have {Days} days, {Weeks} weeks, and {Months} months")
#print(Message)




#Day 2 Project Tip Calculator 

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00/5) * 1.12


print('Welcome to the tip calculator')
bill = float(input('what is the total bill $'))
tip = int(input('How much tip would you like to give? 10, 12, 15? '))
people = int(input('How many people to split the bill? '))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = total_tip_amount + bill
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
print(f'Each person should pay: ${final_amount}')


