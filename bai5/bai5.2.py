# Võ Tá Cường , MSV: 245752021610100
class Hinhchunhat:
    # 1. Phương thức khởi tạo (__init__): Dùng để xây dựng đối tượng
    #    bằng cách nhận chiều dài (dai) và chiều rộng (rong)
    def __init__(self, dai, rong):
        self.chieu_dai = dai  # Gán giá trị dai cho thuộc tính chieu_dai của đối tượng
        self.chieu_rong = rong # Gán giá trị rong cho thuộc tính chieu_rong của đối tượng

    # 2. Phương thức tính diện tích (tinh_dien_tich):
    #    Công thức: Diện tích = Chiều dài * Chiều rộng
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# --- Ví dụ Sử Dụng ---

# Tạo một đối tượng Hình chữ nhật (Hinhchunhat) với chiều dài 10 và chiều rộng 5
hcn1 = Hinhchunhat(10, 5)

# Gọi phương thức tinh_dien_tich() của đối tượng hcn1
dien_tich = hcn1.tinh_dien_tich()

# In kết quả
print(f"Chiều dài: {hcn1.chieu_dai}, Chiều rộng: {hcn1.chieu_rong}")
print(f"Diện tích của hình chữ nhật là: {dien_tich}")