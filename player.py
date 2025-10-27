from pico2d import *

open_canvas()

character = load_image('char1_1.png')

clear_canvas()
character.clip_draw(0,0,30,30,400,300,200,200)
update_canvas()
delay(1)

close_canvas()