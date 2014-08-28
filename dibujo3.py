from tkinter import *

window = Tk()
form = Canvas(window,width=900, height=500)
form.pack()
form.create_rectangle(0,0,900,500,fill='#C5C3BB',outline='#C5C3BB')#primer cuadro
form.create_rectangle(100,70,800,430,fill='#A9B1B9',outline='#A9B1B9')#segundo cuadro
form.create_rectangle(150,105,750,395,fill='#E7E9EB',outline='#E7E9EB')#cuadro fondo base blanco
m m m       mmm (150,105, 350,105, 250,153.7, 150,127.46, fill='#808488', outline='#808488')#primer gris oscuro
form.create_polygon(150,127.46, 250,153.7, 200,178.155, 150,165.89, fill='#C5C5C5', outline='#C5C5C5')#1r grisV
form.create_polygon(350,105,    650,105,   550,154.84, fill='#808488', outline='#808488')#2do gris ^
form.create_polygon(350,105,    550,154.84,   500,179.225 , 300,129.385, fill='#C5C5C5', outline='#C5C5C5')#2do GV
form.create_polygon(650,105, 750,105, 750,129.92, fill='#808488', outline='#808488')
form.create_polygon(650,105, 750,129.92, 750,167.765, 600,129.385, fill='#C5C5C5', outline='#C5C5C5')

'''_________________________________________'''

form.create_line(150,202.735,  200,178.155,   250,190.615,  250,153.7,   450,203.54,  500,179.155 ,  550, 191.615, 
550,154.77,      700,192.15,   750,167.765)




form.create_polygon(150,395, 150,382.54, 200,395, 250,370.615, 300,383.075, 350,358.69, 500,395, fill='#808488', outline='#808488')


mainloop()   
