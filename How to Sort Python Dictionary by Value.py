# How to sort a Python dict by value

my_dict = {'four': 4, 'three': 3, 'two': 2, 'one': 1}

sorted(my_dict.items(), key=lambda x: x[1])
# [('one', 1), ('two', 2), ('three', 3), ('four', 4)]


# Or:


import operator
sorted(my_dict.items(), key=operator.itemgetter(1))
# [('one', 1), ('two', 2), ('three', 3), ('four', 4)]

