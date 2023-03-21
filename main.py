from tkinter import Tk, Canvas, Entry, Text, END, Label
l = 0
idle = 5
check = None
window = Tk()
window.title("dissappearing text app")
window.config(width=500, height=700,pady=50)

input= Text(window, background="white", width=80, height=30, fg="black", font=("Arial", 20, "normal"),insertbackground='black')
input.grid(column=0, row=1, columnspan=5)
idle_timer = Label(text=f"")
idle_timer.grid(row=0,column=4)
words_list =  input.get('1.0', END).split(' ')
word = Label(text=f"words:{0}")
word.grid(row=0, column=3)
def detect():
    global idle
    global l
    global check
    words_list = []
    text = input.get("1.0", END).strip()
    if len(text) != 1:
        for i in text.split(' '):
            if i != "":
                words_list.append(i)



        word.config(text=f"words:{len(words_list)}")
        if l < len(text):
            l = len(text)
            idle = 5
            idle_timer.config(text="")
        else:
            count_down()
        if idle < 0:
            window.after_cancel(check)
            input.delete("1.0", END)
            idle = 5
            l = 0
            idle_timer.config(text="")
            detect()
            return
    check = window.after(1000,detect)


def count_down():
    global idle
    global idle_timer

    idle_timer.config(text=f"00:{idle}")
    idle -= 1







detect()





window.mainloop()
