# Võ Tá Cường , MSV: 245752021610100
# Khởi tạo một danh sách (list) rỗng để lưu trữ các số tìm được
result_numbers = []

# Duyệt qua các số từ 2000 đến 3200 (range(2000, 3201) bao gồm cả 3200)
for n in range(2000, 3201):
    # Kiểm tra hai điều kiện:
    # 1. n chia hết cho 7 (n % 7 == 0)
    # 2. n KHÔNG chia hết cho 5 (n % 5 != 0)
    if (n % 7 == 0) and (n % 5 != 0):
        # Thêm số n vào danh sách sau khi chuyển thành chuỗi (str)
        # để chuẩn bị cho việc in ra theo định dạng chuỗi, cách nhau bởi dấu phẩy
        result_numbers.append(str(n))

# Nối tất cả các phần tử trong danh sách bằng dấu phẩy (",") và in ra màn hình
# Đây là cách hiệu quả nhất để in chuỗi trên một dòng, cách nhau bằng ký tự mong muốn.
print(','.join(result_numbers))