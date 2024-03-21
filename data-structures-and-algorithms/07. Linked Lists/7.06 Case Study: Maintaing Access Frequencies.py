# 7.6 Case Study: Maintaining Access Frequencies
'''
Favorites list ADT:

    access(e): access the element e, incrementing its access count, and adding it to the favorites list if it is not already present.
    remove(e): remove element e from the favorites list, if present
    top(k): return an iteration of the k most accessed elements
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

# 7.6.1 Using a Sorted List
class FavoritesList:
    '''List of elements ordered from most frequently accessed to least.'''

    #---------------------------------------nested _Item class-----------------------------------------
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    #---------------------------------------nonpublic utitlites-----------------------------------------
    def _find_position(self, e):
        '''Search for element e and return its Position (or None if not found)'''
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        '''Move item at Position p earlier in the list based on access count.'''
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first()) and (cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data._delete(p))
    #---------------------------------------public methods-----------------------------------------
    def __init__(self):
        '''Create an empty list of favorites'''
        self._data = PositionalList()
    
    def __len__(self):
        '''Return number of entries on favorites list'''
        return len(self._data)
    
    def is_emtpy(self):
        '''Return True if list is empty'''
        return len(self._data) == 0
    
    def access(self, e):
        '''Access element e, thereby increasing its access count'''
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)
    
    def remove(self, e):
        '''Remove element e from the list of favorites'''
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
    
    def top(self, k):
        '''Generate sequence of top k elements in terms of access counts'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)