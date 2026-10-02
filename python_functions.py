# A function is a block of code which only runs when it is called.
# You can pass data , known as parameters , into a function.
#A function can return data as a result 


# Creating a Function 
# Example 
def my_function():
    print("Hello from a function")

#Calling a Function 
#To call a function , use the function name followed by parenthesis 
#Example : 
def my_function():
    print("Hello from a Function")

#Parameters

def my_function(fname):
    print(fname +"Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Default Parameter value 

def my_function(country="Norway"):print("I am from "+ country)

my_function("Sweden")
my_function()


# Passing a list as a parameter 

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana","cherry"]
my_function(fruits)


# Return values 

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))


# keyword Arguments

def my_function(child3,child2,child1):
    print("The youngest child is " + child3)
my_function(child1="Email",child2="Tobias",child3 = "Linus")
