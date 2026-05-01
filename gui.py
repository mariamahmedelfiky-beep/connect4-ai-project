import pygame
import sys

from constants import *
from game_logic import *
from minimax import minimax


pygame.init()

width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 AI")

font = pygame.font.SysFont("monospace", 50)


def draw_board(board):

    for col in range(COLS):
        for row in range(ROWS):

            pygame.draw.rect(
                screen,
                BLUE,
                (
                    col * SQUARESIZE,
                    row * SQUARESIZE + SQUARESIZE,
                    SQUARESIZE,
                    SQUARESIZE,
                ),
            )

            pygame.draw.circle(
                screen,
                BLACK,
                (
                    int(col * SQUARESIZE + SQUARESIZE / 2),
                    int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                ),
                RADIUS,
            )

    for col in range(COLS):
        for row in range(ROWS):

            if board[row][col] == PLAYER:
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        int(col * SQUARESIZE + SQUARESIZE / 2),
                        height - int(row * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )

            elif board[row][col] == AI:
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (
                        int(col * SQUARESIZE + SQUARESIZE / 2),
                        height - int(row * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )

    pygame.display.update()


def run_game():

    board = create_board()
    game_over = False

    draw_board(board)

    turn = PLAYER

    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]

                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:

                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

                if turn == PLAYER:

                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if is_valid_location(board, col):

                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER)

                        if winning_move(board, PLAYER):
                            label = font.render("PLAYER WINS", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        draw_board(board)

                        turn = AI

        if turn == AI and not game_over:

            col, minimax_score = minimax(board, 5, -9999999, 9999999, True)

            if is_valid_location(board, col):

                pygame.time.wait(500)

                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI)

                if winning_move(board, AI):
                    label = font.render("AI WINS", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                draw_board(board)

                turn = PLAYER

        if is_draw(board) and not game_over:
            label = font.render("DRAW", 1, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True

        if game_over:
            pygame.time.wait(3000)
