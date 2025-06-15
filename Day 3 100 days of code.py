# Conditions Statememts, Logical operators, Code Blocks and Scope

#Control Flow With if else and conditional operators

#print("WElcome to the rollercoaster!")
#height = int(input("what is your height in cm?"))

#if height >= 120:
#    print("You can ride the rollercoaster")
#else:
#    print("Sorry, you have to grow taller before you can ride.")
    
#Comperatibe operators, that is, Greater than >, Less than <, Greater than or equal >=, 
#Less than or egual to <=, equal to == and not equal to !=
#You'l find that we are using one equal sign at some point and sometimes we are using
#two equal signs and it might be confusing.
#We use one equal sign when assigning a value to a variable and two equal signs when
#we are comparing whether two values are equal.

#WHen using the if/else, it is important to check spacing or indetation
#You'll see the if and else are on the same indent while the print functions are 
#on different indents.


#Odds or even exercise
#Modulo OPeration (%) = This is a method for deviding a number by another number and get the reminder
#Example 7 % 3 output will be 1

#7 % 3

# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#if number % 2 == 0:
#    print("This is an even number")
#else:
#    print("This is an odd number")


#Nested if statemnets and elif statements

#Nested if/else statement
#The reason as to why it is called nested if is beacause it is nested inside 
#the if block

#print("WElcome to the rollercoaster!")
#height = int(input("what is your height in cm?"))

#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is your age? "))
#    if age <= 12:
#        print("Please pay $5.")
#    elif age <= 18:
#        print("please pay $7")
#    else:
#        print("please pay $12.")
#else:
#    print("Sorry, you have to grow taller before you can ride.") 

#elif, we can use as many elif statement as we want inside our nested if statement above

#Interactive Coding Exercise

# 🚨 Don't change the code below 👇
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI = round(weight / height ** 2) 

#if BMI < 18.5:
#    print(f"Your BMI is {BMI}, you are underweight")
#elif BMI < 25:
#    print(f"Your BMI is {BMI}, You are normal weight")
#elif BMI < 30:
#    print(f"Your BMI is {BMI}, you are overweight")
#elif BMI < 35:
#    print(f"Your BMI is {BMI}, you are obese")
#else:
#    print(f"Your BMI is {BMI}, you are clinically obese")


#If you have more than three condition or multiple conditions, you can go directly to elif




#Miltiple IF statements in succession

#print("WElcome to the rollercoaster!")
#height = int(input("what is your height in cm?"))
#bill = 0

#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is your age? "))
#    if age <= 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")

#    photo = input("Do you need a photo Taken? Y or N ")
#    if photo == "Y":
#        bill += 3
        
#        print(f"Your final bill is ${bill}")

#    else:
#      print("Sorry, you have to grow taller before you can ride.") 


#Interactive Coding Exercise - Piza Order Practice


#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bill = 0

#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#elif size == "L":
#    bill += 25

#if add_pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else: 
#        bill += 3

#if extra_cheese == "Y":
#    bill += 1

#print(f"Your final bill is ${bill}")

#Challenge

#Age = int(input("What is you age? "))
#if Age < 13:
#    print("You can only watch PG movies")
#elif Age < 18:
#    print("You can only watch PG-13 and PG movies")
#else:
#    ID = input("Do you have an ID ")
#    if ID == "Y":
#        print("You can watch all movies")
#    else:
#        print("You need an ID to watch adult movies")


#Challeng 2

#student_age = int(input("What is your age? "))

#if student_age < 5:
#    print("You're too young to register")
#elif student_age <= 17:
#    Parent_or_Gadian = input("Are you with a Parent or Gadian? Y/N? ")
#    if Parent_or_Gadian == "Y":
#        print("You are allowed to register with supervision")
#    else:
#        print("You need a Parent or Gadian to register")
#else:
#    print("You are allowed to register independently")


 
# if is used when you only have one condition eg if hungry, eat

#if....else is used When there are two out comes eg if rain, stay home else go

# if....elif....else is used when there are many posible choices eg Grading and BMI category

# Nested if is used when one condition depends on another being true eg if not raining,
#the check money
# Its indentatio is very different from the other conditions, examples in the code
#blocks above



# Logical Operators :-
# "and", "or" & "not"

# "and"
#When you conbine two different conditions using an "and" operator, the both have to 
#be true for the entire line of code to be true.
#If just one of them is true, then the overal thing evaluates to false
#We use it when all the conditions are true

#"or"
# We use "or" when we want one of the condition to be True
#If one of the conditions is true or both of them are true, then it will
#evaluate to true
#It is only when both the conditions are faulse does it become false

# "not"
#What the "not" operatror does is that it basically reverses a condition.
#if the condition is faulse then it becomes true and if it is true it becomes false

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#bill = 0

#if height >= 120:
#    print("You can ride the rollercoaster.")
#    age = int(input("What is your age? "))
    
#    if age <= 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7.")
#    elif 45 <= age <= 55:
#        print("Everything is gonna be okay. Have a free ride on us!")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")

#    photo = input("Do you want a photo taken? Y or N: ")
#    if photo.upper() == "Y":
#        bill += 3

#    print(f"Your final bill is ${bill}.")

#else:
#    print("Sorry, you have to grow taller before you can ride.")


#Interactive Coding Exercise - LOve Calculator

# 🚨 Don't change the code below 👇
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


#New functions:- 1. .upper()- Converting to opper case, .lower() and .count() for
#counting lets say how many times a a chracter appears in a string

#combined_names_lower = name1.lower() + name2.lower()

#T = combined_names_lower.count("t")
#R = combined_names_lower.count("r")
#U = combined_names_lower.count("u")
#E = combined_names_lower.count("e")

#true = T + R + U + E

#L = combined_names_lower.count("l")
#O = combined_names_lower.count("o")
#V = combined_names_lower.count("v")
#e = combined_names_lower.count("e")

#Love = L + O + V + e

#love_score = str(true) + str(Love)
#love_score_int = int(love_score)

#if (love_score_int) < 10 or (love_score_int > 90):
#    print(f"Your score is {love_score_int}, you go together like coke and mentos")
#elif (love_score_int >= 40) and (love_score_int<= 50):
#    print(f"Your score is {love_score_int}, You are alright together")
#else:
#    print(f"Your score is {love_score_int}")



#Day 3 project Treasure Island game


print("Welcome to Treasure Island.\nYour mission is to find the tressure!")

Stage1 = input("You are at a cross road. Where do you want to go? Type \"left.\" or \"right.\"\n" ).lower()

if (Stage1 == "left"):
    stage2 = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if (stage2 == "wait"):
        stage3 = input("You have arrived at the island unhurmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
        if (stage3 == "red"):
            print("It is a room full of fire, Game over")
        elif (stage3 == "blue"):
            print("Its a room full of scopions, Game over!!")
        elif (stage3 == "yellow"):
            print("You found the treasure, you win!!")
    else:
        print("You Drowned, Game over")   
else:
    print("Game over")       
        
    
        




   