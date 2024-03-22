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

# 8.2 Binary Trees
'''
A binary tree is an ordered tree with the following properties: 
    1. Every node has at most two children
    2. Each child node is labeled as being either a left child or a right child. 
    3. A left child precedes a right child in the order of children of a node. 

A binary tree can be defined in a recursive way such that a binary tree is either empty or consist of: 
    - A node r, called the root of T, that stores an element
    - A binary tree (possibly empty), called the left subtree of T
    - A binary tree (possible empty), called the right subtree of T
'''

# 8.2.1 The Binary Tree Abstract Data Type
'''
T.left(p): return the position that represents the left child of p, or None if p has no left child.
T.right(p): return the position that represents the right child of p, or None if p has no right child. 
T.sibling(p): return the position that represents the sibling of p, or None if p has no sibling.
'''

class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure.'''

    #--------------------------additional abstract methods--------------------------------
    def left(self, p):
        '''Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        '''Return a Position representing p's right child.
        
        Return None if p does not have a right child.
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    #--------------------------concrete methods implemented in this class--------------------------------
    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling)'''
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

# 8.2.2 Properties of Binary Trees
'''
In a nonempty proper binary tree T, with nE external nodes and nI internal nodes, we have nE = nI + 1. 
'''
    