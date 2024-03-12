# 1.7 Exception Handling
# 1.7.1 Raising an Exception
'''
How much error-checking to perform within a function is a matter of debate.
Checking the type and value of each parameter demands additional execution time and, if taken to an extreme, seems counter to the nature of Python.
'''
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    # do the real work here ... 
def sum(values):
    total = 0
    for v in values:
        total = total + v
    return total

#1.7.2 Catching an Exception
'''
the relative advantage of using a try-except structure is that the none-exceptional case runs efficiently, without extraneous checks for the exceptional condition.
however, handling the exceptional case requires slightly more time when using a try-except structure than with a standard conditional statement.
for this reason, the try-except clause is best used when there is reason to believe that the exceptional case is relatively unlikely, or when it is prohibitively expensive to proactively evaluate a condition to avoid the exception.
if we want to handle two or more types of errors in the same way, we can use a single except-statement.
in order to provide different responses to different types of errors, we may use two or more except-clauses as part of a try-structure. 
'''
age = -1
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    except (ValueError, EOFError):
        print('Invalid resoponse')
        pass # do nothing, yet it can serve syntatically as a body of a control structure

age = -1
while age <= 0:
    try:
        age = int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive')
    except ValueError:
        print('That is an invalid age specification')
    except EOFError:
        print('There was an unexpected error reading input.')
        raise # uses the raise statement without any subsequent argument, to re-raise the same exception that is currently being handled

'''
it is permissible to have a final except-clause without any identified error types, using syntax 'except:', to catch any other exceptions that occured. 
a try-statement can have a finally clause, with a body of code that will always be executed in the standard or exceptional cases, even when an uncaught or re-raised exception occurs.
that block is typically used for critical cleanup work, such as closing an open file.
'''
