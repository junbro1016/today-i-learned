# 6.3 Double-Ended Queues
'''
we next consider a queue-like data structure that supports insertion and deletion at both the front and back of the queue.
Such a structure is called a double-endede queue, or deque, which is usually pronounced 'deck' to avoid confusion with the
dequeue method of the regular queue, ADT, which is pronounced like the abbreviation 'D.Q'.
'''
# 6.3.1 The Deque Abstract Data Type
'''
D.add_first(e): Add element e to the front of deque D.
D.add_last(e): Add element e to the back of deque D.
D.delete_first(): Remove and return the first element from deque D; an error occurs if the deque is empty. 
D.delete_last(): Remove and return the last element from deque D; an error occurs if the deque is empty.
D.first(): return the first element (but do not remove); an error occurs if the deque is empty.
D.last(): return the last element (but do not remove); an error occurs if the deque is empty.
D.is_empty(): return true if deque D does not contain any elements
len(D): return the number of elements in deque D; in python, we implement this with the special method __len__.
'''
# 6.3.3 Deques in Python Collections Module
'''
~ 
the library deque constructor also supports an optional 'maxlen' parameter to force a fixed-length deque.
however, if a call to append at either end is invoked when the deque is full, it does not throw an error;
instead, it causes one element to be dropped from the opposite side. 
'''