import game_world
from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from play_state import collide

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for ball in balls.copy():
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)