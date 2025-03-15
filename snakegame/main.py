import pygame
import sys
from graphics import *
from logic import *

def main():
    pygame.init()
    
    ROWS, COLS = 20, 20
    CELL_SIZE = 30
    BORDER_THICKNESS = CELL_SIZE
    WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

    screen = pygame.display.set_mode((WIDTH + 2 * BORDER_THICKNESS, HEIGHT + 2 * BORDER_THICKNESS))
    pygame.display.set_caption("Snake Game")
    
    font = pygame.font.SysFont("Arial", 24)
    snake_head_img = load_image("./imgs/snake_head.png", CELL_SIZE)
    food_img = load_image("./imgs/food.png", CELL_SIZE)

    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)
    food = create_food(snake, COLS, ROWS)
    score = 0
    clock = pygame.time.Clock()
    running, game_over = True, False

    while running:
        screen.fill(WHITE)
        draw_grid(screen, ROWS, COLS, CELL_SIZE, BORDER_THICKNESS)
        draw_border(screen, WIDTH, HEIGHT, BORDER_THICKNESS)
        draw_snake(screen, snake, direction, CELL_SIZE, BORDER_THICKNESS, snake_head_img)
        draw_food(screen, food, CELL_SIZE, BORDER_THICKNESS, food_img)
        draw_score(screen, score, font)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score, game_over = [(10, 10), (9, 10), (8, 10)], (1, 0), create_food(snake, COLS, ROWS), 0, False
                elif event.key == pygame.K_q:
                    running = False
        
        if not game_over:
            direction = auto_move(snake, food, COLS, ROWS, direction)
            success, snake, food, gained_score = move_snake(snake, food, direction, COLS, ROWS)
            if not success:
                game_over = True
            score += gained_score
            pygame.display.flip()

            # Tốc độ rắn
            clock.tick(100)
        else:
            show_game_over(screen, WIDTH, HEIGHT, BORDER_THICKNESS, font)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
