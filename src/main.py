import pygame
from constants import *
from board import Board
from game import *


WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Damas By Mike')

def get_position_mouse(pos):
    x,y=pos
    row=y // SQUARE
    col= x // SQUARE
    return row,col

def main():
    run=True
    game=Game(WINDOW)
    
    
    
    
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos =pygame.mouse.get_pos()
                row,col = get_position_mouse(pos)
                piece = board.get_piece(row,col)
                board.move(piece,4,3)
        
        game.update()        
        
    pygame.quit()
    
    
main()