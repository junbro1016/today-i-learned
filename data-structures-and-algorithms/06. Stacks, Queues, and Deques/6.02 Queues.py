# 6.2 Queues
'''
queue is a collection of objects that are inserted and removed according to the first-in, first-out (FIFO) principle.
That is, elements can be inserted at any time, but only the element that has been in the queue the longest can be next removed. 
we usually say that elements enter a queue at the back and are removed from the front.
'''
# 6.2.1 The Queue Abstract Data Type
'''
Q.enqueue(e): add element e to the back of queue Q. 
Q.dequeue(): remove and return the first element from the queue Q; an error occurs if the queue is empty. 
Q.first(): return a reference to the element at the front of queue Q, without removing it; an error occurs if the queue is empty.
Q.is_empty(): return True if queue Q does not contain any elements.
len(Q): return the number of elements in queue Q; in python, we implement this with the special method __len__.
'''
# 6.2.2 Array-Based Queue Implementation
'''
Using an Array Circularly

In developing a more robust queue implementation, we allow the front of the queue to drift rightward, and we allow
the contents of the queue to 'wrap around' the end of an underlying array. when we dequeue an element and want to advance
the front index, we use the arithmetic f = (f+1) % N.
'''
'''
A Python Queue Implementation

_data: is a reference to a list instance with a fixed capacity
_size: is an integer representing the current number of elements stored in the queue (as opposed to the length of the _data list)
_front: is an integer that represents the index within _data of the first element of the queue (assuming the queue is not empty)

Adding Elements

avail = (self._front + self._size) % len(self._data)
for example, consider a queue with capacity 10, current size 3, and first element at index 5.
The three elements of such a queue are stored in indices 5, 6, and 7. 
the new element should be placed at (self._front + self._size) = 8 index.
in a case with wrap-around, the use of the modular arithmetic achieves the desired circular semantics.

Resizing the Queue

while transfering the contents of old list to new list, we intentionally realign the front of the queue with index 0 in the new array.
Since the modular arithmetic depends on the size of the array, our state would be flawed had we transferred each element
to its same index in the new array. 
'''
class Empty(Exception):
    pass

class ArrayQueue:
    '''FIFO queue implementation using a Python list as underlying storage.'''
    DEFAULT_CAPACITY = 10

    def __init__(self):
        '''Create an empty queue'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size
    
    def is_empty(self):
        '''Return True if the queue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return (but not remove) the element at the front of the queue.
        
        Raise Emtpy exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        '''Remove and return the first element of the queue.

        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        '''Add an element to the back of queue.'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        '''Resize to a new list of capacity >= len(self)'''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0