from pico2d import *

def move_charater():
    global running
    global xdir, ydir, t

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                xdir = -1
                t = 0
            elif event.key == SDLK_RIGHT:
                xdir = 1
                t = 1

            elif event.key == SDLK_UP:
                ydir = 1
            elif event.key == SDLK_DOWN:
                ydir = -1

            elif event.key == SDLK_ESCAPE:
                running = False


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                xdir = 0
                t = 2
            elif event.key == SDLK_RIGHT:
                xdir = 0
                t = 3

            elif event.key == SDLK_UP:
                ydir = 0
            elif event.key == SDLK_DOWN:
                ydir = 0

open_canvas()
charater = load_image('SayBar.png')

running = True
x, y = 800//2, 600//2
xdir = 0
ydir = 0
t = 3 #기본 멈춰있는 애니 위치
frame = 0

while running:
    clear_canvas()
    move_charater()
    charater.clip_draw(frame * 100, 100 * t, 100, 100, x, y)
    x = x + xdir * 10
    y = y + ydir * 10
    update_canvas()

    delay(0.05)
    frame = (frame + 1) % 8

close_canvas()
