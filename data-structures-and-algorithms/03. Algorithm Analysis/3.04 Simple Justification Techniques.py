# 3.4 Simple Justification Techniques
# Loop Invariant
'''
To prove some statement L about a loop is correct, define L in terms of a series of smaller statements L0, L1, ... ,Lk, where:
1. The initial claim, L0 is true before the loop begins. 
2. If Lj-1 is true before the iteration j, then Lj will be true after iteration j. 
3. The final statement Lk, implies the desired statement L to be true. 
'''
def find(S, val):
    '''Return index j such that S[j]==val, or -1 if no such element.'''
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j 
        j += 1
    return -1
'''
Lj: val is not equal to any of the first j elements of S.
'''