#gui.py 

import os
import sys
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,width=600,height=500,cursor='cross')
canvas.pack()
photo = tk.PhotoImage(file="pop.ppm") #file or path and loc
canvas.create_image(300,300,image=photo) # photo position
label = tk.Label(
    root,
    text="KINDA FUCKING SUS MA BOY HAPPY BDAYYYYY",
    fg="red"
)
canvas.create_window(100,100,window=label)
root.mainloop()





#top = tkinter.Tk()
#top.mainloop()
#top = Tk()
#top.geometry("100x100")
#def helloCallBack():
#   msg = messagebox.showinfo(" Happy Birthday! ")

#B = Button(top, text = "happy birthday", command = helloCallBack)
#B.place(x = 50,y = 50)
#top.mainloop()