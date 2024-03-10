# 1.6 Simple Input and Output
# 1.6.1 Console Input and Output
'''
print function
- the sperator can be customized by providing a desired separating string as a keyword parameter, sep. 
- an alternative trailing string can be designated using a keyword parameter, end. 
- output can be directed to a file by indicating an output file stream using 'file' as a keyword parameter

input function
- displays a prompt, if given as an optional parameter, and then waits until the user enters some sequence of characters followed by the return key.
'''

# 1.6.2 Files
'''
'open' returns a proxy for interactions with the underlying file
'fp = open('sample.txt') attempts to open a file named sample.txt, returning a proxy that allows read-only access to the text file.
open function accepts an optional second parameter that determines the access mode (r, w, a, rb, wb)
when processing a file, the proxy maintains a current position within the file as an offset from the beginning, measured in number of bytes.
'fp.close()' closes the file associated with proxy fp, ensuring that any written contents are saved. 
'''
fp = open('./text1.txt', 'r') # Hello
print(fp.tell()) # 0
print(fp.read()) # Hello. 
print(fp.tell()) # 6
fp.seek(1) 
print(fp.read(2)) # el (current position: 3)
print(fp.read()) # lo. (current position: 6)
fp.close()

fp = open('./text2.txt', 'w')
fp.writelines(['My name is Junhyeong.\n', 'I\'m currently studying python primer.'])
fp.close()

fp = open('./text3.txt', 'w')
print('Hello.\nMy name is Brandon. \nWhat is your name?', file = fp) # no output in console. redircet output of print function to the text3.txt file
fp.close()

fp = open('./text3.txt', 'r')
for line in fp:
    print(line, end = '')
fp.close()