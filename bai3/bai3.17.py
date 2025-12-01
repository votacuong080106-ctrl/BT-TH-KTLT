# Võ Tá Cường , MSV: 245752021610100
# Nhập số n
n = int(input("Nhập số n: "))

print("Các số nhỏ hơn", n, "có tổng các ước số lớn hơn chính nó là:")

# Duyệt qua các số từ 1 đến n-1
for i in range(1, n):
    tong_uoc = 0
    # Tính tổng các ước số của i (không bao gồm chính i)
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    # Kiểm tra điều kiện
    if tong_uoc > i:
        print(i)
