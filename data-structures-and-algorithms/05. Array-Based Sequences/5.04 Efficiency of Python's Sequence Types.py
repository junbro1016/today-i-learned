# 5.4 Efficiency of Python's Sequence Types
# 5.4.1 Python's List and Tuple Class
'''
Adding Elements to a List:

insert method
there are two complicating factors in analyzing the efficiency of such an operation.
first, we note that the addition of one element may require a resizing of the dynamic array, that portion of work 
requires omega n worst-case time but only O(1) amortized time, as per append. The other expense for insert is the
shifting of elements to make room for the new item. Overall this leads to an amortized O(n-k+1) performance.
'''
def insert(self, k, value):
    '''Insert value at index k, shifting subsequent values rightward.'''
    # (for simplicity, we assume 0 <= k <= n in this version)
    if self._n == self._capacity:
        self._resize(2 * self._capacity)
    for j in range(self._n,k,-1):
        self._A[j] = self._A[j-1]
    self._A[k] = value
    self._n += 1

from time import time
def compute_average_first(n):
    data = []
    start = time()
    for k in range(n):
        data.insert(0,None)
    end = time()
    return (end - start) / n

def compute_average_mid(n):
    data = []
    start = time()
    for k in range(n):
        data.insert(n//2, None)
    end = time()
    return (end - start) / n

def compute_average_last(n): # akin to append
    data = []
    start = time()
    for k in range(n):
        data.insert(n, None)
    end = time()
    return (end - start) / n

print(f'k = 0 insertion takes {compute_average_first(100000)} times.') # requires linear time
print(f'k = n//2 insertion takes {compute_average_mid(100000)} times.')
print(f'k = n insertion takes {compute_average_last(100000)} times.')

'''
Removing Elements from a List: 

there is no efficient case for 'remove'; every call requires omega n time. 
one part of the process reaches from the beginning until finding the value at index k,
while the rest iterates from k to end in order to shift elements leftward.
'''
def remove(self, value):
    '''Remove first occurence of value (or raise ValueError)'''
    # note: we do not consdier shrinking the dynamic array in this version
    for k in range(self._n):
        if self._A[k] == value:
            for j in range(k, self._n-1):
                self._A[j] = self._A[j+1]
            self._A[self._n-1] = None
            self._n -= 1
            return
        raise ValueError('value not found')
    
'''
Extending a List: 

in effect, a call to data.extend(other) produces the same outcome as the code,

for element in other:
    data.append(element)

in either case, the running time is proportional to the length of the other list,
and amortized because the underlying array for the first list may be resized to accomodate the additional elements.
in practice, the 'extend' method is preferable to repeated calls to append because the constant factors hidden in the
asymptotic analysis are significantly smaller. 

1. there is always some advantage to using an appropriate python method, because those methods are often implemented natively in compiled language.
2. there is less overhead to a single function call that accomplishes all the work, versus many individual function calls. 
3. the resulting size of the updated list can be calculated in advance.
'''

'''
Constructing New Lists:

experiments should show that the list comprehension syntax is significantly faster than building the list by repeatedly appending. 
Similarly, it is a common Python idiom to initialize a list of constant values using the multiplication operator,
as in [0] * n to produce a list of length n with all values equal to zero. 
Not only this succint for the programmer, it is more efficient than building such a list incrementally.
'''

# 5.4.2 Python's String Class
'''
Compose Strings:

assume that we have a large string 'document' and our goal is to produce a new string, 'letters' that contains only the
alphabetic characters of the original string. 
first code is terribly inefficient. Because strings are immutable, the command, letters += c, would presumably compute the
concatenation , letters + c, as a new string instance and then reassign the identifier, letters, to that result.
This will take O(n^2) times.

a more standard python idiom to guarantee linear time composition of a string is to use a temporary list to store individual pieces,
and then to rely on the join method of the str class to compose the final result. this runs in O(n) time. 

we can further improve the practical execution time by using a list comprehension syntax to build up the temporary list,
rather than by repeated calls to append.
'''
# WARNING: do not do this
letters = ''
document = 'adsfawega40349uqjorgi af 49t jqori jf'
for c in document: 
    if c.isalpha():
        letters += c

# Do like this
temp = []
for c in document:
    if c.isalpha():
        temp.append(c)
    letters = ''.join(temp)

# Better
letters = ''.join([c for c in document if c.isalpha()]) # list comprehension
letters = ''.join(c for c in document if c.isalpha())   # generator comprehension