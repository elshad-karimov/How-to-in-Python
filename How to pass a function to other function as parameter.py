# How to pass a function to other functions as parameter?


# Create bark function which converts text to uppercase
def bark(text):
  return text.upper() + '!'


#Create second function which takes bark as a parameter 
def greet(func):
  greeting = func('Hi, I am a function passed in parameter') 
  print(greeting)

# Call greet function with bark function as parameter
greet(bark)

# Output
# HI, I AM A FUNCTION PASSED IN PARAMETER!








