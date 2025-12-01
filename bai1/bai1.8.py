# Võ Tá Cường , MSV: 245752021610100
# Tính tổng các số chẵn trong dãy Fibonacci nhỏ hơn 4.000.000
a, b = 1, 2
total = 0

while a < 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("Tổng các số chẵn trong dãy Fibonacci:", total)


