# Võ Tá Cường , MSV: 245752021610100
# Program make a simple calculator that can add, subtract, multiply and divide using functions

# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    return x / y

# Hiển thị menu lựa chọn
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Nhập lựa chọn từ người dùng
choice = input("Enter choice (1/2/3/4): ")

# Nhập hai số cần tính
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Thực hiện phép tính tương ứng
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    if num2 != 0:  # kiểm tra chia cho 0
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")