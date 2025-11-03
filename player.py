from pico2d import *

open_canvas()

class Character:
    def __init__(self, image):
        self.image = load_image('char1_1.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

def reset_world():
    pass
def update_world():
    pass
def render_world():
    pass

close_canvas()