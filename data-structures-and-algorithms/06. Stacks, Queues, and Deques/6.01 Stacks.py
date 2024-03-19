# 6.1 Stacks
'''
A stack is a colletion of objects that are inserted and removed according to the last-in, first-out principle.
'''
# 6.1.1 The Stack Abstract Data Type
'''
S.push(e): Add element e to the top of stack S. 
S.pop(): Remove and return the top element from the stack S. an error occurs if the stack is empty. 
S.top(): Return a reference to the top element of stack S, without removing it. an error occurs if the stack is empty. 
S.is_empty(): Return True if stack S does not contain any elements. 
len(S): Return the number of elements in stack S; in python, we implement this with the special method __len__.
'''
# 6.1.2 Simple Array-Based Stack Implementation
'''
The Adapter Pattern:

the adapter design pattern applies to any context where we effectively want to modify an existing class so that
its methods match those of a related, but different, class or interface. one general way to apply the adapter pattern
is to define a new class in such a way that it contains an instance of the existing class as a hidden field, and then to
implement each method of the new class using methods of this hidden instance variable.
'''

class Empty(Exception):
    '''Error attempting to access an element from an empty container'''
    pass

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        '''Create an empty stack.'''
        self._data = []

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self._data)
    
    def is_empty(self):
        '''Return True if the stack is empty'''
        return len(self._data) == 0
    
    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._data.append(e)

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]
    
    def pop(self):
        '''Remove and return the element from the top of the stack.
        
        Raise Empty exception if the stack is emtpy.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()

S1 = ArrayStack()
S1.push(5)
S1.push(3)
print(len(S1)) # 2
print(S1.pop()) # 3
print(S1.is_empty()) # False
print(S1.pop()) # 5
print(S1.is_empty()) # True
S1.push(7)
S1.push(9)
print(S1.top()) # 9
S1.push(4)
print(len(S1)) # 3
print(S1.pop()) # 4
S1.push(6)

# 6.1.3 Reversing Data Using a Stack
'''
we might wish to print lines of a file in reverse order in order to display a data set in decreasing order 
rather than increasing order. This can be accomplished by reading each line and pushing it onto a stack,
and then writing the lines in the order they are popped.
'''
def reverse_file(filename):
    '''Overwrite given file with its contents line-by-line reversed.'''
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

# 6.1.4 Matching Parentheses and HTML Tags 
'''
An Algorithm for Matching Delimiters

an important task when processing arithmetic expressions is to make sure their delimiting symbols match up correctly.
'''
def is_matched(expr): # this runs in O(n) time
    '''Return True if all delimiters are properly match; False otherwise'''
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

'''
Matching Tags in a Markup Language
'''
def is_matched_html(raw):
    '''Return True if all HTML tags are properly match; False otherwise.'''
    S = ArrayStack()
    j = raw.find('<')
    while j != '-1':
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()