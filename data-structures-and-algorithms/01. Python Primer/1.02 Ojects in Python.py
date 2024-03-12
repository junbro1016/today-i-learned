# 1.2 Objects in Python
# 1.2.3 Python's Built-In Classes

print(bool()) # False
print(int()) # 0
print(float()) # 0.0
print(0b1011) # 11
print(0o52) # 42
print(0x7f) # 127
print(int('7f',16)) # 127

'''
A list is a referential structure, as it technically stores a sequence of references to its elements.
Lists are array-based sequences and zero-indexed. 
The constructor will accept any parameter that is of an iterable type.
'''
data = [1,2,3,4]
backup = list(data)
data.append(5)
print(data, backup)

'''
The tuple class provides an immutable version of a sequence.
To express a tuple of length one as a literal, a comma must be placed after the element, but within the paranthesis.
'''
print(type((17,))) # tuple
print(type((17))) # int

'''
str class is specifically designed to efficiently represent an immutable sequence of characters.
'''
print('20\u20AC') #20€

'''
set class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without inherent order to those elements.
it has a highly optimized method for checking whether a specific element is contained in the set. 
only instances of immutable types can be added to a python set.
it is possible to maintain a set of tuples, but not a set of lists or set of sets, as list and sets are mutable.
the frozen set class is an immutable form of the set type, so it is legal to have a set of frozensets.  
'''
print(type({})) # dict
print(type(set())) # set
print(set('hello')) # {'e', 'o', 'h', 'l'}
print(frozenset('hello')) # frozenset({'o', 'h', 'l', 'e'})

'''
dict class represents a dictionary, or mapping, from a set of distinct keys to associated values.
the constructor for the dict class accepts an existing mapping as a parameter.
alternatively, the constructor accepts a sequence of key-value pairs as a parameter
'''
print(dict({'hi':'hello', 'bye': 'goodbye'})) # {'hi': 'hello', 'bye': 'goodbye'}
pairs = [('ga','Irish'), ('de','German')]
print(dict(pairs)) # {'ga': 'Irish', 'de': 'German'}
