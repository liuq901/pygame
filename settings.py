screen_width = 1200
screen_height = 800

bg_color = (230, 230, 230)

ship_limit = 3

bullet_width = 3
bullet_height = 15
bullet_color = (60, 60, 60)
bullet_limit = 5

alien_row_number = 3
alien_col_number = 8
alien_drop_speed = 10

button_width = 200
button_height = 50
button_color = (0, 255, 0)
button_text_color = (255, 255, 255)

def init():
    global ship_speed
    global bullet_speed
    global alien_speed

    ship_speed = 1.5
    bullet_speed = 1.0
    alien_speed = 1.0

def level_up():
    global ship_speed
    global bullet_speed
    global alien_speed

    speedup_scale = 1.1

    ship_speed *= speedup_scale
    bullet_speed *= speedup_scale
    alien_speed *= speedup_scale
