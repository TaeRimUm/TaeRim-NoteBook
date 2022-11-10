from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from ball import Ball, BigBall

boy = None
grass = None
balls = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    global balls
    balls = [Ball() for i in range(10)]
    game_world.add_objects(balls, 1)
    game_world.add_object(boy, 1)
    game_world.add_collision_pairs(boy, balls, 'boy:ball')


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for ball in balls.copy():
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
    for ball in balls:
        if collide(grass, ball):
            ball.stop()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group) #큰놈이 와서 박았는지, 작은놈이 와서 박았는지.
            b.handle_collision(a, group) #충돌처리를 하라고 명령.

    # 충돌 체크.
    # 볼들과 소년의 충돌
    # for ball in balls:


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_a: return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
