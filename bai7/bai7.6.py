# Võ Tá Cường , MSV: 245752021610100
from tkinter import *
from tkinter import messagebox

# =========================
# Các hàm xử lý Menu
# =========================

def NewFile():
    messagebox.showinfo("New File", "New File!")

def OpenFile():
    messagebox.showinfo("Open", "Open File Selected!")

def Exit():
    root.quit()

def InsText():
    messagebox.showinfo("Insert Text", "Insert Text Selected!")

def InsPic():
    messagebox.showinfo("Insert Picture", "Insert Picture Selected!")

def About():
    messagebox.showinfo("About", "This is a simple example of a menu!")

# =========================
# Tạo window
# =========================

root = Tk()
root.title("Menu Example")
root.geometry("350x250")

# =========================
# Tạo menu
# =========================

menu = Menu(root)
root.config(menu=menu)

# ----- Menu File -----
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# ----- Menu Insert -----
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# ----- Menu Help -----
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About...", command=About)

# =========================
root.mainloop()