from pico2d import *
from state_machine import StateMachine
from character import Character

class Idle_Sword:
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
        self.x, self.y = 400, 90 # 검의 초기 위치
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
