from pico2d import *
import game_framework
import play_mode
import select_map
import select_character
import play_mode
from sword import Sword, WoodenSword, AncientSword, BloodSword, CheckinSword, CutterSword, GreenSword, IceSword, LibertySword, LightningSword, GoldenSword, NeptuneSword, NightSword, PinkSword, RosenSword, SharkSword, SyringeSword, BlackpinkSword


direction_image = None
background = None
character = None

def set_background(bg_class):
    global background
    if background:
        del background
    background = bg_class()

def set_character(char):
    global character
    if character:
        del character
    character = char()

def init():
    global sword_list
    global selection_index
    global current_sword
    global direction_image

    sword_list = [Sword, WoodenSword, AncientSword, BloodSword, CheckinSword, CutterSword, GreenSword, IceSword, LibertySword, LightningSword, GoldenSword, NeptuneSword, NightSword, PinkSword, RosenSword, SharkSword, SyringeSword, BlackpinkSword]
    selection_index = 0

    current_sword = sword_list[selection_index](character)

    direction_image = load_image("ui/Direction_21.png")

def finish():
    global current_sword
    global direction_image
    global background
    global character

    del current_sword
    del direction_image

    if background:
        del background
        background = None

    if character:
        del character
        character = None

def update():
    pass

def draw():
    clear_canvas()

    if background:
        background.draw()

    if character:
        character.draw()


    current_sword.draw()

    if direction_image:
        direction_image.draw(430, 360, 100, 100)
        direction_image.composite_draw(0, 'h', 50, 360, 100, 100)

    update_canvas()

def handle_events():
    global selection_index, current_sword

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_mode(select_character)
            elif event.key == SDLK_LEFT: # 왼쪽 화살표 키 입력
                selection_index = (selection_index - 1) % len(sword_list)
                direction_image.composite_draw(0, 'h', 60, 360, 120, 120)
                update_canvas()
                del current_sword
                current_sword = sword_list[selection_index](character)
            elif event.key == SDLK_RIGHT: # 오른쪽 화살표 키 입력
                selection_index = (selection_index + 1) % len(sword_list)
                direction_image.draw(430, 360, 100, 100)
                direction_image.composite_draw(0, 'h', 50, 360, 100, 100)
                update_canvas()
                del current_sword
                current_sword = sword_list[selection_index](character)
            elif event.key == SDLK_SPACE:
                selected_character = sword_list[selection_index]
                play_mode.set_background_class()
                play_mode.set_sword_class(selected_character)
                game_framework.change_mode(play_mode)