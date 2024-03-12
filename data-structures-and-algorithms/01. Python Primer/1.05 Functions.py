# 1.5 Functions
'''
function is a traditional, stateless function that is invoked withoust the context of a particular class or an instance of that class.
method is a member function that is invoked upon a specific object using an object-oriented message passing syntax.
the first line, beginning with the keyword 'def', serves as the funtion's signature.
each time a function is called, python creates a dedicated 'activation record' that stores information relevant to the current call.
this activation record includes what is known as a namespace to manage all identifiers that have local scope within the current call.
the namespace includes the function's parameters and any other identifiers that are defined locally within the body of the function.
an identifier in the local scope of the function caller has no relation to any identifier with the same name in the caller's scope (although identifiers in different scopes may be aliases to the same object).
'''

'''
if a return statement is executed without an explicit argument, the None value is automatically returned.
likewise, None will be returned if the flow of control ever reaches the end of a function body without having executed a return statement. 
'''

# 1.5.1 Information Passing
'''
in the context of a function signature, the identifiers used to describe the expected parameters are known as formal parameters. 
the object sent by the caller when invoking the function are the actual parameters. 
parameter passing in python follows the semantics of the standard assignment statement. 
when a function is invoked, each identifier that serves as a formal parameter is assigned to the respective actual parameter.
an advantage to python's mechanism for passing information to and from a function is that objects are not copied. 
this ensures that the invocation of a function is efficient, even in a case where a parameter or return value is a complex object.
'''
def count(data, target):
    # data = scores
    # target = 1
    n = 0
    print(data is scores) # True
    for item in data:
        if item == target:
            n += 1 
    return n

scores = [1,1,2,3,23,4,34,35,5]
print(count(scores, 1)) # 2

'''
because the formal parameter is an alias for the actual parameter, the body of the function may interact with the object in ways that change its state.
note that reassigning a new value to a formal parameter with a function body, such as data = [], does not alter the actual parameter; such a reassignment simply breaks the alias.
'''
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
nums = [1,2,3,4,5]
print(nums) # [1,2,3,4,5]
scale(nums, 2)
print(nums) # [2,4,6,8,10]

'''
it is illegal to define a function with as signature such as bar(a, b=15, c) with b having a default value, yet not the subsequent c.
if a default parameter value is present for one parameter, it must be present for all further parameters.

def foo(a, b=1,c=2): --> legal
def foo(a, b=1, c): --> illegal

range(start, stop, step)
range(b) 
range(a,b)
range(a,b,2)

this combination of forms seems to violate the rules for default parameters.
however, this effect can be achieved with some sleight of hand, as follows:
'''
def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

'''
the traditional mechanism for matching the actual parameters sent by a caller, to the formal parameters declared by the function signature is based on the concept of positional arguments.
python supports an alternate mechanism for sending a parameter to a function known as a keyword arguement. 
'''
# 1.5.2 Python's Built-In Functions
'''
all(iterable) : return True if bool(e) is True for each element e
any(iterable) : return True if bool(e) is True for at least one element e
divmod(x,y) : return (x//y, x%y) as tuple, if x and y are integers
hash(obj) : return an integer hash value for the object
id(obj) : return the unique integer serving as 'identity' for the object
isinstance(obj, cls) : determine if obj is an instance of the class (or a subclass)
iter(iterable) : return a new iterator object for the parameter
next(iterator) : return the next element reported by the iterator
open(filename, mode) : open a file with the given name and access mode
pow(x,y) : equivalent ot x ** y
pow(x,y,z) : return the value (x ** y % z) as an integer
'''
print(divmod(34.5,3.6)) # (9.0, 2.099999999999999)
a = 1
print(id(1)) # 4315294000
print(id(a)) # 4315294000
