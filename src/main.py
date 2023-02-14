import pygame
from constants import WIDTH,HEIGHT
from board import Board


WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Damas By Mike')

def main():
    run=True
    board=Board()
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WINDOW)
        pygame.display.update()
    pygame.quit()
    
    
main()