# Võ Tá Cường , MSV: 245752021610100
import tkinter as tk

class MyApp:
    def __init__(self, root):
        # a) Xây dựng cửa sổ đồ họa
        self.root = root
        self.root.title("Demo Tkinter")
        self.root.geometry("300x200")

        # b & d) Thêm button với màu nền (bg) và màu chữ (fg)
        self.button = tk.Button(
            root,
            text="Nhấn tôi",
            command=self.on_button_click,  # c) Xử lý sự kiện
            bg="lightblue",   # Màu nền
            fg="red"          # Màu chữ
        )
        self.button.pack(pady=50)

    # c) Phương thức xử lý sự kiện button
    def on_button_click(self):
        print("Button đã được nhấn!")

# Khởi tạo cửa sổ
root = tk.Tk()
app = MyApp(root)
root.mainloop()
