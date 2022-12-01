import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    eat_sound = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, get_canvas_width()-1), random.randint(0, get_canvas_height()-1)

        # fill here
        if Ball.eat_sound is None:
            Ball.eat_sound = load_wav('pickup.wav')
            Ball.eat_sound.set_volume(32)

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)



    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_collision(self, other, grou):
        # fill here
        # 볼이 먹힐 때, 충돌 처리되어 없어질 때,
        Ball.eat_sound.play() #class 변수. 볼마다 사운드를 바꿀 필요가 없음. -> 16줄로 감.
        game_world.remove_object(self)
