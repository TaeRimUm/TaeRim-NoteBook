from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #elif event.type == SDL_MOUSEMOTION:
            #x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



open_canvas(TUK_WIDTH, TUK_HEIGHT)

# fill here
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True

#케릭터의 위치
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x,y = sx, sy

#화살표의 위치
ax, ay = x, y

frame = 0
hide_cursor()

t = 0
#세상 초기화
def reset_world():

    global ax, ay
    global t
    global sx, sy

    ax, ay = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    t=0
    sx , sy = x, y
    #화살표 위치를 정한 후, t 초기화, 현재의 x, y위치 초기화

    pass

#계속 호출하니까 t의 값을 0부터 랜덤으로
def update_world():

    global x, y
    global t

    t += 0.001 #속도가 빠르면 t의 값을 줄이기
    x = (1-t) * sx + t * ax
    y = (1-t) * sy + t * ay

    if t >= 1.0:
        reset_world()

    pass

reset_world()

#무한루프돌면서
while running:

    update_world()

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    arrow.draw(ax, ay) #(ax, ay, 100, 100)

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


    update_canvas()
    frame = (frame + 1) % 8
    handle_events()


close_canvas()


#마우스랑 캐릭터 x죄표가
#[ 캐릭터 마우스 ]에서 마우스의 x값이 캐릭터의 x값보다 크면 캐릭터가 오른쪽으로 가는거, 작으면 [ 마우스 캐릭터 ] 니까 왼쪽으로 가는거 출력


