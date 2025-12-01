# Võ Tá Cường , MSV: 245752021610100
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        # Tách chuỗi thành các từ, đảo ngược danh sách, rồi nối lại
        words = self.text.split()     # ['hello', '.py']
        reversed_words = words[::-1]  # ['.py', 'hello']
        return ' '.join(reversed_words)

# Ví dụ sử dụng
input_text = 'hello .py'
reverser = ReverseWords(input_text)
print(reverser.reverse())  # Kết quả: '.py hello'
