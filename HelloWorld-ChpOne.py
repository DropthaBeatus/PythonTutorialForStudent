# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Hello I got a few subjects we can work with this will be just a baseline help for you
#TODO: Reading materiral:

#Intro  (Optional)
#https://www.tutorialspoint.com/python/python_overview.htm

#Variable Types (Recommended)
#https://www.tutorialspoint.com/python/python_variable_types.htm

#Pass by value vs Pass by reference  (Optional)
#https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/

#TODO: Practice
#Create a two functions one that prints out a String and one that returns a value
#The program should do some basic arthimetic (Add, Subtract, etc idc)
#For old time sakes make sure your program prints out 'Hello World' as an output
#Boring I know.... We just need to do some Wax-on, Wax-off for the first week

#Below here is a function
#You define a function with the keyword 'def'. This function is called 'greeting'
#This function contains a parameter. This parameter is called name. We will pass a String
#A String is a combination of characters. Basically any text num or chars. E.g. 'Hello' is a string
def greeting(name):
    # We have a function below called print we do not have to create this function as it is stored within the Python library
    #The function print will display any String that is passed into it our case is name.
    #Any indented lines will be process when the function is called. To end the function simply do not indent your lines
    print(name)


#Pass by Value
def changeVariableValue(info):
    #pass by reference
    print('Value inside the function: ', info)
    info = 'This is the third line'
    print('Value inside the function: ', info)

#Pass by Reference
def changeVariableValueID(info):
    #pass by reference
    print('Value inside the function: ', info, id(info))
    info = 'This is the sixth line'
    print('Value inside the function: ', info, id(info))

#if you would like to keep the value in the function we can return it
def changeVariableValueReturn(info):
    #pass by reference
    print('Value inside the function: ', info, id(info))
    info = 'This is the tenth line'
    print('Value inside the function: ', info, id(info))

#return the funciton by calling return and put the variable after it
#Even though we return the value we will still need to assign it to a variable
    return info









#TODO: The code will start running below
#Why?
#because reads code from top to down but goes by tiers of if the code is indented or not
#Even though functions names above are not indented the compiler will ignore it since the def keyword defines the programs as a function
#This also means the code will not run the indented code unless a certain criteria is meet such as calling the function above

#We create a String variable called greet. This variable will contain the value 'Hello World'
#This is a basic way to describe how this works if you want a more advance explanation just ask
greet = 'Hello World'

#We call the function greeting and pass the value 'Hello World'. This will then print the value onto the screen once we run the program
greeting(greet)

info = 'This is the second line'
changeVariableValue(info)
#So the function above should change the variable correct? Since we assign the variable info a new value in the changeVariableValue function.
#Will the value change?
print('Value outside the function: ', info, "\n")
#You'll notice that the value 'This is the second line' remains.
# That is because the change was made in the function changeVariableValue's scope and we actually pass the variables value.
#THINK ABOUT IT AS COPYING OVER THE VALUE AND PASSING IT TO THE FUNCTION
#If you would like to find out where the variable is stored call the function id()
# So the changes will not be applied out the function



#We redo this again but this time call the value's id aka location of where the value is store in memory
info = "This is the fifth line"
changeVariableValueID(info)
print('Value outside the function: ', info, id(info), "\n")

#notice when we change the value of the function it is then copied over to a new location with a new value

#What happens if we change the value of the variable within this scope of the function
info = "This is the eighth line"
print('Value outside the function: ', info, id(info), "\n")
#The id also changes interesting....

info = "This is the ninth line"

#This time we call a similar function but we will return the changed value and assign it to the 'info' variable
info = changeVariableValueReturn(info)
#This time the variable will actually change its value
#Lets also find out the id of the value
print('Value outside the function: ', info, id(info), "\n")
#The id stays the same... Is this because they share the same value?




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
