# 7.4 The Positional List ADT
# 7.4.1 The Positional List Abstract Data Type
'''
    L.first(): Return the position of the first element of L, or None if L is empty.
    L.last(): Return the position of the last element of L, or None if L is empty.
    L.before(p): Return the position of L immediately before position p, or None if the p is the first position
    L.after(p): Return the position of L immediately after position p, or None if the p is the last position
    L.is_empty(): Return True if list L does not contain any elements.
    len(L): Return the number of elements in the list
    iter(L): Return a forward iterator for the elements of the list. 

    L.add_first(e): Insert a new element e at the front of L, returning the position of the new element. 
    L.add_last(e): Insert a new element e at the back of L, returning the position of the new element. 
    L.add_before(p,e): Insert a new element e just before position p in L, returning the position of the new element
    L.add_after(p,e): Insert a new element e just after position p in L, returning the position of the new element
    L.repalce(p,e): Replace the element at position p with element e, returning the element formerly at position p
    L.delete(p): Remove and return the element at position p in L, invalidating the position.
'''

# 7.4.2 Doubly Linked List Implementation
'''
Each method of the positional list ADT runs in worst-case O(1) time when implemented with a doubly linked list. 
'''
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