import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
TURN_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 200)

BOARD = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'board.png')), (WIDTH, HEIGHT))
XS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'clipartX.png')), (WIDTH//4, HEIGHT//4))
OHS = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'clipartO.png')), (WIDTH//4, HEIGHT//4))



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
                WIN.blit(XS, ((x * 300)+40, (y * 300) + 40))
            else:
                WIN.blit(OHS, ((x * 300)+40, (y * 300) + 40))
        x += 1
        



def draw_board(board):
    WIN.fill(WHITE)
    WIN.blit(BOARD, (0,0))
    draw_xando(board)
    pygame.display.update()


def check_win(board):
    return 0
    
def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,
     HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

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
                place_x_o(pos, turn)

        clock.tick(FPS)
        draw_board(board)
        win = check_win(board)

        if (win != 0):
            if (win == 'X'):
                winner_text = 'P1 WINS'
            elif (win == 'O'):
                winner_text = 'P2 WINS'
            else:
                winner_text = 'TIE GAME'
            draw_winner(winner_text)
            break

if __name__ == '__main__':
    main()