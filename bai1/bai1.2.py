# Võ Tá Cường , MSV: 245752021610100
import math

# Nhập tọa độ điểm thứ nhất (nên dùng float để chính xác hơn)
x1 = float(input("Enter x1 --> "))
y1 = float(input("Enter y1 --> "))

# Nhập tọa độ điểm thứ hai
x2 = float(input("Enter x2 --> "))
y2 = float(input("Enter y2 --> "))

# Tính bình phương hiệu tọa độ (dùng toán tử lũy thừa ** hoặc math.pow() sẽ gọn hơn)
# d1 = (x2 - x1) ** 2
# d2 = (y2 - y1) ** 2
d1 = (x2 - x1) * (x2 - x1)
d2 = (y2 - y1) * (y2 - y1)

# Tính khoảng cách (res)
res = math.sqrt(d1 + d2)

# In kết quả
print("Distance between two points:", res)