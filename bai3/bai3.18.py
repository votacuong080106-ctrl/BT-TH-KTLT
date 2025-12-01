# Võ Tá Cường , MSV: 245752021610100
n = int(input("Nhập n: "))

# Tạo danh sách Fibonacci nhỏ hơn n
fibo = []
a, b = 0, 1

while a < n:
    fibo.append(a)
    a, b = b, a + b

print("Các số Fibonacci nhỏ hơn", n, "là:", fibo)
