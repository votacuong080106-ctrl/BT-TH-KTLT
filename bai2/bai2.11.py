# Võ Tá Cường , MSV: 245752021610100
def benefit(t, n, k):
    # Kiểm tra dữ liệu đầu vào
    if t < 0 or n <= 0 or k <= 0:
        print("Dữ liệu không hợp lệ! Vui lòng nhập các số dương.")
        return

    # Tính lãi kép
    total = n * (1 + t / 100) ** k

    # In kết quả
    print(f"Số tiền nhận được sau {k} tháng là: {total:.2f} VND")

    # Trả về giá trị nếu cần dùng lại
    return total


# --- Phần nhập dữ liệu ---
try:
    t = float(input("Nhập lãi suất (%/tháng): "))
    n = float(input("Nhập số tiền gửi ban đầu (VND): "))
    k = int(input("Nhập số tháng gửi: "))

    benefit(t, n, k)
except ValueError:
    print("Vui lòng nhập đúng định dạng số!")
