# How to usedNamedtuples?
# Using namedtuple is way shorter than defining a 
# class manually:
from collections import namedtuple
Phone = namedtuple('Phone', 'model color')
# Our new "Phone" class works as expected:
my_phone = Phone('iPhone10', "black")
print(my_phone.model)
# 'iPhone10'
my_phone.color
# black

# We get a nice string repr for free:
print(my_phone)
# Phone(model='iPhone10', color='black')

# Like tuples, namedtuples are immutable:
my_phone.color = 'white'
# AttributeError: "can't set attribute"


