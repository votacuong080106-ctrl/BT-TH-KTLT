# Võ Tá Cường , MSV: 245752021610100
balance = 0

while True:
    line = input("Nhập giao dịch (Enter để kết thúc): ")
    if not line:  # nếu người dùng nhấn Enter, kết thúc
        break
    operation, amount = line.split()  # tách ký hiệu và số tiền
    amount = int(amount)
    if operation.upper() == 'D':
        balance += amount
    elif operation.upper() == 'W':
        balance -= amount

print(balance)
