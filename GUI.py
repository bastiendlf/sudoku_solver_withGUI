# GUI.py
import pygame
from sudoku_solver import solve, grid
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (10, 10, 150)
GRID = (100, 100, 100)

TEXT_RECT = (SCREEN_WIDTH / 9, SCREEN_HEIGHT / 9)

given_number_pos = list()
for row in range(9):
    for col in range(9):
        if grid[row][col] != 0:
            given_number_pos.append((row, col))


def draw_grid(screen):
    screen.fill(WHITE)

    for i in range(1, 9):
        pygame.draw.rect(screen, GRID, [i * SCREEN_HEIGHT / 9, 0, 1, SCREEN_HEIGHT])
        pygame.draw.rect(screen, GRID, [0, i * SCREEN_HEIGHT / 9, SCREEN_WIDTH, 1])

    pygame.draw.rect(screen, BLACK, [SCREEN_HEIGHT / 3, 0, 5, SCREEN_HEIGHT])
    pygame.draw.rect(screen, BLACK, [2 * SCREEN_HEIGHT / 3, 0, 5, SCREEN_HEIGHT])
    pygame.draw.rect(screen, BLACK, [0, SCREEN_HEIGHT / 3, SCREEN_WIDTH, 5])
    pygame.draw.rect(screen, BLACK, [0, 2 * SCREEN_HEIGHT / 3, SCREEN_WIDTH, 5])


def draw_numbers(screen, grid: list):
    font = pygame.font.SysFont('Arial', 75)
    for i in range(9):
        for j in range(9):
            number = grid[i][j]
            if number != 0:
                color = BLACK if (i, j) in given_number_pos else BLUE

                textSurface = font.render(str(number), True, color)
                text_rect = textSurface.get_rect()

                text_rect.topleft = (j * SCREEN_WIDTH / 9 + SCREEN_WIDTH / 9 / 3, i * SCREEN_HEIGHT / 9)
                screen.blit(textSurface, text_rect)


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku solver")

    run = True
    start_solve = True
    thread = threading.Thread(target=solve, args=(grid,))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_grid(screen)
        draw_numbers(screen, grid)

        if start_solve:
            thread.start()
            start_solve = False

        pygame.display.update()
