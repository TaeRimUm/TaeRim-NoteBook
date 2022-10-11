from pico2d import *
import game_framework
import play_state

running = True
image = None
logo_time = 0.0


# fill here

def enter():
    # fill here
    global image
    image = load_image('tuk_credit.png')

    pass

def exit():
    # fill here
    global image
    del image

    pass

def update():
    # fill here
    global logo_time
    global running
    if logo_time > 0.5:
        logo_time = 0
        #running = False
        game_framework.change_state(play_state)

    delay(0.01)
    logo_time += 0.01

    pass

def draw():
    # fill here
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

    pass

def handle_events():
    events = get_events()





