# Võ Tá Cường , MSV: 245752021610100
# Nhập chuỗi các số nhị phân cách nhau bởi dấu phẩy
s = input("Nhập các số nhị phân (phân tách bởi dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
binary_list = s.split(',')

# In ra các giá trị vừa nhập
print("Các số nhị phân bạn đã nhập là:")
for b in binary_list:
    print(b.strip())   # .strip() để loại bỏ khoảng trắng thừa (nếu có)
