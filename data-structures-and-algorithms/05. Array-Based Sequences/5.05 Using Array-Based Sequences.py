# 5.5 Using Array-Based Sequences
# 5.5.1 Storing High Scores for a Game
class GameEntry:
    '''Represents one entry of a list of high scores.'''
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score) # e.g., '(Bob, 98)'

class Scoreboard:
    '''Fixed-length sequence of high scores in nondecreasing order.'''

    def __init__(self, capacity=10):
        '''Initialize scoreboard with given maximum capacity.
        
        All entries are initially None.
        '''
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        '''Return entry at index k'''
        return self._board[k]
    
    def __str__(self):
        '''Return string representation of the high score list.'''
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        '''Consider adding entry to high scores.'''
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1 
            while j > 0 and self._board[-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

# 5.5.2 Sorting a Sequence
def insertion_sort(A):
    '''Sort list of comparable elements into nondecreasing order.'''
    for k in range(1, len(A)):       # from 1 to n-1
        cur = A[k]
        idx = k-1
        while idx >= 0 and A[idx] > cur:
            A[idx+1] = A[idx]
            idx -= 1
        A[idx+1] = cur

# 5.5.3 Simple Cryptography
class CeaserCipher:
    '''Class for doing encryption and decryption using a Caeser cipher.'''

    def __init__(self, shift):
        '''Construct Ceaser cipher using given integer shift for rotation.'''
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        '''Return string representing encrypted message.'''
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        '''Return decrypted message given encrypted secret.'''
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        '''Utility to perform transformation based on given code string.'''
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)