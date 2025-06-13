
#print('Hello world')
#print('Day - Python print fuction')
#print('The fuction is declared like this:')
#print('print("what to print")')
#print('print(\'what to print\')')

#Sring Manipulation and code inteigence
#In the previous codes, we hade to write a print fuction for each of
#the three codes that we wanted them to be printed in a different line 
#but the is a way we can write the code in one print fuction to give 
#us each ot the sentences in a different line as we wanted earlier 
#using backward slash and n - \n.

#print('Hello world\nHello world\nHello world')
#print('Day 1 python fuction\nThe fuction is declared like this:\nprint(\'what to print\')')
#print('Day 1 - Python function\nThe function is declared like this:\nprint("what to print")')

               #String Concatenation
#String concantenation means joining two or more strings to form one bigger string

#print('Hello' + 'Emmanuel')

#If you look at the following code snipet, i have combined 'Hello' and my name
#'Emmanuel' with a plus sign, but there is no space between the two, Ouput:HelloEmmanuel.
#There is no space in between them because we do note have a space character in between them!
# We can add a space in three ways:
# 1. Adding a space after Hello:

#print('Hello '+ 'Emmanuel')

# 2. Adding a space Before Emmanuel:

#print('Hello' + ' Emmanuel')

# 3. Adding another string in between the two through string concantenation
# which will be just a space:

#print('Hello' + ' ' + 'Emmanuel')

#In python, spaces are very important- the spaces that we add on our code
#For example if i added a tab using a tab key in the code bellow, i am getting an
#IndentationError = (base) manuh@manuh-pop-os:~$ /bin/python3 "/home/manuh/Desktop/python projects/hello.py"
#  File "/home/manuh/Desktop/python projects/hello.py", line 42
#   print('Hello worl')
#IndentationError: unexpected indent
#    print('Hello world')#

#So, when you are coding in python it is important that you start off all of you code at the 
#beging of the line and that you don't accidentally have any space at
#or any tabs you have inserted infront of the line of the code

#Indentation Errors highlight issuse with spacing

            #Debbuging
#Debugging Exercise
#Fix the code below 👇

#Fix the code below 👇

#print("Day 1 - String Manipulation")
#print("String Concatenation is done with the \"+\" sign.")
#print('e.g. print("Hello " + "world")')
#print("New lines can be created with a backslash and n.")


                  #The Input function: Input()
#We use the input fuction for example when we want to enter some data eg.

#print(input('What is your name: '))

#Format:  input("A prompt for the user")

#print('Hello ' + input("What is your name:") + "!")
#We use it to get user input


#Inputs Exercise
#Instructions
#Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
#Warning. Your program should work for different inputs. e.g. any name that you input.
#Example Input

#Angela

#Example Output

#6

#e.g. When you hit run, this is what should happen:
#Hint

#   You can put functions inside other functions.
#    Don't try to print anything other than the length.

#Test Your Code

#Before checking the solution, try copy-pasting your code into this repl:

#https://repl.it/@appbrewery/day-1-3-test-your-code

#This repl includes my testing code that will check if your code meets this assignment's objectives.
#Solution

#https://repl.it/@appbrewery/day-1-3-solution

#In order to get the number of characters in a person's name, we need to use the len() Fuction 


#print( len( input("What is your name? ") ) )

#print(len('Emmanuel'))

#print( len( input("what is you name: ") ) )



              #Python Variabiles
#A variable is a container for values(string, Integers,float and booleen)
#It behaveves as if it was the value it contains
#name = input('What is your name')
#print(name)

#name = input("What is your name? ")
#length = (len(name))
#print(length)

#Coding Exercise Variable
# 🚨 Don't change the code below 👇
#a = input("a: ")
#b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇


#c = a
#a = b
#b = c



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
#print("a: " + a)
#print("b: " + b)

#Naming Variables
#Rules to follow when naming variables
# 1. Make your code readable
# 2. Seperate multiple words in the name of your variale using an underscore eg user_name. You can not have a space in betwwen,it is not valid code!
# 3. Incase you want to number your variables eg, length1, length2 etc, write
#the number at the end of the variable as shown above not at the start - 1length.
#This will result to an error message
# 4, Do not use the names of print functions as variables eg input and print
# 5. Avoid typing errors when using a variable multiple times as it may result to errors


#Day 1 Project Band Name Generator
print('Welcoem to the Band Name Generator')
city = input('What city did you up in?\n')
Pet = input('What is the name of your pet?\n')
print('your band name could be ' + city + ' ' + Pet )








