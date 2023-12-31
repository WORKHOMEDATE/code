__author__="zhao"

import tkinter as tk
import random
import threading
import time
def dow():
    window = tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0, width)
    b=random.randrange(0, height)
    window.title(':)')
    window.geometry("200x50"+"+"+str(a)+"+"+str(b))
    tk.Label(window,text='电脑被黑客入侵', bg='red', font=('楷体', 17), width=14, height=3).pack()
    window.mainloop()

threads = []
for i in range(190):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()