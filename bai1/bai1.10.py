# Võ Tá Cường , MSV: 245752021610100
# Khởi tạo một chuỗi (String)
a = "hi i am python programmer"

# BƯỚC 1: TÁCH CHUỖI (Split)
# Phương thức split() sẽ tách chuỗi 'a' thành một danh sách (List) các từ
# (mặc định dựa trên ký tự khoảng trắng)
b = a.split()

# In danh sách các từ đã tách
print("1. Sau khi TÁCH (Split):")
print(b)

# BƯỚC 2: NHẬP CHUỖI (Join)
# Phương thức join() sẽ nối các phần tử trong danh sách 'b' thành một chuỗi mới
# với ký tự được chỉ định ("-") làm ký tự nối giữa các phần tử.
# Ở đây tôi thay thế ký tự nối bằng "-" để minh họa rõ hơn sự thay đổi.
c = "-".join(b)

# In chuỗi mới đã được nối
print("\n2. Sau khi NHẬP (Join) bằng '-':")
print(c)