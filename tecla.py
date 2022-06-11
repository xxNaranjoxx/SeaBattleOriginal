from tkinter import *

ventana = Tk()
ventana.geometry("700x300+0+0")

img = PhotoImage(file="1.png")
btn = Button(ventana,image=img,height=40,width=100).place(x=100,y=100)

ventana.mainloop()