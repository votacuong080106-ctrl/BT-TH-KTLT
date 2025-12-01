# Võ Tá Cường , MSV: 245752021610100
# Nhập một dãy các từ từ bàn phím
ds = input("Nhập dãy từ: ").split()

# Tìm độ dài lớn nhất
max_len = max(len(tu) for tu in ds)

# In các từ có độ dài bằng độ dài lớn nhất
print("Các từ dài nhất là:")
for tu in ds:
    if len(tu) == max_len:
        print(tu)
