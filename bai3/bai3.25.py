# Võ Tá Cường , MSV: 245752021610100
data = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")

# Tách thành danh sách chuỗi
items = data.split(',')

# Lọc số lẻ
odds = []

for x in items:
    if int(x) % 2 == 1:   # kiểm tra số lẻ
        odds.append(x)

print(",".join(odds))
