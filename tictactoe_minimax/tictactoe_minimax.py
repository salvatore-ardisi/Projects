import sys

# The Tic-Tac-Toe board
board = ['-'] * 9

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

# The AI player and the human player
ai_player = 'X'
human_player = 'O'


def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i + 1] + ' | ' + board[i + 2])


def is_board_full(board):
    """Checks if the board is full."""
    return '-' not in board


def get_winner(board):
    """Checks if there is a winner and returns the winner player ('X' or 'O')."""
    for combination in winning_combinations:
        a, b, c = combination
        if board[a] == board[b] == board[c] != '-':
            return board[a]
    return None


def evaluate(board):
    """Evaluates the board and returns the score for the AI player."""
    winner = get_winner(board)
    if winner == ai_player:
        return 1
    elif winner == human_player:
        return -1
    else:
        return 0


def minimax(board, depth, is_maximizing):
    """Applies the minimax algorithm to determine the best move for the AI player."""
    score = evaluate(board)

    if score == 1:
        return score - depth
    if score == -1:
        return score + depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -sys.maxsize
        for i in range(9):
            if board[i] == '-':
                board[i] = ai_player
                score = minimax(board, depth + 1, False)
                board[i] = '-'
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = sys.maxsize
        for i in range(9):
            if board[i] == '-':
                board[i] = human_player
                score = minimax(board, depth + 1, True)
                board[i] = '-'
                best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    """Returns the best move for the AI player."""
    best_score = -sys.maxsize
    best_move = -1

    for i in range(9):
        if board[i] == '-':
            board[i] = ai_player
            score = minimax(board, 0, False)
            board[i] = '-'
            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    """Plays the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    player_choice = int(input("Enter 1 to go first or 2 for AI to go first: "))

    if player_choice == 1:
        human_player = 'X'
        ai_player = 'O'
        current_player = human_player
    else:
        human_player = 'O'
        ai_player = 'X'
        current_player = ai_player

    print_board(board)

    while True:
        if current_player == human_player:
            move = int(input("Enter a number from 1 to 9 to make your move: ")) - 1
            while board[move] != '-':
                print("Invalid move. Try again.")
                move = int(input("Enter a number from 1 to 9 to make your move: ")) - 1
            board[move] = human_player
            current_player = ai_player
        else:
            move = get_best_move(board)
            board[move] = ai_player
            current_player = human_player

        print("Current Board")
        print_board(board)

        winner = get_winner(board)
        if winner is not None:
            print("Game over. {} wins!".format(winner))
            break

        if is_board_full(board):
            print("Game over. It's a tie!")
            break


# Start the game
play_game()
