from pico2d import *


def handle_events():
    # fill here
    # 좌우 움직이기!!!!
    global running
    global x
    global y  # 바깥쪽에 정의된 X이다!
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:

            # 아래 Tab키로 띄어쓰기 존내 중요함
            if event.key == SDLK_RIGHT:  # 오른쪽
                x = x + 10  # 증가
        elif event.key == SDLK_LEFT:  # 왼쪽
            x = x - 10  # 감소

        elif event.key == SDLK_UP:
            y = y + 10
        elif event.key == SDLK_DOWN:
            y = y - 10

        elif event.key == SDLK_ESCAPE:
            running = False


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = 800 // 2
pass
# 존내빠르게 호다다다다다닥하고 달림

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()
