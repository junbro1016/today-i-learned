# 5.3 Dynamic Arrays and Amortization
'''
because the system might dedicate neighboring memory locations to store other data, 
the capacity of an array cannot trivially be increased by expanding into subsequent cells.

python relies on an algorithmic sleight of hand known as a 'dynamic array'. 
the first key to providing the semantics of a dynamic array is that a list instance maintains an underlying array 
that often has greater capacity than the current length of the list. 
if user continues to append elements to a list, any reserved capacity will eventually be exhausted. 
in that case, the class request new, larger array from the system, and initializes the new array so that 
its prefix matches that of the existing smaller array. 

'getsizeof' function reports the number of bytes that are being used to store an object in python.
for a list, it reports the number of bytes devoted to the array and other instance variables of the list, 
but not any space devoted to elements referenced by the list. 
'''
import sys
data = []
for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size of bytes: {1:4d}'.format(a,b))
    data.append(None)
'''
although we cannot directly access private instance variables for a list,
we can speculate that in some form it maintains state information akin to:

_n : the number of actual elements currently stored in the list.
_capacity: the maximum number of elements that could be stored in the currently allocated array
-A: the reference to the currently allocated array (initially None)
'''
# 5.3.1 Implementing a Dynamic Array
'''
if an element is appended to a list at a time when the underlying array is full, we perform the following rules: 
    1. allocate a new array B with larger capacity
    2. Set B[i] = A[i] for 0, ... , n-1, where n denotes current number of items
    3. Set A = B, that is, we henceforth use B as the array supporting the list. 
    4. Insert the new element in the new array.
the remaining issue to consider is how large of a new array to create.
a commonly used rule is for the new array to have twice the capacity of the existing array that has been filled. 
'''
import ctypes

class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init(self):
        '''Create an empty array.'''
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array
    
    def __len__(self):
        '''Return number of elements stored in the array.'''
        return self._n
    
    def __getitem__(self, k):
        '''Return element at index k.'''
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                              # retrieve from array
    
    def append(self, obj):
        '''Add object to end of the array'''
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        '''Resize internal array to capacity C.'''
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self, c):
        '''Return new array with capacity c.'''
        return (c * ctypes.py_object)()               # see ctypes documentation
    
# 5.3.2 Amortized Analysis of Dynamic Arrays
'''
to perform an amortized analysis, we use an accounting technique where we view the computer as a coin-operated
appliance that requires the payment of one cyber-dollar for a constant amount of computing time. 
when an operation is executed, we should have enough cyber-dollars available in our current 'bank account' to pay
for that operation's running time. 
the beauty of this analysis method is that we can overcharge some operations in order to save up cyber-dollars to pay for others. 

Let us assume that one cyber-dollar is enough to pay for the execution of each append operation in S,
excluding the time spent for growing the array. Also, let us assume that growing the array from size k to size 2k 
requires k cyber dollars for the time spent initializing the new array. We shall charge each append operation
three cyber-dollars. Thus, we overcharge each append operation that does not cause an overflow by two cyber-dollars. 
Think of the two cyber-dollars profited in an insertion that does not grow the array as being 'stored' with the cell
in which the element was inserted. An overflow occurs when the array S has 2^i elements, for some integer i >= 0, and 
the size of the array used by the array representing S is 2^i. Thus, doubling the size of the array will require
2^i cyber-dollars. Fortunately, these cyber-dollars can be found stored in cells 2^(i-1) through 2^i -1. Note that the
previous overflow occured when the number of elements became larger than 2^(i-1) for the first time, and thus the
cyber-dollars stored in cells 2^(i-1) through 2^i-1 have not yet been spent. Therefore, we have a valid amortization
scheme in which each operation is charged three cyber-dollars and all the computing time paid for. That is, we can pay 
for the execution of n append operation using 3n cyber dollars. In other words, the amortized running time of each append
operation is O(1); hence, the total running time of n append operations is O(n). 
'''
# 5.3.3 Python's List Class
'''
A careful examination of the intermediate array capacities suggests that python is not using a pure geometric progression,
nor is it using an arithmetic progression. with that said, it is clear that python's implementation of the append method
exhibits amortized constant-time behavior.

we can get a more accurate measure of the amortized cost per operation by performing a series of n append operations on 
an initially empty list and determining the average cost of each. 
'''
from time import time
def compute_average(n):
    '''Perform n appends to an empty list and return average time elapsed.'''
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

for i in range(1,100000000,10000000):
    print(f'Append {i} times in {compute_average(i)} seconds.')
    print()
'''
it seems clear that the amortized time for each append is independent of n. 
'append' operation takes O(1) amortized time.
'''

    
