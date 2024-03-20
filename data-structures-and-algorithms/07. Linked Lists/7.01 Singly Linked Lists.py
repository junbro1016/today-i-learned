'''
there are some notable disadvantages in python list.

    1. the length of a dynamic array might be longer than the actual number of elements that it stores. 
    2. Amortized bounds for operations may be unacceptable in real-time system. 
    3. Insertions and deletions at interior positions of an array are expensive.

'linked list' provides an alternative to an array-based sequence (such as a python list).
a linked list reliese on a more distributed representation known as a node. 
each node maintains a reference to its element and one or more references to neighboring nodes in order to collectively
represent the linear order of the sequence. elements of a linked list cannot be efficiently accessed by a numeric index, k,
and we cannot tell just by examining a node if it is the second, fifth, or twentieth node in the list. however, linked list
avoid the three disadvantages noted above for array-based sequences. 
'''
# 7.1 Singly Linked Lists
'''
A 'singly linked list' is a collection of nodes that collectively form a linear sequence. each node stores a reference to
an object that is an element of the sequence, as well as a reference to the next node of the list.
the first and last node of a linked list are known as the head and tail of the list, respectively.
'''
# 7.1.1 Implementing a Stack with a Singly Linked List
'''
we need to decide whether to model the top of the stack at the head or at the tail of the list. 
there is clearly a best choice here; we can efficiently insert and delete elements in constant time only at the head.
since all stack operations affect the top, we orient the top of the stack at the head of our list.
'''
class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''
    #--------------------------------nested _Noed class----------------------------------------------
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element
            self._next = next
    #-------------------------------------stack methods----------------------------------------------
    def __init__(self):
        '''Create an empty stack.'''
        self._head = None
        self._size = 0
    
    def __len__(self):
        '''Return the number of elements in the stack'''
        return self._size
    
    def is_empty(self):
        '''Return True is the stack is empty'''
        return self._size == 0
    
    def push(self, e):
        '''Add element e to the top of the stack'''
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        '''Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        '''
        if self._size == 0:
            raise Exception('stack is empty')
        return self._head._element
    
    def pop(self):
        '''Remove and return the element from the top of the stack
        
        Raise Empty exception if the stack is empty.
        '''
        if self._size == 0:
            raise Exception('stack is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result

# 7.1.2 Implementing a Queue with a Singly Linked List
'''
the natural orientation for a queue is to align the front of the queue with the head of the list,
and the back of the queue with the tail of the list, because we must be able to enqueue elements at the back,
and dequeue them from the front. 
'''
class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''
    #--------------------------------nested _Noed class----------------------------------------------
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element
            self._next = next
    #-------------------------------------queue methods----------------------------------------------
    def __init__(self):
        '''Create an empty queue'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size
    
    def is_empty(self):
        '''Return True if the queue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return (but not remove) the element at the front of the queue'''
        if self.is_empty():
            raise Exception('queue is empty')
        return self._head._element
    
    def dequeue(self):
        '''Remove and return the first element of the queue.
        
        Raise Empty Exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        '''Add an element to the back of the queue.'''
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1