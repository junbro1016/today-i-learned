# 1.8 Iterators and Generators
'''
a file can produce an iteration of its lines. 
an iterator is an object that manages an iteration through a series of values. 
If variable, i, identifies an iterator object, then each call to the built-in function, 'next(i)', produces a subsequent element from the underlying series, with a StopIteration exception raised to indicate that there are no further elements.
An iterable is an object, obj, that produces an iterator via the syntax iter(obj).
by these definitions, an instance of a list is an iterable, but not itself an iterator. 
more generally, it is possible to create multiple iterators based upon the same iterable object, with each iterator maintaining its own state of progress.
'''
data = [1,2,3,4]
i = iter(data)
j = iter(data)
print(next(i)) # 1
print(next(j)) # 1
print(next(i)) # 2
print(next(j)) # 2
print(next(i)) # 3
print(next(j)) # 3
print(next(i)) # 4
print(next(j)) # 4
# print(next(i)) # StopIteration error
# print(next(j)) # StopIteration error
'''
iterators typically maintain their state with indirect reference back to the original collections of elements. 
For example, calling iter(data) on a list instance produces an instance of the 'list_iterator' class.
That iterator does not store its own copy of the list of elements.
Instead, it maintains a current index into the original list, representing the next element to be reported. 
Therefore, if the contents of the original list are modified after the iterator is constructed, but before the iteration is complete, the iterator will be reporting the updated contents of the list.
'''
data = [1,2,3,4]
i = iter(data)
print(next(i)) # 1
print(next(i)) # 2
data[2] = 5
data[3] = 6
print(next(i)) # 5
print(next(i)) # 6
# print(next(i)) # StopIteration error
'''
the call 'range(1000000)' does not return a list of numbers.
it returns a 'range' object that is iterable. 
this object generates the million values one at a time, and only as needed. 
'''
a = range(10000)
r = iter(a)
print(next(r)) # 0
print(next(r)) # 1
print(next(r)) # 2 
'''
Generators:
the most convenient technique for creating iterators in Python is through the use of generators. 
A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a yield statement is executed to indicate each element of the series. 
it is illegal to combine yield and return statements in the same implementation, other than a zero-argument return statement to cause a generator to end its execution. 
a generator cna rely on multiple yield statements in different constructs.
'''
def factors1(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

def factors2(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

def factors3(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k 
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k 

a = factors2(100)
print(next(a)) # 1
print(next(a)) # 2

for f in factors2(10):
    print(f) # 1 2 5 10

for f in factors3(10):
    print(f) # 1 10 2 5 