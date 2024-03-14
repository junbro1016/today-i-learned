# 2.6 Shallow and Deep Copying
from copy import copy, deepcopy

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

color1 = Color(1,2,3)
color2 = Color(4,5,6)
color3 = Color(7,8,9)

# initialization 
warmtones = [color1, color2, color3]

# make an alias
palette = warmtones
print(id(warmtones), id(palette))
print(warmtones, palette)

# shallow copying
palette = copy(warmtones)
print(id(warmtones), id(palette))
print(warmtones, palette)
warmtones[0]._red = 10
print(palette[0]._red) # 10
warmtones[0]._red = 1
print(palette[0]._red) # 1

# deep copying
palette = deepcopy(warmtones)
print(id(warmtones), id(palette))
print(warmtones, palette)
warmtones[0]._red = 111
print(palette[0]._red) # 1
print(warmtones[0]._red) # 111

'''
shallow copy:
the new list initialized so that its contents are precisely the same as the original sequence. 
however, python's lists are referential, and so the new list represents a sequence of references to the same elements as in the first.
we can legitimately add or remove elements from palette without affecting warmtones, but if we edit a color instance from the palette list, we effectively change the contents of warmtones.

deep copy:
the new copy references its own copies of those referenced by the original version. 
'''