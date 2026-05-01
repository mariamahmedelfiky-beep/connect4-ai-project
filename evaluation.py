from constants import *


def evaluate_window(window, piece):
    score = 0

    opponent_piece = PLAYER

    if piece == PLAYER:
        opponent_piece = AI

    if window.count(piece) == 4:
        score += 100

    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10

    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80

    return score


def score_position(board, piece):
    score = 0

    center_array = [int(i) for i in list(board[:, COLS // 2])]
    center_count = center_array.count(piece)
    score += center_count * 6

    # Horizontal
    for row in range(ROWS):
        row_array = [int(i) for i in list(board[row, :])]

        for col in range(COLS - 3):
            window = row_array[col:col + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Vertical
    for col in range(COLS):
        col_array = [int(i) for i in list(board[:, col])]

        for row in range(ROWS - 3):
            window = col_array[row:row + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + i][col + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Negative diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + 3 - i][col + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score
