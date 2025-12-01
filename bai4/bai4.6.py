# Võ Tá Cường , MSV: 245752021610100
import mylistmodule as mlm

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập các phần tử
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sắp xếp danh sách
sorted_lst = mlm.sort_list(lst)
print("Danh sách đã sắp xếp:", sorted_lst)

# Tìm giá trị lớn nhất và nhỏ nhất
max_val = mlm.max_element(lst)
min_val = min(lst)
print("Phần tử lớn nhất:", max_val)
print("Phần tử nhỏ nhất:", min_val)

# Tìm vị trí (index) của phần tử lớn nhất và nhỏ nhất
max_index = lst.index(max_val)
min_index = lst.index(min_val)
print("Vị trí phần tử lớn nhất:", max_index)
print("Vị trí phần tử nhỏ nhất:", min_index)
