# Võ Tá Cường , MSV: 245752021610100
import numpy as np

# Định nghĩa kiểu dữ liệu có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Danh sách thông tin sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In mảng gốc
print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao
sorted_students = np.sort(students, order='height')
print("Sorted by height:")
print(sorted_students)
