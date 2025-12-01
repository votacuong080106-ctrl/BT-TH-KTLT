# Võ Tá Cường , MSV: 245752021610100
s = input("Nhập câu: ")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():      # kiểm tra chữ cái
        letters += 1
    elif ch.isdigit():    # kiểm tra chữ số
        digits += 1

print("Chữ cái:", letters)
print("Chữ số:", digits)
