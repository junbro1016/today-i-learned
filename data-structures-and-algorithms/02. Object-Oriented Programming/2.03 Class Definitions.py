# 2.3 Class Definitions
# 2.3.1 Example
class CreditCard:
    '''A consumer credit card'''
    def __init__(self, customer, bank, acnt, limit):
        '''Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer
        bank     the name of the bank
        acnt     the account identifier
        limit    credit limit
        ''' 
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        '''Return name of the customer'''
        return self._customer
    def get_bank(self):
        '''Return the bank's name'''
        return self._bank
    def get_account(self):
        '''Return the card identifying number'''
        return self._account
    def get_limit(self):
        '''Return current credit limit'''
        return self._limit
    def get_balance(self):
        '''Return current balance'''
        return self._balance
    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied. 
        '''
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        '''Process customer payment that reduces balance.'''
        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
'''
encapsulation:
by the conventions, a single leading underscore in the name of a data member, such as '_balance' implies that it is intended as nonpublic.
users of a class should not directly access such members. 
'''

# 2.3.2 Operator Overloading and Python's Special Methods
'''
operator overloading:
operator overloading is done by implementing a specially named method.
in particular, the + operator is overloaded by implementing a method named '__add__', which takes the right-hand operand as a parameter and which returns the result of the expression.
that is, the syntax, a+b, is converted to a method call on object of the form a.__add__(b). 
when a binary operator is applied to two instances of different types, as in 3 * 'love me', python gives deference to the class of the left operand. 
however, if that class does not implement such a behavior, python checks the class definition for the right-hand operand, in the form of a special method named '__rmul__' (or __radd__, __rsub__, ...)

non-operator overloads: 
python relies on specially named methods to control the behavior of various other functionality, when applied to user-defined classes.
for example, the syntax str(foo) is formally a call to the constructor for the string class.
of course, if the parameter is an instance of a user defined class, the original authors of the string class could not have know how that instance should be portrayed.
so the string constructor calls a specially named method, foo.__str__(), that must return an appropriate string representation.
similar special methods are used to determine how to construct an int, float, or bool based on a parameter from a user-defined class.

implied methods: 
there are some operators that have default definitions provided by python, in the absence of special methods, and there are some operators whose definitions are derived from others.
for example, the __bool__ method, which supports the syntax 'if foo:' has default semantics so that every object other than None is evaluated as True.
however, for container types, the __len__ method is typically defined to return the size of the container. 
if such a method exists, then the evaluation of bool(foo) is interpreted by default to be True for instances with nonzero length, and False for instances with zero length.
'''

# 2.3.3 Example: Multidimensional Vector Class
class Vector:
    '''Represent a vector in a multidimensional space.'''
    def __init__(self, d):
        '''Create d-dimensional vector of zeros.'''
        self._coords = [0] * d
    def __len__(self):
        '''Return the dimension of the vector'''
        return len(self._coords)
    def __getitem__(self, j):
        '''Return jth coordinate of vector'''
        return self._coords[j]
    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value'''
        self._coords[j] = val
    def __add__(self, other):
        '''Return sum of two vectors'''
        if len(self) != len(other): # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        '''Return True if vector has same coordinates as other'''
        return self._coords == other._coords
    def __ne__(self, other):
        '''Return True if vector differs from other'''
        return not self == other # relies on existing __eq__definition
    def __str__(self):
        '''Produce string representation of vector'''
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation

if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23 # based on the use of __setitem__
    v[-1] = 45 # based on the use of __setitem__
    print(v[4]) # via __getitem__
    u = v + v # via __add__
    print(u)
    total = 0
    for entry in v:
        total += entry # implicit iteration via __len__ and getitem
    print(total)

# 2.3.4 Iterators
'''
an iterator for a collection provides one key behavior: it supports a special method named __next__ that returns the next element of the collection, if any, or raises a StopIteration exception to indicate that there are no further elements. 
our preferred appraoch is the use of the generator syntax, which automatically produces an iterator of yielded values. 
python also helps by providing an automatic iterator implementation for any class that defines both __len__ and __getitem__.
'''
class SequenceIterator:
    '''An iterator for any of Python's sequence types'''
    
    def __init__(self, sequence):
        '''Create an iterator for the given sequence.'''
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return (self._seq[self._k]) # return the data element
        else:
            raise StopIteration() # there are no more elements
        
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self
    
# 2.3.5 Example: Range Class 
class Range:
    '''A class that mimic's the built-in range class'''
    def __init__(self, start, stop=None, step=1):
        '''Initialize a Range instance.

        Semantics is similar to built-in range class
        '''
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem
        self._start = start
        self._step = step

    def __len__(self):
        '''Return number of entries in the range.'''
        return self._length
    
    def __getitem__(self, k):
        '''Return entry at index k (using standard interpretation if negative).'''
        if k < 0:
            k += len(self) # attempt to convert negative index
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step