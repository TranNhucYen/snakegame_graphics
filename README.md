# snakegame_graphics

## Cấu trúc dự án 
  main.py: Tập tin chính khởi chạy trò chơi và quản lý vòng lặp game.

  graphics.py: Chứa các hàm xử lý đồ họa như vẽ lưới, viền, rắn, thức ăn, điểm số và thông báo game over.

  logic.py: Chứa các hàm xử lý logic của trò chơi, bao gồm tạo vị trí thức ăn, thuật toán BFS tìm đường đi, và cập nhật vị trí rắn.

  imgs: Thư mục chứa hình ảnh cần thiết cho trò chơi (ví dụ: snake_head.png và food.png).
    
## Tùy chỉnh

  điều chỉnh tốc độ rắn "main.py" => 
  
    clock.tick(100)
  
  chọn chế độ thủ công hoặc tự động ở "main.py" => 
  
    direction = auto_move(snake, food, COLS, ROWS, direction) #hoặc
    direction = manual_move(direction)

## Phần chính 
  thay đổi lại thuật toán BFS ở hàm "bfs_path"
