from tkinter import *

window = Tk()
form = Canvas(window,width=500, height=500)
form.pack()



form.create_rectangle(0,0,501,501,fill='gainsboro',outline='gainsboro')
form.create_rectangle(10,10,490,490,fill='light goldenrod',outline='light goldenrod')
form.create_rectangle(45,55,455,470,fill='gray',outline='gray')
form.create_rectangle(80,85,420,450,fill='royal blue',outline='royal blue')
form.create_rectangle(115,155,385,425,fill='white',outline='white')



mainloop()


