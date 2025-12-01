# Võ Tá Cường , MSV: 245752021610100
class ATM:
    def __init__(self, balance=0):
        self.balance = balance  # Khởi tạo số dư

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} VND.")
        else:
            print("Số tiền nạp không hợp lệ!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ!")
        elif amount <= 0:
            print("Số tiền rút không hợp lệ!")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} VND.")

# Chương trình chính
atm = ATM(1000)  # Khởi tạo số dư ban đầu 1000 VND

while True:
    print("\n---- ATM ----")
    print("1. Kiểm tra số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Thoát")
    choice = input("Chọn chức năng (1-4): ")

    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        amount = int(input("Nhập số tiền nạp: "))
        atm.deposit(amount)
    elif choice == '3':
        amount = int(input("Nhập số tiền rút: "))
        atm.withdraw(amount)
    elif choice == '4':
        print("Thoát chương trình. Hẹn gặp lại!")
        break
    else:
        print("Chọn chức năng không hợp lệ!")
