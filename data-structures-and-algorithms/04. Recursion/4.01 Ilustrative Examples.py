# 4.1 Illustrative Examples
# 4.1.1 Factorial Function
'''
in python, each time a function (recursive or otherwise) is called, a structure known as an 'activation record' or 'frame' is created to store information about the progress of that invocation of the function.
this activation record includes a namespace for storing the function call's parameters and local variables, and information about which command in the body of the function is currently executing. 
when the execution of a function call leads to a nested function call, the execution of the former call is suspended and its activation record stores the place in the source code at which the flow of control should continue upon return of the nested call.
this process is used both in the standard case of one function calling a different function, or in the recursive case in which a function invokes itself.
the key point is that there is a different activation record for each active call.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 4.1.2 Drawing a English Ruler
def draw_line(tick_length, tick_label=''):
    '''Draw one line with given tick length (followed by optional label)'''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    '''Draw tick interval based upon a central tick length'''
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

def draw_ruler(num_inches, major_length):
    '''Draw English ruler with given number of inches, major tick length.'''
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))

# 4.1.3 Binary Search
def binary_search(data, target, low, high):
    '''Return True if target is found in indicated portion of a Python list.
    
    The search only considers the portion from data[low] to data[high] inclusive.'''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)
        
# 4.1.4 File Systems
'''
python's os module:
- os.path.getsize(path): return the immediate disk usage (measured in bytes) for the file or directory that is identified by the string path
- os.path.isdir(path): return True if entry designated by string path is a directory; False otherwise
- os.listdir(path): return a list of strings that are the names of all entries within a directory designated by string path. 
- os.path.join(path, filename): compose the path string and filename string using an appropriate operating system separator between the two.
'''
import os

def disk_usage(path):
    '''Return the number of bytes used by a file/folder and any descendents'''
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for f in os.listdir(path):
            childpath = os.path.join(path, f)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total

disk_usage(os.getcwd())