# 4.6 Eliminating Tail Recursion
'''
some forms of recursion can be eliminated without any use of auxilliary memory.
A recursion is tail recursion if any recursive call that made from one context is the very last operation in that context,
with the return value of the recursive call (if any) immediately returned by the enclosing recursion.
by necessity, a tail recursion must be a linear recursion.

Any tail recursion can be reimplemented nonrecursively by enclosing the body in a loop for repetition,
and replacing a recursive call with new parameters by a reassignement of the existing parameters to those values.
'''
def binary_search_iterative(data, target):
    '''Return True if target is found in the given Python list.'''
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

def reverse_iterative(S):
    '''Reverse elements in sequence S.'''
    start = 0
    stop = len(S)-1
    while start < stop:
        S[start], S[stop] = S[stop], S[start]
        start += 1
        stop -= 1
