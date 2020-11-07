name = 'Hello'
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
print(type(name))
print(type(board))

def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-----')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-----')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

board['top-L']='O'
board['mid-M']='O'
board['low-R']='O'
board['mid-R']='X'
printBoard(board)
