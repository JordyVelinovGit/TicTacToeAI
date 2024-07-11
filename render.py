def render(board):
    
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == None):
                board[i][j] = " "

    print("    0 1 2")
    print("   -------")
    print(f"0 | {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"1 | {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"2 | {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("   -------")