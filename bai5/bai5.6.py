# Võ Tá Cường , MSV: 245752021610100
class StringManipulator:
    def __init__(self):
        self.text = ""  # Khởi tạo biến lưu chuỗi

    def get_String(self):
        self.text = input("Nhập một chuỗi: ")  # Nhận chuỗi từ người dùng

    def print_String(self):
        print(self.text.upper())  # In chuỗi dưới dạng chữ in hoa

# Ví dụ sử dụng
str_obj = StringManipulator()
str_obj.get_String()    # Người dùng nhập chuỗi
str_obj.print_String()  # In ra chữ in hoa
