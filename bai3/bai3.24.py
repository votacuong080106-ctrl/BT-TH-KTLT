# Võ Tá Cường , MSV: 245752021610100
s = input("Nhập câu: ")

upper = 0   # đếm chữ hoa
lower = 0   # đếm chữ thường

for ch in s:
    if ch.isupper():      # kiểm tra chữ hoa
        upper += 1
    elif ch.islower():    # kiểm tra chữ thường
        lower += 1

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
