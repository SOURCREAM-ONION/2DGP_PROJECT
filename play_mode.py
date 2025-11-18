from pico2d import *
import game_world
from character import Character
from sword import Sword
import game_framework
import title_mode
from building import Building


# 충돌 체크 함수 추가
def collide_bb(bb_a, bb_b):
    if bb_a is None or bb_b is None:  # None 체크 추가
        return False

    left_a, bottom_a, right_a, top_a = bb_a
    left_b, bottom_b, right_b, top_b = bb_b

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_MOUSEBUTTONDOWN or event.type == SDL_KEYDOWN:
            character.handle_event(event)
            sword.state_machine.handle_event(('INPUT', event))


def init():  # 월드가 새로 나올때 그려지는 부분
    global running
    global character
    global world
    global sword
    global building

    running = True
    world = []
    game_world.clear()

    sword = Sword()
    game_world.add_object(sword, 0)

    character = Character()
    game_world.add_object(character, 1)

    building = Building()
    game_world.add_object(building, 0)


def update():  # 월드에 객체가 추가되는 부분
    game_world.update()

    if sword.is_attacking():
        # 1층 충돌 체크
        if collide_bb(building.get_bb_floor1(), sword.get_bb()):
            building.destroy_floor(0)  # 1층만 파괴

        # 2층 충돌 체크
        if collide_bb(building.get_bb_floor2(), sword.get_bb()):
            building.destroy_floor(1)  # 2층만 파괴

        # 3층 충돌 체크
        if collide_bb(building.get_bb_floor3(), sword.get_bb()):
            building.destroy_floor(2)  # 3층만 파괴


def draw():  # 월드가 만들어지는 부분
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():  # 월드가 사라질때 지워지는 부분
    pass