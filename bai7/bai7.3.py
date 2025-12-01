# Võ Tá Cường , MSV: 245752021610100
import turtle

# Tạo màn hình
window = turtle.Screen()
window.bgcolor("white")

# Tạo turtle
painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0)

# Danh sách màu lặp lại như hình mẫu
colors = ["red", "green", "blue"]

# Vẽ 36 vòng tròn xoay góc 10 độ
for i in range(36):
    painter.pencolor(colors[i % 3])   # Lặp màu đỏ – xanh lá – xanh dương
    painter.circle(100)
    painter.left(10)

turtle.done()