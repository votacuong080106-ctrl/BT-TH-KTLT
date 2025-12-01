# Võ Tá Cường , MSV: 245752021610100
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # mặc định chọn Python

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()

for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()