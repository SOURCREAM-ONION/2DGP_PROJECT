from pico2d import load_image


class Idle:
    def __init__(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

class Character:
    def __init__(self): # 캐릭터가 처음 생성될 때 나오는 부분
        self.x, self.y = 400, 300 # 캐릭터의 초기 위치
        self.frame = 0 # 캐릭터의 프레임 초기화
        self.image = load_image('Char1_1.png') # 캐릭터의 이미지 로드

    def draw(self):  # 캐릭터가 그려지는 부분
        self.image.clip_draw(self.frame * 30, 30, 30, 30, 400, 300) # 캐릭터의 이미지에서 프레임에 맞게 그리기

    def update(self): # 캐릭터가 업데이트 되는 부분
        self.frame = (self.frame + 1) % 3 # 프레임을 0, 1, 2로 순환시키기 (3프레임 애니메이션)
