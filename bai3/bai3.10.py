# Võ Tá Cường , MSV: 245752021610100
# Nhập một list từ bàn phím
ds = input("Nhập list: ").split()

# Cắt list: bỏ phần tử đầu và cuối
x = ds[1:-1]

# In các phần tử sau khi cắt
for c in x:
    print(c)
