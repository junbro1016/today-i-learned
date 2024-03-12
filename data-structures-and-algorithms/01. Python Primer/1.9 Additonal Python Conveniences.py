# 1.9 Additional Python Conveniences
# 1.9.1 Conditional Expressions
'''
conditional expressions:
'expr1 if condition else expr2' == 'condition ? expr1 : expr2' 
'''

# 1.9.2 Comprehension Syntax
'''
produce one series of values based upon the processing of another series. 

'[expression for value in iterable if condition]'

note that both expression and condition may depend on value, and the if-clause is optional. 

'result = []
for value in iterable:
    if conditon:
        result.append(expression)'
'''
factors1 = [k for k in range(1,101) if 100 % k == 0] # list comprehension
factors2 = {k for k in range(1,101) if 100 % k == 0} # set comprehension
factors3 = (k for k in range(1,101) if 100 % k == 0) # generator comprehension
factors4 = {k : k for k in range(1,101) if 100 % k == 0} # list comprehension
print(next(factors3)) # 1
print(next(factors3)) # 2
print(next(factors3)) # 4
print(next(factors3)) # 5
print(next(factors3)) # 10 
print(type(factors3)) # <class 'generator'>
print(factors4) # {1: 1, 2: 2, 4: 4, 5: 5, 10: 10, 20: 20, 25: 25, 50: 50, 100: 100}

# 1.9.3 Packing and Unpacking of Sequences
'''
python provides two additional conveniences involving the treatment of tuples and other sequence types.
if a series of comma-seperated expressions are given in a larger context, they will be treated as a single tuple, even if no enclosing parentheses are provided.
this behavior is called automatic packing of a tuple. 
'''
data = 2,4,6,8
print(data) # (2,4,6,8)
print(type(data)) # <class 'tuple'>
'''
python can automatically unpack a sequence, allowing one to assign series of individual identifiers to the elements of sequence.
for this syntax, the right-hand side expression can be any iterable type, as long as the number of variables on the left-hand side is the same as the number of elements in the iteration.
'''
a,b,c,d = range(7,11)
print(a,b,c,d) # 7 8 9 10
'''
simultaneous assignments:
we explicitly assign a series of values to a series of identifiers, using a syntax:
'x,y,z = 6,2,5' 
when using a simultaneous assignment, all of the expressions are evaluated on the right-hand side before any of the assignments are made to the left-hand variables.
this is significant, as it provides a convenient means for swapping the values associated with two variables: 
'j,k = k,j'
'''
a,b = 1,2
print(a,b) # 1 2
a,b = b,a
print(a,b) # 2 1

a = [0,0,0,0]
i, a[i], i, a[i] = range(4)
print(a) # [1,0,3,0]

def fib():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b
