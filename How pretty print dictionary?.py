# The standard print statement for dicts 
# is hard to read:
custom_dict = {'one': 1, 'two': 2, 'three': 3}
print(custom_dict)
# {'one': 1, 'two': 2, 'three': 3}


# Use "json" module for pretty printing
import json
print(json.dumps(custom_dict, indent=4))
# {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }













