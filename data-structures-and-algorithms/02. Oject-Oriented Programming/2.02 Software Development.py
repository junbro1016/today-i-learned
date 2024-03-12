# 2.2 Software Development
'''
traditional software development involves several phases. Three major steps are: 
1. Design 2. Implementation 3. Testing and Debugging
'''
# 2.2.3 Coding Style and Documentation
'''
coding style 
the official style guide for python code is available online at: http://www.python.org/dev/peps/pep-0008
- python code blocks are typically indented by 4 spaces.
- it is strongly recommended that tabs be avoided, as tabs are displayed with differing widths across systems, and tabs and spaces are not viewed as identical by the python interpreter.
- use meaningful names for identifiers. 
- try to choose names that can be read aloud, and choose names that reflect the action, reponsibility, or data each identifier is naming.
- Classes (other than python's built-in classes) should have a name that serves as a singular noun, and should be capitalized. ('Date' rather than 'date' or 'Dates')
- when multiple words are concatenated to form a class name, they should follow the so-called 'CamelCase' convention in which the first letter of each word is capitalized.
- function, including member functions of a class, should be lowercase. 
- if multiple words are combined, they should be separated by under-scores.
- the name of a function should typically be a verb that describes its affect. 
- however, if the only purpose of the function is to return a value, the function name may be a noun that describes the value ('sqrt' rather than 'calculate_sqrt')
- names that identify an individual object (a parameter, instance variable, local variable) should be a lowercase noun 
- identifiers that represent a value considered to be a constant are traditionally identified using all capital letters and with underscores to separate words
- identifiers in any context that begin with a single leading underscore (_secret) are intended to suggest that they are only for 'internal' use to a class or module, and not part of a public interface.

documentation
python provides integrated support for embedding formal documentation directly in source code using a mechanism known as a docstring. 
formally, any string literal that appears as the first statement within the body of a module, class, or function (including a member function of a class) will be considered to be a docstring. 
by convention, those string literals should be delimited within triple quotes ('''''')
more detailed docstrings should begin with a single line that summarizes the purpose, followed by a blank line, and then further details. 
a docstring is stored as a field of the module, function, or class in which it is declared. 
it serves as documentation and can be retrieved in a variety of ways. 
'''
def scale(data, factor):
    '''Multiply all entries of numeric data list by the given factor'''
    for j in range(len(data)):
        data[j] *= factor

# help(scale)

