# 9.1.1 Priorities 
'''
priority queue is a collection of prioritized elements that allows arbitrary element insertion, and allows the removal of the element that has first priority. When an element is added to a priority queue, the user designates its priority by providing an associated key. the element with the minimum key will be the next to be removed from the queue.
'''

# 9.1.2 The Priority Queue ADT
'''
P.add(k,v): insert an item with key k and value v into priority queue p. 

P.min(): return a tuple (k,v), representing the key and value of an item in priority queue P with minimum key (but do not remove the item); an error occurs if the priority queue is empty.

P.remove_min(): remove an item with minimum key from p, and return a tuple (k,v), representing the key and value of the removed item; an error occurs if the priority queue is empty. 

P.is_empty(): return True if priority queue P does not contain any item. 

len(P): return the number of items in priority queue p. 

- a priority queue may have multiple entries with equivalent keys, in which case methods min and remove_min may report an arbitrary choice of item having minimum key. 
'''
