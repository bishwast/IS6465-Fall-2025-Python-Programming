theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

def isWinner(bo, le):   # bo = board, le = letter
    # Given a board and a player’s letter, this function returns True if that player has won.
    # using bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or  # across the top
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or  # across the middle
            (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or  # across the bottom
            (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or  # down the left side
            (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or  # down the middle
            (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or  # down the right side
            (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or  # diagonal
            (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le))  # diagonal

print("Welcome to the Tic Tac Toe!")
turn = "X"

for i in range(9):
    print_board(theBoard)

    print("Turn for " + turn + ". Move on which space? ")
    move = input()
    theBoard[move] = turn

    if isWinner(theBoard, turn):
        print_board(theBoard)
        print("Congrats, you won!")
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
