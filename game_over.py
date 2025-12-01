from pico2d import *
import game_framework
import play_mode
import title_mode

image = None

def init():
    global image
    image = load_image('EndBackground.png')

def finish():
    global image
    del image

def update():
    pass

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw_to_origin(0,0, 400, 600)
    update_canvas()