# How to unpack function arguments?

def my_func(a, b, c):
    print(a, b, c)

# create tuple or dictionary
my_tuple = (1, 0, 1)
my_dict = {'a': 1, 'b': 0, 'c': 1}

# Pass them as argument to the function
my_func(*my_tuple)
# 1, 0, 1

my_func(**my_dict)
# 1, 0, 1




