# Võ Tá Cường , MSV: 24575202161010
import tkinter as tk
from tkinter import messagebox

# Hàm hiển thị lựa chọn radio button
def show_selection():
    selection = var.get()
    messagebox.showinfo("Thông tin lựa chọn", f"Bạn chọn: {selection}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân & Radio Button")
root.geometry("400x350")

# ---- Form thông tin cá nhân ----
frame_info = tk.LabelFrame(root, text="Thông tin cá nhân", padx=10, pady=10)
frame_info.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(frame_info, text="Họ tên: Võ Tá Cường", font=('Helvetica', 12)).pack(anchor='w', pady=2)
tk.Label(frame_info, text="Ngày sinh: 01/01/2000", font=('Helvetica', 12)).pack(anchor='w', pady=2)
tk.Label(frame_info, text="MSSV: 245752021610100", font=('Helvetica', 12)).pack(anchor='w', pady=2)
tk.Label(frame_info, text="Ngành học: Công nghệ thông tin", font=('Helvetica', 12)).pack(anchor='w', pady=2)

# ---- Form Radio Button ----
frame_radio = tk.LabelFrame(root, text="Chọn một số", padx=10, pady=10)
frame_radio.pack(fill="both", expand=True, padx=10, pady=10)

# Biến lưu trạng thái lựa chọn radio button
var = tk.IntVar(value=1)  # giá trị mặc định

# Tạo radio button
tk.Radiobutton(frame_radio, text="Lựa chọn 1", variable=var, value=1).pack(anchor='w', pady=2)
tk.Radiobutton(frame_radio, text="Lựa chọn 2", variable=var, value=2).pack(anchor='w', pady=2)
tk.Radiobutton(frame_radio, text="Lựa chọn 3", variable=var, value=3).pack(anchor='w', pady=2)

# Nút Click Me
tk.Button(frame_radio, text="Click Me", command=show_selection).pack(pady=10)

# Chạy GUI
root.mainloop()
