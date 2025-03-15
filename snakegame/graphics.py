import pygame

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (170, 215, 81)
DARK_GREEN = (162, 209, 73)
RED = (255, 0, 0)
SNAKE_COLOR = (71, 114, 255)
BORDER_COLOR = (80, 200, 120)
TEXT_COLOR = WHITE

def load_image(path, size):
    """Tải ảnh từ file và thay đổi kích thước."""
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (size, size))

def draw_grid(screen, rows, cols, cell_size, border_thickness):
    """Vẽ lưới ô vuông của trò chơi."""
    for row in range(rows):
        for col in range(cols):
            color = GREEN if (row + col) % 2 == 0 else DARK_GREEN
            rect = (col * cell_size + border_thickness, row * cell_size + border_thickness, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)

def draw_border(screen, width, height, border_thickness):
    """Vẽ viền bàn cờ."""
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, width + 2 * border_thickness, border_thickness))
    pygame.draw.rect(screen, BORDER_COLOR, (0, height + border_thickness, width + 2 * border_thickness, border_thickness))
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, border_thickness, height + 2 * border_thickness))
    pygame.draw.rect(screen, BORDER_COLOR, (width + border_thickness, 0, border_thickness, height + 2 * border_thickness))

def draw_snake(screen, snake, direction, cell_size, border_thickness, snake_head_img):
    """Vẽ rắn với hình ảnh đầu rắn quay đúng hướng."""
    angle = { (1, 0): 0, (-1, 0): 180, (0, -1): 90, (0, 1): -90 }[direction]
    rotated_head = pygame.transform.rotate(snake_head_img, angle)
    
    screen.blit(rotated_head, (snake[0][0] * cell_size + border_thickness, snake[0][1] * cell_size + border_thickness))
    for segment in snake[1:]:
        segment_rect = (segment[0] * cell_size + border_thickness, segment[1] * cell_size + border_thickness, cell_size, cell_size)
        pygame.draw.rect(screen, SNAKE_COLOR, segment_rect, border_radius=4)

def draw_food(screen, food, cell_size, border_thickness, food_img):
    """Vẽ thức ăn trên màn hình."""
    screen.blit(food_img, (food[0] * cell_size + border_thickness, food[1] * cell_size + border_thickness))

def draw_score(screen, score, font):
    """Hiển thị điểm số trên màn hình."""
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

def show_game_over(screen, width, height, border_thickness, font):
    """Hiển thị thông báo game over."""
    game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
    text_rect = game_over_text.get_rect(center=(width // 2 + border_thickness, height // 2 + border_thickness))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
