import numpy as np
from constants import *


def create_board():
    return np.zeros((ROWS, COLS), dtype=int)


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[0][col] == EMPTY


def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row


def print_board(board):
    print(np.flip(board, 0))


def get_valid_locations(board):
    valid_locations = []

    for col in range(COLS):
        if is_valid_location(board, col):
            valid_locations.append(col)

    return valid_locations


def winning_move(board, piece):

    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece
                and board[row][col + 1] == piece
                and board[row][col + 2] == piece
                and board[row][col + 3] == piece
            ):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if (
                board[row][col] == piece
                and board[row + 1][col] == piece
                and board[row + 2][col] == piece
                and board[row + 3][col] == piece
            ):
                return True

    # Positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece
                and board[row + 1][col + 1] == piece
                and board[row + 2][col + 2] == piece
                and board[row + 3][col + 3] == piece
            ):
                return True

    # Negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == piece
                and board[row - 1][col + 1] == piece
                and board[row - 2][col + 2] == piece
                and board[row - 3][col + 3] == piece
            ):
                return True

    return False


def is_draw(board):
    return len(get_valid_locations(board)) == 0
