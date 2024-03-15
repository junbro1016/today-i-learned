# 3.3 Asymptotic Analysis
# Prefix Averages
def prefix_average1(S): # Quadratic Time Algorithm
    '''Return list such that for all j, A[j] equals average of S[0] ... S[j]'''
    result = [0] * len(S)
    for j in range(len(S)):
        total = 0
        for i in range(j+1):
            total += S[i]
        result[j] = total / (j+1)
    return result

def prefix_average2(S): # A Lineaer Time Algorithm
    '''Return list such that for all j, A[j] equals average of S[0] ... S[j]'''
    result = [0] * len(S)
    total = 0
    for j in range(len(S)):
        total += S[j]
        result[j] = total / (j+1)
    return result

# Three-way set disjointness
def disjoint1(A,B,C): # A cubic time algorithm
    '''Return True if there is no element common to all three lists.'''
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

def disjoint2(A,B,C): # A quadratic time algorithm
    '''Return True if there is no element common to all three lists.'''
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True

# Element Uniqueness
def unique1(S): # a quadratic time algorithm
    '''Return True if there are no duplicate elements in sequence S.'''
    for j in range(len(S)):
        for i in range(j+1,len(S)):
            if S[j] == S[i]:
                return False
    return True

def unique2(S): # a nlogn time algorithm
    '''Return True if there are no duplicate elements in sequence S.'''
    temp = sorted(S)
    for j in range(1, len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True