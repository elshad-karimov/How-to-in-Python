# How to swap values of variables in Python?

# Let's say we want to swap the values 
# of x and y...
x = 10
y = 20

# The "classic" way to do it with a temporary 
# variable:
tmp = x
x = y
y = tmp

# Python also lets us use this short-hand:
x, y = y, x




