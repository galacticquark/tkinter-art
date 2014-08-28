from tkinter import *

window = Tk()
form = Canvas(window,width=500, height=500)
form.pack()
form.create_rectangle(0,0,500,500,fill='gainsboro',outline='gainsboro')
form.create_rectangle(10,10,490,490,fill='#B0414E',outline='#B0414E')
form.create_rectangle(80,130,420,460,fill='#49141A',outline='#49141A')
form.create_rectangle(120,195,380,435,fill='#263131',outline='#263131')






mainloop()
