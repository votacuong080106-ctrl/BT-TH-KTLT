# Võ Tá Cường , MSV: 245752021610100
result = []

for num in range(1000, 3001):  # gồm cả 1000 và 3000
    s = str(num)
    if (int(s[0]) % 2 == 0 and
        int(s[1]) % 2 == 0 and
        int(s[2]) % 2 == 0 and
        int(s[3]) % 2 == 0):
        result.append(s)

print(",".join(result))
