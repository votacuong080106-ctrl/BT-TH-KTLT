# Võ Tá Cường , MSV: 245752021610100
import math

P = []

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(math.sqrt(x))
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True

# Tạo tuple P gồm các số nguyên tố < 1.000.000
for num in range(1_000_000):
    if is_prime(num):
        P.append(num)

P = tuple(P)

print("Số lượng số nguyên tố:", len(P))
# print(P)  # Nếu muốn in toàn bộ tuple
