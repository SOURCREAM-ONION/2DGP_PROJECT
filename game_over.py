from pico2d import *
import game_framework
import play_mode
import title_mode

image = None
font_gameover = None
font_esc = None
font_score = None

def init():
    global image, font_gameover, font_esc, font_score
    image = load_image('EndBackground.png')
    font_gameover = load_font('ENCR10B.ttf', 60)
    font_esc = load_font('ENCR10B.ttf', 25)
    font_score = load_font('ENCR10B.ttf', 30)

def finish():
    global image, font_gameover, font_esc, font_score
    del image
    del font_gameover
    del font_esc
    del font_score

def update():
    pass

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw_to_origin(0,0, 480, 720)
    font_gameover.draw(90, 530, 'Game Over', (255, 0, 0))
    font_esc.draw(115, 150, 'Press ESC to Title', (255, 255, 255))
    font_score.draw(150, 390, f'Score: {play_mode.score}', (255, 255, 255))

    update_canvas()