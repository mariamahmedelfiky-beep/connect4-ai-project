import math
import random

from constants import *
from game_logic import *
from evaluation import score_position


def is_terminal_node(board):

    return (
        winning_move(board, PLAYER)
        or winning_move(board, AI)
        or len(get_valid_locations(board)) == 0
    )


def minimax(board, depth, alpha, beta, maximizing_player):

    valid_locations = get_valid_locations(board)

    # Prefer center columns first
    valid_locations.sort(key=lambda col: abs(3 - col))

    terminal = is_terminal_node(board)

    if depth == 0 or terminal:

        if terminal:

            if winning_move(board, AI):
                return None, 100000000

            elif winning_move(board, PLAYER):
                return None, -100000000

            else:
                return None, 0

        else:
            return None, score_position(board, AI)

    if maximizing_player:

        value = -math.inf
        best_col = random.choice(valid_locations)

        for col in valid_locations:

            row = get_next_open_row(board, col)

            temp_board = board.copy()

            drop_piece(temp_board, row, col, AI)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                False
            )[1]

            if new_score > value:

                value = new_score
                best_col = col

            alpha = max(alpha, value)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best_col, value

    else:

        value = math.inf
        best_col = random.choice(valid_locations)

        for col in valid_locations:

            row = get_next_open_row(board, col)

            temp_board = board.copy()

            drop_piece(temp_board, row, col, PLAYER)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                True
            )[1]

            if new_score < value:

                value = new_score
                best_col = col

            beta = min(beta, value)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best_col, value
