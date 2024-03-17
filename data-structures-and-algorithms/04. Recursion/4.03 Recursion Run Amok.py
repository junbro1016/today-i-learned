# 4.3 Recursion Run Amok
'''Running time of the function is O(2^n)'''
def unique3(S, start, stop):
    '''Return True if there are no duplicate elements in slice S[start:stop].'''
    if stop - start <= 1: return True                # at most one time
    elif not unique3(S, start, stop-1): return False # first part has duplicate
    elif not unique3(S, start+1, stop): return False # second part has duplicate
    else: return S[start] != S[stop-1]               # do fist and last differ? 

'''
An Inefficient Recursion for Computin Fibonacci Numbers
'''
def bad_fibonacci(n):
    '''Return the nth fibonacci number'''
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-2)

'''
An Efficient Recursion for Computing Fibonacci Numbers:
    rather than having the function return a single value, which is the nth Fibonacci number, 
    we define a recursive function that returns a pair of consecutive Fibonacci numbers (Fn ,Fn-1), using the convention Fn-1 = 0.
'''
def good_fibonacci(n):
    '''Return pair of Fibonacci numbers, F(n) and F(n-1)'''
    if n <= 1:
        return (n,0)
    else:
        a, b = good_fibonacci(n-1)
        return (a+b, a)

# 4.3.1 Maximum Recursive Depth in Python
'''
the desingers of python made an internal decision to limit the overall number of function activations that can be simultaneously active.
the precise value of this limit depends upon the python distribution, but a typical default value is 1000.
if this limit is reached, the python interpreter raises a RuntimeError with a message, 'maximum recursion depth exceeded.'
the python interpreter can be dynamically reconfigured to change the default recursive limit. 
this is done through use of a module naemd 'sys', which supports a 'getrecursionlimit' and 'setrecursionlimit'.
'''
import sys
old = sys.getrecursionlimit()
sys.setrecursionlimit(1000000)