from pico2d import *

class Building:
    def __init__(self):
        self.x, self.y = 200, 500 # 건물의 초기 위치
        self.building = load_image('Building1.png') # 건물 이미지 로드
        self.framex = 450 # 건물 프레임 크기 x
        self.framey = 100 # 건물 프레임 크기 y

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        if self.y > 20: # 건물이 y좌표 20이 될때까지
            self.y -= 0.5 # 건물이 y좌표로 내려옴

    def do(self):
        pass

    def get_bb(self):
        return self.x - 200, self.y - 15, self.x + 200, self.y + 325 # 건물의 충돌 박스 좌표 반환

    def draw(self):
        self.building.clip_draw(0, 307, 1080, 307, self.x, self.y, self.framex, self.framey)
        self.building.clip_draw(0, 614, 1080, 307, self.x, self.y + 101, self.framex, self.framey)
        self.building.clip_draw(0, 921, 1080, 307, self.x, self.y + 202, self.framex, self.framey)
        #self.building.clip_draw(0, 1228, 1080, 307, self.x, self.y + 110, self.framex, self.framey)
        #self.building.clip_draw(0, 1535, 1080, 307, self.x, self.y + 145, self.framex, self.framey)
        #self.building.clip_draw(0, 1842, 1080, 307, self.x, self.y + 180, self.framex, self.framey)
        #self.building.clip_draw(0, 2149, 1080, 307, self.x, self.y + 215, self.framex, self.framey)
        #self.building.clip_draw(0, 2456, 1080, 307, self.x, self.y + 250, self.framex, self.framey)
        #self.building.clip_draw(0, 2763, 1080, 307, self.x, self.y + 285, self.framex, self.framey)
        #self.building.clip_draw(0, 3070, 1080, 307, self.x, self.y + 320, self.framex, self.framey)
        draw_rectangle(*self.get_bb()) # 건물의 충돌 박스