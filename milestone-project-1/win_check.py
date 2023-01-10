def win_check(board,mark):

    return ((board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5] == mark)
            or (board[6] == board[7] == board[8] == mark) or (board[0] == board[3] == board[6] == mark)
            or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark)
            or (board[6] == board[4] == board[2] == mark) or (board[0] == board[4] == board[8] == mark))
