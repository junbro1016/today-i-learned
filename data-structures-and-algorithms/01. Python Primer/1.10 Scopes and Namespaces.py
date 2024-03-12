# 1.10 Scopes and Namespaces
'''
the process of determining the value associated with an identifier is known as name resolution.
each distinct scope in python is represented using an abstraction known as a namespace.
python implements a namespace with its own dictionary that maps each identifying string to its associated value. 
'dir' reports the name of the identifiers in a given namespace.
'vars' returns the full dictionary. 
when an identifier is indicated in a command, python searches a series of namespaces in the process of name resolution. 
first, the most locally enclosing scope is searched for a given name. 
if not found there, the next outer scope is searched, and so on. 
'''
a = 1
b = 2
print(dir())
print(vars())
'''
in the terminology of programming languages, 'first-class-objects' are instances of a type that can be assigned to an identifier, passed as a parameter, or returned by a function. 
int and list, are clearly first-class types in python. 
in python, functions and classes are also treated as first-class objects. 
'''
scream = print # define scream as an alias for the existing print function
scream('hello') # hello
print('hello') # hello