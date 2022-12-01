from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('TUK_GROUND.png')
        # fill here
        self.bgm = load_music('football.mp3') #load_music는 mp3하고 ogg를 읽을 수 있음.
        self.bgm.set_volume(32)                    # 중요 : ground가 플레이 함. #
        self.bgm.repeat_play() #반복적으로 플레이

    def __getstate__(self):
        state = {}
        return state

    def __setstate__(self, state):
        self.__init__()

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280 // 2, 1024 // 2)

