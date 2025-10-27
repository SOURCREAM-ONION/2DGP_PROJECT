from pico2d import *

open_canvas()

character = load_image('char1_1.png')
sword = load_image('basic_sword.png')
'''
frame = 0
while True:
    clear_canvas()
    character.clip_draw(frame * 30, 30, 30, 30, 400, 300, 50, 50)
    frame = (frame + 1) % 3
    update_canvas()
    delay(0.1)
'''

frame = 0
while True:
    clear_canvas()
    sword.clip_draw(frame * 203, 0, 203, 350, 400, 300, 50, 50)
    frame = (frame + 1) % 10
    update_canvas()
    delay(0.1)


close_canvas()