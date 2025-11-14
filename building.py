from pico2d import *

class Building:
    def __init__(self):
        self.x, self.y = 200, 300 # 건물의 초기 위치
        self.building = load_image('Building1.png')

    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        self.building.draw_now()