class StateMachine:
    def __init__(self, start_state):
        self.current_state = start_state # 초기 상태를 시작상태로 설정
        self.current_state.enter() # 시작 상태

    def update(self):
        self.current_state.do() # 현재 상태를 계속 실행

    def draw(self):
        self.current_state.draw() # 현재 상태의 draw 메서드 호출
