# Võ Tá Cường , MSV: 245752021610100
import math

pos = [0, 0]  # Vị trí ban đầu của robot (tọa độ y, x)

while True:
    s = input()  # Nhập hướng di chuyển, ví dụ: "UP 5"
    if not s:    # Nếu người dùng nhấn Enter (dòng trống) => kết thúc nhập
        break

    movement = s.split(" ")  # Tách chuỗi thành 2 phần: hướng và số bước
    direction = movement[0]  # Hướng di chuyển
    steps = int(movement[1]) # Số bước (đổi sang số nguyên)

    # Cập nhật vị trí robot theo hướng
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass  # Nếu nhập sai hướng, bỏ qua

# Tính khoảng cách từ (0,0) đến (x,y) theo định lý Pythagoras
distance = math.sqrt(pos[1]**2 + pos[0]**2)

# In ra kết quả làm tròn đến số nguyên gần nhất
print(int(round(distance)))

