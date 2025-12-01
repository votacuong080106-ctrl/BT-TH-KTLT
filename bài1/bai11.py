# Võ Tá Cường , MSV: 245752021610100
# Khởi tạo các danh sách
l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]

# 1. Tạo danh sách 'm' chứa hai danh sách 'l' và 'k'
m = []
m.append(l) # m = [[1, 'python', 4, 7]]
m.append(k) # m = [[1, 'python', 4, 7], ['cse', 2, 'guntur', 8]]

# In danh sách 'm' (chứa hai danh sách con)
print("Danh sách 'm' chứa l và k:")
print(m)

# 2. Tạo từ điển 'd' để 'kết nối' (lưu trữ) các danh sách
# LỖI CÚ PHÁP ĐÃ SỬA: Trong dictionary, các cặp key:value phải được ngăn cách bằng dấu phẩy (,)
# Dùng: {1: l, 2: k, 'combine_list': m}
d = {1: l, 2: k, 'combine_list': m}

# In từ điển 'd'
print("\nTừ điển 'd' kết nối các danh sách:")
print(d)