# 2.5 Namespaces and Object-Orientation
# 2.5.1 Instance and Class Namespaces
'''
instance namespaces: manages attributes specific to an individual object. 
class namespaces: is used to manage members that are to be shared by all instances of a class, or used without reference to any particular instance.
'''
'''
how entries are established in a namespace:
'self._balance = 0', where 'self' is an identifier for the newly constructed instance.
the use of 'self' as a qualifier for 'self._balance' in such an assignment causes the _balance identifier to be added directly to the instance namespace. 
a class namespace includes all declarations that are made directly within the body of the class definition. 
'''
'''
class data members:
a class-level data member is often used when there is some value, such as a constant, that is to be shared by all instances of a class.
'''
class PredatoryCreditCard():
    OVERLIMIT_FEE = 5 # this is a class-level member

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
'''
nested classes:
it is also possible to nest one class definition within the scope of another class.
this is unrelated to the concept of inheritance. 
'''
'''
dictionaries and __slots__ declaration:
by default, python represents each namespace with an instance of the built-in dict class that maps identifying names in that scope to the associated objects.
python provides a more direct mechanism for representing instance namespaces that avoids the use of ausiliary dictionary.
to use of the streamlined representation for all instances of a class, that class definition must provide a class-level member named __slots__ that is assigned to a fixed sequence of string that serve as names for instance variables.
when inheritance is used, if the base class declares  __slots__, a subclass must also declare __slots__ to avoid creation of instance dictionaries.
the declaration in the subclass should only include names of supplemental methods that are newly introduced. 
'''
class CreditCard: 
    __slots__ = '_customer', '_bank', '_account', '_balance', '_limit' # right-hand side is tuple 

# 2.5.2 Name Resolution and Dynamic Dispatch
'''
when the dot operator syntax is used to access an existing member, python interpreter begins a name resolution process, described as follows:
1. the instance namespace is searched; if the desired name is found, its assciated value is used.
2. otherwise the class namespace, for the class to which the instance belongs, is searched; if the name is found, its associated value is used. 
3. if the name was not found in the immediate class namespace, the search continues upward through the inheritance hierarchy, checking the class namespace for each ancestor. the first time the name is found, its associate value is used.
4. if the name has still not been found, ans Attribute Error is raised.
'''