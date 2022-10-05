from pico2d import *

def handle_events():
    # fill here
    # 좌우 움직이기!!!!
    global running
    global x #바깥쪽에 정의된 X이다!
    global y #일단 추가
    global xdir
    global ydir

    events = get_events() #1. 입력 이벤트 폴링
    for event in events:
        if event.type == SDL_QUIT: #2. 이벤트 종류 구분
            running = False
        elif event.type == SDL_KEYDOWN:

            # 아래 Tab키로 띄어쓰기 중요함
            if event.key == SDLK_RIGHT:  # 오른쪽 #3. 이벤트 실제 입력값 구하기
                xdir += 1  # 증가

            elif event.key == SDLK_LEFT:  # 왼쪽
                xdir -= 1  # 감소
                #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, -90)
                #update_canvas()

            elif event.key == SDLK_UP:
                ydir += 1

            elif event.key == SDLK_DOWN:
                ydir -= 1

            
            elif event.key == SDLK_ESCAPE:
                running = False


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1

            elif event.key == SDLK_UP:
                ydir -= 1

            elif event.key == SDLK_DOWN:
                ydir += 1




open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2 #이게 뭔 값이였지# #800 // 2 전체 캔버스800에서 절반을 사용하겠다 는 의미
xdir = 0
ydir = 0
y = 600 // 2 #얘는 내가 왜 넣었지.

frame = 0

while running:
    clear_canvas()
    grass.draw(400, 200)

    #if xdir == 1:
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                                                       #x, y) 로 수정하면 대각선으로 움직임.
                                                       #90, x)로 수정하면 좌, 우 키눌렀는데 위, 아래로 움직임.
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += xdir * 5
    y += ydir * 5
    delay(0.01)


close_canvas()
