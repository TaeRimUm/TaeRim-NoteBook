
#복붙해서 코드에 넣기
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


#키입력(이벤트)받아서 좌우로 움직이기
def handle_events():
    global running
    global x #바깥쪽에 정의된 X이다!
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:

            #아래 Tab키로 띄어쓰기 존내 중요함
             if event.key == SDLK_RIGHT: #오른쪽
                x = x + 10 #증가
            elif event.key == SDLK_LEFT: #왼쪽
                x = x - 10 #감소
            elif event.key == SDLK_ESCAPE:
                running = False

open_canvas()
