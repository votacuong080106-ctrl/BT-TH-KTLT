# Võ Tá Cường , MSV: 245752021610100
import turtle

# Tạo cửa sổ
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo turtle vẽ
painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

# Vẽ 180 hình vuông xoay dần
for i in range(180):
    painter.left(18)
    drawsq(painter, 200)

turtle.done()