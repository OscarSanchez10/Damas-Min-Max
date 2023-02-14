import pygame
from constants import *
from piece import *


class Board:
    def __init__(self) :
        self.board = []
        self.white=12
        self.black=12
        self.white_king=0
        self.black_king=0
        self.select_piece=None
        self.create_board()
    
    
    #Metodo para Dibujar el tablero    
    def draw_square(self,window):
        window.fill(BLUE)
        for row in range(ROWS):
            for col in range(row%2,ROWS,2):
                pygame.draw.rect(window,GRAY,(row*SQUARE,col*SQUARE,SQUARE,SQUARE))
                
                
    #Ubicacion de las fichas
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    #            
    def draw(self,window):
        self.draw_square(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece= self.board[row][col]
                if piece != 0:
                    piece.draw(window)