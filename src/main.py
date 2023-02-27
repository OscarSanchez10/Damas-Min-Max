import pygame
from constants import *
from game import Game
from minmax.algorithm import minimax

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas By MM')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE
    col = x // SQUARE
    return row, col


def main():
    run = True
    game = Game(WINDOW)

    while run:

        # Si es el turno del jugador blanco, elige el mejor movimiento según el algoritmo Minimax
        if game.turn == WHITE:
            value, new_board = minimax(game.getBoard(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
