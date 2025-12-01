# Võ Tá Cường , MSV: 245752021610100
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sắp xếp theo nhiều cột: chiều cao trước, id sinh viên sau (nếu muốn)
# lexsort dùng thứ tự từ cuối lên đầu, nên id là thứ tự thứ hai
indices = np.lexsort((student_id, student_height))

print("Chỉ số sắp xếp:")
print(indices)

print("Dữ liệu sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])
