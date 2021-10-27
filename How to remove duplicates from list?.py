# How to remove duplicates from List?

# Most straightforward approach to removing duplicates 
# in a list is probably using the set() function. 
# Because in Set the values are unique.

# Sample list
my_list = [1,2,3,2,1,2,3,4,5,4,5,3,1]

# Create set from list
my_set = set(my_list)

# Then override the my_list with new list from Set

my_list = list(my_set)
print(my_list)
# [1, 2, 3, 4, 5]







