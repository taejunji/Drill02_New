from pico2d import *
import math

open_canvas()

# fill here
character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def render_frame(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.1)

def run_circle():
    print('Circle')
    r,cx,cy = 200,400,300
    for deg in range(0,360,5):
        x = cx + r*math.cos(math.radians(deg))
        y = cy + r*math.sin(math.radians(deg))
        render_frame(x,y)

def run_rectangle():
    print('Rectangle')

    #bottom Line
    for x in range(50,750+1,5):
      render_frame(x,90)
    #top Line
    for x in range(750,50-1,-5):
        render_frame(x,550)


while True:
    #run_circle()
    run_rectangle()
    break



close_canvas()
