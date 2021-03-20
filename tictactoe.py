import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
TURN_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 200)

BOARD = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'board.png')), (WIDTH, HEIGHT))
XS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'clipartX.png')), (WIDTH//5, HEIGHT//5))
OHS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'clipartO.png')), (WIDTH//5, HEIGHT//5))



FPS = 10


def draw_xando(board):
    x = 0
    y = 0
    for space in board:
        if (x == 3):
            x = 0
            y += 1
        if (space != 0):
            if (space == 'X'):
                WIN.blit(XS, ((x * (WIDTH//3))+ 50, (y * (HEIGHT//3)) + 50))
            else:
                WIN.blit(OHS, ((x * (WIDTH//3))+ 50, (y * (HEIGHT//3)) + 50))
        x += 1
        



def draw_board(board):
    WIN.fill(WHITE)
    WIN.blit(BOARD, (0,0))
    draw_xando(board)
    pygame.display.update()

def col_win(board):
    first = 0
    for counter in range(3):
        first = board[counter]
        if (first != 0):
            if((first == board[counter + 3]) and (first == board[counter + 6])):
                return first
    return 0



def row_win(board):
    first = 0
    for counter in [0,3,6]:
        first = board[counter]
        if (first != 0):
            if((first == board[counter + 1]) and (first == board[counter + 2])):
                return first
    return 0


def diag_win(board):
    if (board[4] != 0):
        mid = board[4]
        if ((board[0] == mid) and (board[8] == mid)):
            return mid
        elif ((board[2] == mid) and (board[6] == mid)):
            return mid
    else:
        return 0


def check_win(board):
    tie = True
    win = 0
    for space in board:
        if (space == 0):
            tie = False
            break

    col_w = col_win(board)
    row_w = row_win(board)
    diag_w = diag_win(board)

    if (col_w != 0):
        win = col_w
    elif (row_w != 0):
        win = row_w
    elif (diag_w != 0):
        win = diag_w
    
    if (win == 'X'):
        return 'X'
    elif (win == 'O'):
        return 'O'
    elif (tie):
        return 'T'
    else:
        return 0


    
def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,
     HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def place_x_o(pos, turn, board):
    index = pos[0]//(WIDTH//3) + (3 *(pos[1]//(HEIGHT//3)))
    if (board[index] != 0):
        return turn
    else:
        if (turn == 1):
            board[index] = 'X'
            return 2
        else:
            board[index] = 'O'
            return 1


def main():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    clock = pygame.time.Clock()
    run = True
    win = 0
    turn = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                turn = place_x_o(pos, turn, board)
                win = check_win(board)

        clock.tick(FPS)
        draw_board(board)

        if (win != 0):
            if (win == 'X'):
                winner_text = 'P1 WINS'
            elif (win == 'O'):
                winner_text = 'P2 WINS'
            else:
                winner_text = 'TIE GAME'
            draw_winner(winner_text)
            main()

if __name__ == '__main__':
    main()