# Võ Tá Cường , MSV: 245752021610100
import tkinter
import random

# List màu sắc
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 30  # thời gian chơi gốc

# Hàm bắt đầu game
def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()  # bắt đầu đếm ngược
    nextColour()

# Hàm chọn màu tiếp theo
def nextColour():
    global score
    global timeleft
    
    if timeleft > 0:
        e.focus_set()
        
        # Kiểm tra màu nhập đúng
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

# Hàm đếm ngược
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# Tạo cửa sổ GUI
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

# Thêm label hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Label điểm
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Label thời gian
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Label hiển thị màu
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Entry để nhập màu
e = tkinter.Entry(root)
e.pack()
e.focus_set()

# Bắt sự kiện nhấn Enter
root.bind('<Return>', startGame)
root.mainloop()
