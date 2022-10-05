import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0]. p2[1]

    a = (y2-y1)/(x2-x1)
    #결정적인 문제 : (x2-x1)이 0이 되면 나눗셈을 할 수 없다.
    b = y1 - a * x1

    for x in range(x2, x1 + 1, 5):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

def draw_line(p1, p2):
    # fill here
    draw_big_point(p1) #p1 적고 쉬프트 엔터
    draw_big_point(p2)

    #촘촘하게 할려면 range의 값을 줄이면 됨
    for i in range(0, 100 + 1, 2):
        t = i / 100

        #(1-t) + t 의 비울로
        x = (1-t) *p1[0] + t *p2[0] #x1, x2
        y = (1-t) *p1[1] + t *p2[1] #y1, y2
        draw_point((x, y))

    draw_point(p2)

    pass


prepare_turtle_canvas()

draw_line((-200, -100), (300, 150))
turtle.done()

# fill here
#draw_linf_base((100,200), (100, -150)) 일 경우,
#division by zero : 0이 나외서 나숫셈을 할 수 없다는 오류

turtle.done()