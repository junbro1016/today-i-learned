# 1.3 Expressions, Operators, and Precedence

'''
'a is b' evaluates to True, precisely when identifiers a and b are aliases for the same object. 
'a == b' tests a more general notion of equivalence. 
use of 'is' and 'is not' should be reserved for situations in which it is necessary to detect true aliasing. 
'''
a = 98.0
b = a
print(a is b) # True
print(a is not b) # False
print(a == b) # True
print(a != b) # False
b = 98
print(a is b) # False
print(a is not b) # True
print(a == b) # True
print(a != b) # False

'''
python carefully extends the semantics of // and % to cases where one or both operands are negative. 
python guarantees that quotient * divisor + remainder == dividend.
if the divisor m is positive, python guarantees  0 <= r < m.
if the divisor m is negative, python guarantees m < r <= 0.
'''
print(-27//4) # -7
print(-27%4) # 1
# -7 * 4 + 1 == -27
print(27//-4) # -7
print(27%-4) # -1
# -7 * -4 + (-1) == 27

'''
because lists are mutable, the syntax 's[j]=val' can be used to replace an element at a given index. 
lists also support a syntax, del s[j], that removes the designated element from the list. 
slice notation can also be used to replace or delete a sublist.
all sequences define comparison operations based on lexicographic order.
'''
a = [1,2,3,4]
print(a) # [1,2,3,4]
del a[1]
print(a) # [1,3,4]
print([5,6,9] < [5,7]) # True

'''
sets and frozensets support the following operators: 

'key in s' : containment check
'key not in s' : non-containment check
's1 == s2' : s1 is equivalent to s2
's1 != s2' : s1 is not equivalent to s2
's1 <= s2' : s1 is subset of s2
's1 < s2' : s1 is proper subset of s2
's1 >= s2' : s1 is superset of s2
's1 > s2' : s1 is proper superset of s2
's1 | s2' : the union of s1 and s2
's1 & s2' : the intersection of s1 and s2
's1 - s2' : the set of elements in s1 but not s2
's1 ^ s2' : the set of elements in precisely one of s1 or s2 (xor)

note well that sets do not guarantee a particular order of their elements, so the comparison operators, such as <, are not lexicogrpahic. 
rather, they are based on the mathematical notion of a subset. 

dictionaries support the following operators: 

'd[key]' : values associated with given key
'd[key] = value' : set (or reset) the value associated with given key
'del d[key]' : remove key and its associated value from dicitonary
'key in d' : containment check
'key not in d' : non-containment check
'd1 == d2' : d1 is equivalent to d2
'd1 != d2' : d1 is not equivalent to d2
'''
s1 = {1,2,3}
s2 = {1,2}
print(s2 < s1) # True
d1 = {'안녕하세요': 'Korean'}
d2 = {'안녕하세요': 'korean'}
print(d1 == d2) # False

'''
python supports an extended assignment operators for most binary operators. 
for an immutable type, such as a number or a string, one should not presume that this syntax changes the value of of the existing object, but instead that it will reassign the identifier to a newly constructed value.
however, it is possible for a type to redefine such semantics to mutate the object, as the list class does for the += operator.
'''
alpha = [1,2,3]
beta = alpha # an alias for alpha
print(alpha, beta)
print(alpha is beta) # True
beta += [4,5] # extends the original list with two more elements
print(alpha, beta)
print(alpha is beta) # True
beta = beta + [6,7] # reassigns beta to a new list [1,2,3,4,5,6,7]
print(alpha, beta)
print(alpha is beta) # False

'''
python allows a chained assignment, such as x = y = 0, to assign multiple identifiers to the rightmost value.
python also allows the chaining of comparison operators.
for example, the expression 1 <= x + y <= 10 is evaluated as teh compound (1 <= x+y) and (x+y <=10), but without computing the intermediate value x+y twice.
'''