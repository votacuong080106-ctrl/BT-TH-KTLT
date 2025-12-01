# Võ Tá Cường , MSV: 245752021610100
# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi: ")

# Tạo chuỗi mới không chứa chữ số
chuoi_moi = ""
for ch in s:
    if not ch.isdigit():   # Nếu ký tự không phải là chữ số thì giữ lại
        chuoi_moi += ch

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
