from turtle import *

p = Pen()
p.color("red", "yellow")        # 펜 색깔은 빨강, 칠하는 색은 노랑
p.pendown()
p.begin_fill()                  # 도형 내부를 칠함

while True:
    p.forward(200)
    p.left(170)
    print(p.pos())

    if abs(p.pos()) < 1:
        break

p.end_fill()
done()