from pico2d import *

class PauseMenu:
    def __init__(self):
        self.image_restart = load_image("ui/Button_06.png") # 재시작 이미지
        self.image_quit = load_image("ui/Button_07.png") # 나가기 이미지

        # 버튼 위치 및 크기 설정
        self.center_x = 240
        self.center_y = 360

        # 버튼 크기
        self.button_size = 100 # 버튼 크기
        self.spacing = 80  # 버튼 간 간격

        # 재시작 버튼 위치
        self.restart_button_x = self.center_x - self.spacing
        self.restart_button_y = self.center_y

        # 나가기 버튼 위치
        self.quit_button_x = self.center_x + self.spacing
        self.quit_button_y = self.center_y

    def update(self):
        pass

    def draw(self):
        self.image_restart.draw(self.restart_button_x, self.restart_button_y, self.button_size, self.button_size)
        self.image_quit.draw(self.quit_button_x, self.quit_button_y, self.button_size, self.button_size)

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x, 720 - event.y  # 마우스 좌표 변환

            # 재시작 버튼 클릭 여부 확인
            if (self.restart_button_x - self.button_size / 2 <= mouse_x <= self.restart_button_x + self.button_size / 2 and
                self.restart_button_y - self.button_size / 2 <= mouse_y <= self.restart_button_y + self.button_size / 2):
                return 'restart'  # 재시작 이벤트 반환

            # 나가기 버튼 클릭 여부 확인
            if (self.quit_button_x - self.button_size / 2 <= mouse_x <= self.quit_button_x + self.button_size / 2 and
                self.quit_button_y - self.button_size / 2 <= mouse_y <= self.quit_button_y + self.button_size / 2):
                return 'quit'  # 나가기 이벤트 반환

        return None