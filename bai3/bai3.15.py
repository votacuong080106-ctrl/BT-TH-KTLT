# Võ Tá Cường , MSV: 245752021610100
# Nhập chuỗi từ bàn phím
s = input("Nhập các từ tiếng Anh, cách nhau bởi dấu cách: ")

# Tách chuỗi thành danh sách các từ
words = s.split()

# Sắp xếp các từ theo thứ tự từ điển (a → z)
words.sort()

# In kết quả ra màn hình
print("Các từ theo thứ tự từ điển:")
for w in words:
    print(w)
