# Võ Tá Cường , MSV: 245752021610100
import math  # Thư viện toán học để dùng hằng số pi

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính

    def area(self):
        return math.pi * self.radius ** 2  # Diện tích: πr²

    def circumference(self):
        return 2 * math.pi * self.radius  # Chu vi: 2πr

# Ví dụ sử dụng
c = Circle(5)  # Bán kính r = 5
print("Diện tích:", c.area())          # In diện tích
print("Chu vi:", c.circumference())    # In chu vi
