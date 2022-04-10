# https://py2.codeskulptor.org/#user49_x34bor7CmS_3.py
import simplegui
import random

TILE_WIDTH = 8
TILE_HEIGHT = 8
RIGHT = (TILE_WIDTH, 0)
DOWN = (0, TILE_HEIGHT)
LEFT = (-TILE_WIDTH, 0)
UP = (0, -TILE_HEIGHT)
WIDTH = TILE_WIDTH * 50
HEIGHT = TILE_HEIGHT * 50
UP_KEYS = ['up', 'w', 'k']
LEFT_KEYS = ['left', 'a', 'h']
RIGHT_KEYS = ['right', 'd', 'l']
DOWN_KEYS = ['down', 's', 'j']

SNAKE_LINE_WIDTH = 1
SNAKE_LINE_COLOR = "gray"
SNAKE_FILL_COLOR = "gray"

WALL_LINE_WIDTH = 1
WALL_LINE_COLOR = "red"
WALL_FILL_COLOR = "red"

snake = [[WIDTH/2, HEIGHT/2]]
add_to_snake_length = 4
moving_dir = RIGHT

walls = []
berries = []
next_move = RIGHT

time_to_move = 5
berry_interval = 1000
max_berries = 4
current_frame = 0
is_game_over = False
game_over_pause = 800

def new_game():
    global snake, add_to_snake_length, berries, is_game_over
    snake = [[WIDTH/2, HEIGHT/2]]
    add_to_snake_length = 4
    berries = []
    is_game_over = False

    
    
def up_is_pressed(key):
    for k in UP_KEYS:
        if simplegui.KEY_MAP[k] == key:
            return True
    return False

def left_is_pressed(key):
    for k in LEFT_KEYS:
        if simplegui.KEY_MAP[k] == key:
            return True
    return False

def down_is_pressed(key):
    for k in DOWN_KEYS:
        if simplegui.KEY_MAP[k] == key:
            return True
    return False

def right_is_pressed(key):
    for k in RIGHT_KEYS:
        if simplegui.KEY_MAP[k] == key:
            return True
    return False

def key_handler(key):
    global moving_dir, next_move
    if up_is_pressed(key) and moving_dir != DOWN:
        next_move = UP
    elif right_is_pressed(key) and moving_dir != LEFT:
        next_move = RIGHT
    elif down_is_pressed(key) and moving_dir != UP:
        next_move = DOWN
    elif left_is_pressed(key) and moving_dir != RIGHT:
        next_move = LEFT
        
def update():
    global add_to_snake_length, next_move, moving_dir
    global snake, is_game_over
    last_pos = []
    moving_dir = next_move
    if add_to_snake_length > 0:
        last_pos = [snake[-1][0], snake[-1][1]]
        snake.append(last_pos)
        add_to_snake_length -= 1

    for i in range(len(snake) - 1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    
    snake[0][0] = snake[0][0] + moving_dir[0]
    snake[0][1] = snake[0][1] + moving_dir[1]
    
    if worm_game_over():
        game_over_timer.start()
        is_game_over = True
        
def berry_handler():
    if len(berries) > max_berries:
        return
    
    p = [0, 0]
    while space_is_empty(p) == False :
        p[0] = random.randrange(0, WIDTH, TILE_WIDTH)
        p[1] = random.randrange(0, HEIGHT, TILE_HEIGHT)
    berries.append(p)


def space_is_empty(p):
    for s in snake:
        if p[0] == s[0] and p[1] == s[1]:
            return False
    for w in walls:
        if p[0] == w[0] and p[1] == w[1]:
            return False
    for b in berries:
        if p[0] == b[0] and p[1] == b[1]:
            return False
    return True

# Handler to draw on canvas
def draw(canvas):
    global current_frame, time_to_move
 
    current_frame += 1
    if current_frame > time_to_move:
        if not is_game_over:
            update()
            current_frame = 0
            check_worm_eats_berry()
        
    for s in snake:
        draw_tile(canvas, s, SNAKE_LINE_WIDTH, SNAKE_LINE_COLOR, SNAKE_FILL_COLOR)
    for w in walls:
        draw_tile(canvas, w, WALL_LINE_WIDTH, WALL_LINE_COLOR, WALL_FILL_COLOR)
    for b in berries:
        draw_tile(canvas, b, 1, "blue", "blue")
        
def check_worm_eats_berry():
    global add_to_snake_length
    index = []
    for i in range(len(berries)):
        if snake[0] == berries[i]:
            add_to_snake_length += 4
            index.append(berries[i])
    for i in range(len(index)):
        berries.remove(index[i])

def worm_game_over():
    for w in walls:
        if snake[0] == w:
            return True
    for s in snake[1:]:
        if snake[0] == s:
            return True
    return False

def new_game_handler():
    new_game()
    game_over_timer.stop()
    
    
def draw_tile(canvas, tile, line_width, line_color, fill_color):
    p2 = [tile[0] + TILE_WIDTH, tile[1]]
    p3 = [tile[0] + TILE_WIDTH, tile[1] + TILE_HEIGHT]
    p4 = [tile[0], tile[1] + TILE_HEIGHT]
    canvas.draw_polygon([tile, p2, p3, p4], line_width, line_color, fill_color)
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
for x in range(0, WIDTH, TILE_WIDTH):
    walls.append([x, 0])
    walls.append([x, HEIGHT - TILE_WIDTH])

for y in range(0, HEIGHT, TILE_HEIGHT):
    walls.append([0, y])
    walls.append([WIDTH - TILE_WIDTH, y])

berry_timer = simplegui.create_timer(berry_interval, berry_handler)
berry_timer.start()

game_over_timer = simplegui.create_timer(game_over_pause, new_game_handler)
# Start the frame animation
frame.start()

