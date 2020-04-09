# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:51:02 2020

@author: William
"""
import numpy as np
#import pygame

row_count = 6
col_count = 7

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def drop_piece(board, row , col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    
    return board[row_count-1][col] == 0 # top row is 5th row


def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #Check vertical locations for win
    for r in range(row_count-2):
        for c in range(col_count):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
            
    #Check ascending slope for win
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    #Check descending slope for win
    for c in range(col_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
#def draw_board(board):
    

board = create_board()
print_board(board)
game_over = False
turn = 0

#pygame.init()

square_size = 100 # in pixels

width = col_count * square_size
height = (row_count + 1) * square_size

size = (width, height)

#screen = pygame.display.set_mode(size)

while not game_over:
    #Ask for Player 1 input
    if turn % 2 == 0:
        col = int(input("Player 1, make your selection! (0-6): "))
        while col > 6:
            col = int(input("Player 1, please make a valid selection! (0-6): "))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            print_board(board)
            
            if winning_move(board, 1):
                print("PLAYER 1 Wins!!!!!")
                game_over = True
    
    #Ask for Player 2 input
    else:
        col = int(input("Player 2, make your selection! (0-6): "))
        while col > 6:
            col = int(input("Player 2, please make a valid selection! (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print_board(board)
            
            if winning_move(board, 2):
                print("PLAYER 2 Wins!!!!!")
                game_over = True
        
    #2print("Your selection is " + int(selection))
    
    turn += 1