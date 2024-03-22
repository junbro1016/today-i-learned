# 8.1 General Trees
# 8.1.1 Tree Definitions and Properties
'''
a tree is an abstract data type that stores elements hierarchically. 
'''
'''
Formal Tree Definition:

- if T is nonempty, it has a special node, called the root of T, that has no parent. 
- each node v of T different from the root has a unique parent node w; every node with parent w is a child of w.

note that according to our definition, a tree can be empty, meaning that it does not have any nodes.
'''

# 8.1.2 The Tree Abstract Data Type
'''
p.element(): return the element stored at position p.

T.root(): return the position of the root of tree T, or None if T is empty.
T.is_root(p): return True if position p is the root of Tree T.
T.parent(p): return the position of parent of position p, or None if p is the root of T. 
T.num_children(p): return the number of children of position p. 
T.children(p): generate an iteration of the children of position p. 
T.is_leaf(p): return True if position p does not have any children. 
len(T): return the number of positions (and hence elements) that are contained in tree T. 
T.is_empty(): return True if tree T does not contain any positions
T.positions(): Generate an iteration of all positions of tree T. 
iter(T): Generate an iteration of all elements stored within tree T. 
'''
class Tree:
    '''Abstract base class representing a tree structure.'''

    #--------------------------------------nested Position class----------------------------------------
    class Position:
        '''An abstraction representing the location of a single element'''

        def element(self):
            '''Return the element stored at this Position'''
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            '''Return True if other Position represents the same location'''
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)
    
    #----------------abstract methods that concretes subclass must support-------------------
    def root(self):
        '''Return Position representing the tree's root (or None if empty).'''
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        '''Return Position representing p's parent (or None if p is root).'''
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        '''Return the number of children that Position p has'''
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        '''Return the total number of elements in the tree.'''
        raise NotImplementedError('must be implemented by subclass')
    
    #-----------------------concrete methods implemented in this class---------------------------
    def is_root(self, p):
        '''Return True if Position p represents the root of the tree'''
        return self.root() == p
    
    def is_leaf(self, p):
        '''Return True if Position p does not have any children'''
        return self.num_children(p) == 0
    
    def is_empty(self):
        '''Return True if the tree is empty'''
        return len(self) == 0
    
    def depth(self, p):
        '''Return the number of levels separating Position p from the root.'''
        if self.is_root(p):
            return 0
        parent = self.parent(p)
        return 1 + self.depth(parent)
    
    def _height2(self, p):
        '''Return the height of the tree'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        '''Return the height of the subtree rooted at Position p.
        
        If p is None, return the height of the entire tree.
        '''
        if p is None():
            p = self.root()
        return self._height2(p)

# 8.1.3 Computig Depth and Height
'''
let p be the position of a node of a tree T. 
the depth of p is the number of ancestors of p, excluding p itself. 
note that this definition implies that the depth of the root of T is 0.

- if p is the root, then the depth of p is 0.
- otherwise, the depth of p is one plus the depth of the parent of p. 
'''
def depth(self, p):
    '''Return the number of levels separating Position p from the root.'''
    if self.is_root(p):
        return 0
    parent = self.parent(p)
    return 1 + self.depth(parent)

'''
the height of a position p in a tree T is also defined recursively:
- if p is a leaf, then the height of p is 0.
- otherwise, the height of p is one more than the maximum of the heights of p's children

the height of a nonempty tree T is equal to the maximum of the depths of its leaf positions.
'''
def _height1(self):
    '''Return the height of the tree'''
    return max(self.depth(p) for p in self.position() if self.is_leaf(p))

def _height2(self, p):
    '''Return the height of the tree'''
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))
'''
we can determine the running time of the height2 algorithm by summing over all the positions,
the amount of time spent on the nonrecursive part of each call. 
'''