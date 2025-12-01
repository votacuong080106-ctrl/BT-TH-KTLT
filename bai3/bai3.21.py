# Võ Tá Cường , MSV: 245752021610100
data = input("Nhập chuỗi các số nhị phân 4 chữ số (cách nhau bởi dấu phẩy): ")

# Tách chuỗi thành danh sách
items = data.split(',')

# Danh sách chứa các số chia hết cho 5
result = []

for b in items:
    if int(b, 2) % 5 == 0:   # Chuyển nhị phân sang thập phân rồi kiểm tra chia hết 5
        result.append(b)

# In kết quả
print(",".join(result))
