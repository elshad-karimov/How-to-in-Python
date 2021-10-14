# How to merge two dictionaries in Python 3.5+

x = {'one': 1, 'two': 2}
y = {'three': 3, 'four': 4}

z = {**x, **y}

# Output
{'one': 1, 'two': 2, 'three': 3, 'four': 4}

