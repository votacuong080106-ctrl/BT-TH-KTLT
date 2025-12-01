# Võ Tá Cường , MSV: 245752021610100
# Yêu cầu người dùng nhập hai giới hạn a và b
# Sử dụng int() vì đề bài nói là "dãy số tự nhiên"
a = int(input("Enter the start of the range (a): "))
b = int(input("Enter the end of the range (b): "))

print(f"\n--- Numbers and their inverses in range [{a}, {b}] ---")

# Vòng lặp for để duyệt qua các số tự nhiên n từ a đến b (bao gồm cả b)
for n in range(a, b + 1):
    # Số nghịch đảo là 1/n
    # Phải đảm bảo n khác 0. Nếu n=0, ta bỏ qua hoặc báo lỗi.
    if n == 0:
        print("Warning: Cannot calculate inverse for 0 (1/0 is undefined)")
        continue # Bỏ qua vòng lặp này

    # Tính toán
    inverse_fraction = f"1/{n}"
    inverse_decimal = 1 / n # Python tự động thực hiện phép chia float

    # In kết quả
    # Số nghịch đảo (dạng phân số) và kết quả (dạng thập phân)
    print(f"Number (n): {n}")
    print(f"  Inverse (Fraction): {inverse_fraction}")
    print(f"  Inverse (Decimal):  {inverse_decimal}")
    print("-" * 30)