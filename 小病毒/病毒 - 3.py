__author__="zhao"

import tkinter.messagebox

while True:
    root = tkinter.Tk()
    root.geometry("400x300")
    root.title(":) Windows10正在被攻击 :)")
    root.configure(bg="white")
    label = tkinter.Label(root, text=":) 你的windows正在被攻击 :)", font=("Arial", 20), bg="white")
    label.pack()
    button = tkinter.Button(root, text="Exit", font=("Arial", 10), bg="white", fg="red", command=root.destroy)
    button.pack()
    root.mainloop()
    tkinter.messagebox.askokcancel("退出", "退出吗? :)")
    tkinter.messagebox.askokcancel(":)", "不可能! :)")
    tkinter.messagebox.askokcancel(":)", ":)")
    tkinter.messagebox.askokcancel(":)", ":D 哈哈哈哈哈**** :)")
    tkinter.messagebox.askokcancel(";)", ";) 哈哈哈哈哈哈哈哈哈哈******** :D")
    root = tkinter.Tk()
    root.geometry("1920x1080")
    root.configure(bg="black")
    root.mainloop()
