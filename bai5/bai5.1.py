# Võ Tá Cường , MSV: 245752021610100
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

# Tạo đối tượng và tính diện tích
aCircle = Circle(2)
print(aCircle.area())
