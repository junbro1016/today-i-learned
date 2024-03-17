# 4.4 Further Examples of Recursion
# 4.4.1 Linear Recursion
'''
if a recursive function is designed so that each invocation of the body makes at most one new recursive call, this is known as 'linear recursion'.
note that linear recursion terminology reflects the structure of the recursion rate, not the asymptotic analysis of the running time.
'''
'''
Summing the Elements of a Sequence Recursively:
    the sum of all n integers in S is trivially 0, if n=0, and otherwise that it is the sum of the first n-1 integers in S plus the last element in S.
'''
def linear_sum(S, n):
    '''Return the sum of the first n numbers of sequence S.'''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

'''
Reversing a Sequence with Recursion:
    reversal of a sequence can be achieved by swapping the first and last elements and then recursively reversing the remaining elements.
'''
def reverse(S, start, stop):
    '''Reverse elements in implicit slice S[start:stop].'''
    if stop - start > 1:                             # if at least 2 elements:
        S[start], S[stop-1] = S[stop-1], S[start]    # swap first and last
        reverse(S, start+1, stop-1)                  # recur on rest

'''
Recursive Algorithm for Computing Powers:
    1. x^n = x * x^(n-1)
    2. x^n = (x^k)^2 (n is even)
       x^n = x*(x^k)^2 (n is odd)
       k = n//2
    our new formulation of the power function results in O(logN) recursive calls.
    because the recursive depth of the improved version is O(logN), its memory usage is O(logN) as well.
'''
def power1(x,n):
    '''Compute the value x ** n for integer n.'''
    if n==0:
        return 1
    else:
        return x * power1(x, n-1)

def power2(x,n):
    '''Compute the value x ** n for interger n.'''
    if n == 0:
        return 1
    else:
        partial = power2(x, n//2)
        result = partial*partial
        if n % 2 == 1:
            result *= x
        return result
    
# 4.4.2 Binary Recursion
'''
when a function makes two recursive calls, we say that it uses binary recursion. 
binary_sum uses O(logN) amount of additional space, which is a big improvement over the O(n) space used by the linear_sum.
the running time of binary_sum is O(n), as there are 2n-1 function calls, each requiring constant time.

Q. How does binary sum use O(log N) space?
https://stackoverflow.com/questions/32426732/how-does-binary-sum-use-olog-n-space
'''
def binary_sum(S, start, stop):
    '''Return the sum of the numbers in implicit slice S[start:stop]'''
    if stop - start <= 0:                                               # zero elements in slice
        return 0
    elif stop - start == 1:                                             # one element in slice
        return S[start]
    else:                                                               # two or more elements in slice
        mid = (start+stop)//2
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop) 
    
# 4.4.3 Multiple Recursion
'''
Generalizing from binary recursion, we define multiple recursion as a process in which a function may make more than two recursive calls.
'''