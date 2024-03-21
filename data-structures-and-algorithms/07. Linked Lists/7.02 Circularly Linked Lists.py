# 7.2 Circularly Linked Lists
'''
in the case of linked lists, there is a more tangible notion of a circularly linked list,
as we can have the tail of the list use its next reference to point back to the head of the list.
we call such a structure a circularly linked list.

a circularly linked list provides a more general model than a standard linked list for data sets that are cyclic, that is,
which do not have any particular notion of a beginning and end. even though a circularly linked list has no beginning 
or end, per se, we must maintain a reference to a particular node in order to make use of the list.
'''

# 7.2.1 Round-Robin Schedulers
'''
a round-robin schedular could be implemented with the general queue ADT, by repeatedly performing the following steps on queue Q.
    1. e = Q.dequeue()
    2. Service element e
    3. Q.enqueue()

if using a circularly linked list,
    1. Service element Q.front()
    2. Q.rotate()
'''

# 7.2.1 Implementing a Queue with a Circularly Linked List
class CircularQueue:
    '''Queue implementation using circularly linked list for storage.'''
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element
            self._next = next
    
    def __init__(self):
        '''Create an empty queue'''
        self._tail = None
        self._size = 0
    
    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size
    
    def is_empty(self):
        '''Return True if the queue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        '''Return and remove the element at the front of the queue
        
        Raise exception if the queue is empty.
        '''
        if self.is_empty():
            raise Exception('queue is empty')
        
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        '''Add an element to the back of the queue'''
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        '''Rotate front element to the back of the queue.'''
        if self._size > 0:
            self._tail = self._tail._next




