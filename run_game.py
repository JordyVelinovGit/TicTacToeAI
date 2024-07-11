from get_move import get_move
from new_board import new_board
from render import render

board = new_board()

board[0][0] = "X"
board[0][1] = "O"
board[0][2] = "X"

render(board)

get_move()