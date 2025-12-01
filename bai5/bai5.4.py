# Võ Tá Cường , MSV: 245752021610100
class RomanConverter:
    # Bảng ánh xạ các ký tự La Mã với giá trị số nguyên
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, roman):
        self.roman = roman.upper()  # Chuyển chữ thường thành chữ hoa nếu cần

    def to_integer(self):
        total = 0
        prev_value = 0
        # Duyệt từ phải sang trái
        for char in reversed(self.roman):
            value = self.roman_dict.get(char, 0)
            if value < prev_value:
                total -= value  # Nếu nhỏ hơn ký tự trước, trừ
            else:
                total += value  # Ngược lại, cộng
            prev_value = value
        return total

# Ví dụ sử dụng
num = RomanConverter("XIV")
print(num.to_integer())  # Kết quả: 14

num2 = RomanConverter("MCMXCIV")
print(num2.to_integer())  # Kết quả: 1994
