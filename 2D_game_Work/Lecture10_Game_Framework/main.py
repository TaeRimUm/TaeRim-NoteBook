import pico2d
import logo_state

start_state = logo_state
#boy_grass_object 파일명 => start_state

pico2d.open_canvas()
start_state.enter()
# game main loop code
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    pico2d.delay(0.05)
start_state.exit()
pico2d.close_canvas()

