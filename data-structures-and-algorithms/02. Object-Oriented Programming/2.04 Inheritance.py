# 2.4 Inheritance
'''
there are two ways in which a subclass can differentiate itself from its superclass. 
a subclass may specialize an existing behavior by providing a new implementation that overrides an existing method. 
a subclass may also extend its superclass by providing brand new methods.
'''
# 2.4.1 Extending the CreditCard Class
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

class PredatoryCreditCard(CreditCard):
    '''An extension to CreditCard that compounds interests and fees.'''

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
    
    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.'''
        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        '''Assess monthly interest on outstanding balance'''
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
'''
python does not support formal access control, but names beginning with a single underscore are conventionally akin to protected,
while names beginning with a double underscore (other than special methods) are akin to private. 
'''

# 2.4.2 Hierarchy of Numeric Progressions
'''
a numerice progression is a sequence of numbers, where each number depends on one or more of the previous numbers.
arithmetic progression determines the next number by adding a fixed constant to the previous value,
and a geometric progression determines the next number by multiplying the previous value by a fixed constant.
in general, a progression requires a first value, and a way of identifying a new value based on one or more previous values.
'''
class Progression:
    '''Iterator producing a generic progression.

    Default iterator produces the whole numbers 0,1,2 ...
    '''
    
    def __init__(self, start=0):
        '''Initialize current to the first value of the progression'''
        self._current = start
    
    def _advance(self):
        '''Update self._current to a new value. 

        This should be overridden by a subclass to customize progression. 

        By convention, if current is set to None, this designates the end of a finite progression
        '''
        self._current += 1
    
    def __next__(self):
        '''Return the next element, or else raise StopIteration error'''
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current 
            self._advance()
            return answer
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator'''
        return self
    
    def print_progression(self, n):
        '''Print next n values of the progression'''
        print(' '.join(str(next(self)) for j in range(n)))
    
class ArithmeticProgression(Progression):
    '''Iterator producing an arithmetic progression.'''

    def __init__(self, increment=1, start=0):
        '''Create a new arithmetic progression.

        increment the fixed constant to add to each term
        start     the first term of the progression
        '''
        super().__init__(start)
        self._increment = increment

    def _advance(self): # overriding
        '''Update current value by adding the fixed increment'''
        self._current += self._increment

class GeometricProgression(Progression):
    '''Iterator producing a geometric progression'''

    def __init__(self, base=2, start=1):
        '''Create a new geometric progression.
        
        base      the fixed constant multiplied to each term
        start     the first term of the progression'''

        super().__init__(start)
        self._base = base

    def _advance(self): # overriding
        '''Update current value by multiplying it by the base value'''
        self._current *= self._base

class FibonacciProgression(Progression):
    '''Iterator producing a generalized Fibonacci progression'''

    def __init__(self, first=0, second=1):
        '''Create a new fibonacci progression.
        
        first    the first term of the progression
        second   the second term of the progression'''

        super().__init__(first)
        self._prev = second - first 

    def _advance(self):
        '''Update current value by taking sum of pervious two'''
        self._prev, self._current = self._current, self._current + self._prev

if __name__ == '__main__':
    print('Default Progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5 and start 2: ')
    ArithmeticProgression(5,2).print_progression(10)

    print('Geometric progression with base 3: ')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with start values 4 and 6: ')
    FibonacciProgression(4,6).print_progression(10)

# 2.4.3 Abstract Base Classes
'''
we say a class is an abstract base class if its only purpose is to serve as a base class through inheritance. 
more formally, an abstract base class is one that cannot be directly instantiated, while a concrete class is one that can be instantiated. 
the template method pattern is when an abstract base class provides concrete behaviors that rely upon calls to other abstract behaviors. 
a metaclass is different from a superclass, in that it provides a template for the class definition itself. 
python disallows instantiation for any subclasses that does not override the abstract methods with concrete implementations.
'''
from abc import ABCMeta, abstractmethod 

class Sequence(metaclass=ABCMeta):
    '''Our own version of collections.Sequence abstract base class'''

    @abstractmethod
    def __len__(self):
        '''Return the length of the sequence'''
    
    @abstractmethod
    def __getitem__(self, j):
        '''Return the element at index j of the sequence'''
    
    def __contains__(self, val):
        '''Return True if val found in the sequence; False otherwise'''
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    
    def index(self, val):
        '''Return leftmost index at which val is found (or raise ValueError)'''
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
    
    def count(self, val):
        '''Return the number of elements equal to given value'''
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    