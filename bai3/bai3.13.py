# Võ Tá Cường , MSV: 245752021610100
# Nhập một list từ bàn phím
ds = input("Nhập list: ").split()

# Tìm vị trí của phần tử 'abc'
if 'abc' in ds:
    print("Vị trí của chuỗi 'abc' là:", ds.index('abc'))
else:
    print("Phần tử 'abc' không có trong list!")
