import random

def create_food(snake, cols, rows):
    """Tạo vị trí thức ăn không trùng với rắn."""
    food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
    while food in snake:
        food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
    return food


# Nơi tạo thuật toán tìm kiếm đường đi 
def bfs_path(snake, food, cols, rows):
    """Tìm đường đi ngắn nhất bằng thuật toán BFS."""
    start = snake[0]
    obstacles = set(snake[1:])
    queue = [(start, [start])]
    visited = {start}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        pos, path = queue.pop(0)
        if pos == food:
            return path
        for d in directions:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if (0 <= next_pos[0] < cols and 0 <= next_pos[1] < rows 
                    and next_pos not in obstacles and next_pos not in visited):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos]))
    return None

# Tự động di chuyển theo thuật toán bfs
def auto_move(snake, food, cols, rows, current_direction):
    """Xác định hướng di chuyển tự động dựa trên BFS."""
    path = bfs_path(snake, food, cols, rows)
    if path and len(path) >= 2:
        next_cell = path[1]
        head = snake[0]
        return (next_cell[0] - head[0], next_cell[1] - head[1])
    
    # Nếu thuật toán không tìm được đường đi thì di chuyển theo hướng hiện tại
    return current_direction

def move_snake(snake, food, direction, cols, rows):
    """Cập nhật vị trí rắn, kiểm tra va chạm."""
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if new_head in snake or new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
        return False, snake, food, 0  # Game over
    
    snake.insert(0, new_head)
    if new_head == food:
        return True, snake, create_food(snake, cols, rows), 1
    else:
        snake.pop()
        return True, snake, food, 0
