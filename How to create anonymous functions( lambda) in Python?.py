# How to create anonymous function (lambda func)?
# Sometimes, naming a function is not  worth the 
# trouble. e.g - when you’re sure the function 
# will only be used once.

add_two = lambda x: x + 2
print(add_two(3))
# 5

# When you need to use a function as an argument,
# in such cases, the function is often used only once
numbers = [1, 3, 5, 7]
times_three = map(lambda x: x * 3, numbers)
print(list(times_three))
# [3, 9, 15, 21]




