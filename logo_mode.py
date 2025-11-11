from pico2d import *

image = None
running = True
logo_start_time = 0.0

def init():
    global image, logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    global image
    del image

def update():
    global running
    current_time = get_time()
    if current_time - logo_start_time >= 2.0:
        running = False

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()