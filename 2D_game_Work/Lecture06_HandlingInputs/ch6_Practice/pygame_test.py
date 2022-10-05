to_x = 0
to_y = 0

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
        ​​​​for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
            ​​​​​​​​if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                ​running = False

            if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
                ​​if event.key == pygame.K_LEFT: #왼쪽 방향키가 눌렸을 때
​​​​​​​​​​​​​​​​                    to_x -= 0.5
            ​​​​​​​​​​​​elif event.key == pygame.K_RIGHT: #오른쪽 방향키가 눌렸을 때
​​​​​​​​​​​​​​​​                    to_x += 0.5
            elif event.key == pygame.K_DOWN: #아래쪽 방향키가 눌렸을 때
​​​​​​​​​​​​​​​​                    to_y += 0.5
​​​​​​​​​​​​            elif event.key == pygame.K_UP: #위쪽 방향키가 눌렸을 때
​​​​​​​​​​​​​​​​                    to_y -= 0.5

​​​​​​​​            if event.type == pygame.KEYUP: #방향키를 뗐을 때 캐릭터 멈춤
​​​​​​​​​​​​                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
​​​​​​​​​​​​​​​​                    to_x = 0
​​​​​​​​​​​​                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
​​​​​​​​​​​​​                    ​​​to_y = 0

        ​​​character_x_pos += to_x
​        ​​​character_y_pos += to_y
