# Võ Tá Cường , MSV: 245752021610100
import math

def Tinh(R):
    if R <= 0:
        return "Bán kính không hợp lệ!"
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    return chu_vi, dien_tich

# Nhập bán kính từ bàn phím
R = float(input("Nhập bán kính R: "))
kq = Tinh(R)

if isinstance(kq, str):
    print(kq)
else:
    chu_vi, dien_tich = kq
    print("Chu vi hình tròn =", chu_vi)
    print("Diện tích hình tròn =", dien_tich)
