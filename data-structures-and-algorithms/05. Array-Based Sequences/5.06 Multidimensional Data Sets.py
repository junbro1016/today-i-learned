# 5.6 Multidimensional Data Sets
'''
Constructing a Multidimensional List
'''
c = 6
r = 3
'''
Below just create a one-dimensional list with r*c numbers of zeros.
'''
# WARNING: this is a mistake
data1 = ([0] * c) * r
'''
Below, the problem is that all r entries of the list known as data2 are references to the same instance of a list of c zeros.
For simplicity, we overlook the facts that the values in the secondary list are referential.
'''
# This is still mistake
data2 = [[0] * c] * r
data2[2][0] = 100
print(data2[0][0], data2[1][0], data2[2][0]) # 100 100 100
'''
To properly initialize a two-dimenstional list, we must ensure that each cell of the primary list refers to an 
independent instance of a secondary list. This can be accomplished through the use of Python's list comprehension syntax.
'''
data3 = [[0]*c for _ in range(r)]
data3[2][0] = 100
print(data3[0][0], data3[1][0], data3[2][0]) # 0 0 100

# Tic Tac Toe
class TicTacToe:
    '''Management of a Tic-Tac-Toe game (does not do strategy)'''

    def __init__(self):
        '''Start a new game'''
        self._board = [[' ']*3 for _ in range(3)]
        self._player = 'X'
    
    def mark(self, i, j):
        '''Put ans X or O mark at position(i,j) for next player's turn'''
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'
        
    def _is_win(self, mark):
        '''Check whether the board configuration is a win for the given player.'''
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or 
                mark == board[1][0] == board[1][1] == board[1][2] or 
                mark == board[2][0] == board[2][1] == board[2][2] or 
                mark == board[0][0] == board[1][0] == board[2][0] or 
                mark == board[0][1] == board[1][1] == board[2][1] or 
                mark == board[0][2] == board[1][2] == board[2][2] or 
                mark == board[0][0] == board[1][1] == board[2][2] or 
                mark == board[0][2] == board[1][1] == board[2][0] )

    def winner(self):
        '''Return mark of winning player, or None to indicate a tie.'''
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        '''Return string representation of current game board.'''
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
        
game = TicTacToe()
game.mark(1,1)
game.mark(0,2)
game.mark(2,2)
game.mark(0,0)
game.mark(0,1)
game.mark(2,1)
game.mark(1,2)
game.mark(1,0)  
game.mark(2,0)

print(game)
winner = game.winner()
if winner is None:
    print('Tie')
else:
    print(winner, 'wins')