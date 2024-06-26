
class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation'''
    
    class _Node:
        '''Lightweight, nonpublic class for storing a doubly linekd node.'''
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        '''Create an empty list'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the list'''
        return self._size
    
    def is_empty(self):
        '''Return True if list is empty'''
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None # deprecate, help garbage collection
        return element

class PositionalList(_DoublyLinkedBase):
    '''A sequential conatiner of elements allowing positional access'''
    
    #--------------------------------nested Position class-------------------------------------
    class Position:
        '''An abstraction representing the location of a single element'''
        def __init__(self, container, node):
            '''Constructor should not be invoked by user'''
            self._container = container
            self._node = node
        
        def element(self):
            '''Return the element stored at ths Position'''
            return self._node._element
        
        def __eq__(self, other):
            '''Return True if other is a Position representing the same location'''
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not(self == other)
        
    #--------------------------------utility method-------------------------------------
    def _validate(self, p):
        '''Return position's node, or raise appropriate error if invalid'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._conatiner is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                                 # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        '''Return Position instance for given node (or None if sentinel)'''
        if node is self._header or self._trailer:
            return None
        return self.Position(self, node)

    #--------------------------------accessors-------------------------------------
    def first(self):
        '''Return the first Position in the list (or None if list is empty)'''
        return self._make_position(self._header._next)

    def last(self):
        '''Return the last Position in the list (or None if list is empty)'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''Return the Position just before Position p (or None is p is first)'''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        '''Return the Position just after Position p (or None if p is last)'''
        node = self._validate(p)
        return self._make_position(node._next)

    def iter(self):
        '''Generate a forward iteration of the elements of the list'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    #--------------------------------mutators-------------------------------------
    # override inherited version to return Position, rather than Node 
    def _insert_between(self, e, predecessor, successor):
        '''Add element between existing nodes and return new Position'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        '''Insert element e at the front of the list and return new Position'''
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''Insert element e at the back of the list and return new Position'''
        self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        '''Insert element e into list before Position p and return new Position'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''Insert element e into list after Position p and return new Position'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''Remove and return the element at Position p'''
        delete = self._validate(p)
        self._delete_node(delete)

    def replace(self, p, e):
        '''Replace the element at Position p with e.
        
        Return the element formerly at Position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

# 9.2.1 The Composition Design Patterns
class PriorityQueueBase:
    '''Abstract base class for a priority queue'''

    class _Item:
        '''Lightweight composite to store priority queue items'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __It__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        '''Return true if the priority queue is empty'''
        return len(self) == 0
    
# 9.2.2 Implementation with an Unsorted List
class UnsortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with an unsorted list'''

    def _find_min(self): # nonpublic utility
        '''Return Position of item with minimum key'''
        if self.is_empty():
            raise KeyError('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk 
            walk = self._data.after(walk)
        return small
    
    def __init__(self):
        '''Create a new empty Priority Queue'''
        self._data = PositionalList()

    def __len__(self):
        '''Return the number of items in the priority queue'''
        return len(self._data)
    
    def add(self, key, value):
        '''Add a key-value pair'''
        self._data.add_last(self._Item(key, value))

    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key'''
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        '''Remove and return (k,v) tuple with minimum key'''
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

class SortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with a sorted list'''

    def __init__(self):
        '''Create a new empty Priority Queue'''
        self._data = PositionalList()

    def __len__(self):
        '''Return the number of items in the priority queue'''
        return len(self._data)
    
    def add(self, key, value):
        '''Add a key-value pair'''
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self.data.add_after(walk, newest)

    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key'''
        if self.is_empty():
            raise KeyError
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        '''Remove and return (k,v) tuple with minimum key'''
        if self.is_empty():
            raise KeyError
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
