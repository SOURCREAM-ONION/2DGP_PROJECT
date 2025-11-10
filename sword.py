from pico2d import *
from state_machine import StateMachine
from character import Character

class Idle_Sword:
    def __init__(self, sword):
        self.sword = sword
        self.frame = 0 # 검 대기 애니메이션 프레임 초기화
        self.frame_count = 6 # 검 대기 애니메이션 프레임 수

    def enter(self):
        self.frame = 0

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        import math
        self.sword.image.clip_composite_draw(0, 0, 122, 122, -math.pi / 2, '' ,self.sword.x, self.sword.y, 50, 50)

class Wield_Sword:
    def __init__(self, sword):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Sword:
    def __init__(self):
        self.x, self.y = 405, 87 # 검의 초기 위치
        self.image = load_image('basic_sword.png') # 검의 이미지 로드
        self.IDLE_SWORD = Idle_Sword(self)
        self.WIELD_SWORD = Wield_Sword(self)
        self.state_machine = StateMachine(self.IDLE_SWORD)



    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        pass
