# Võ Tá Cường , MSV: 245752021610100
# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Tạo dictionary chứa cặp (i, i*i)
result = {}   # khởi tạo dictionary rỗng
for i in range(1, n + 1):
    result[i] = i * i

# In dictionary
print(result)
