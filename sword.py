from pico2d import *
from state_machine import StateMachine
from character import Character

class Sword:
    def __init__(self):
        self.x, self.y = 400, 90 # 검의 초기 위치
        self.image = load_image('basic_sword.png') # 검의 이미지 로드
        self.state_machine = StateMachine()

    def update(self):
        self.state_machine.update() # 상태 머신의 업데이트 호출

    def draw(self):
        self.image.draw(self.x, self.y) # 검의 이미지 그리기

    def handle_event(self, event):
        self.state_machine.handle_event(event) # 상태 머신의 이벤트 처리 호출