from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    # running에 물결표 = "이거 문제가 생길 수 있어연."
    # C언어였으면 int running이지만, 함수내에 있는 지역변수로 인식함.
    # 앞에 global running 을 써줘야 "이친구는 전체에 쓰일거야!" 라는 의미임. 넣어줘야 물결표가 없어짐.
    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)

close_canvas()

