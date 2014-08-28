from tkinter import *

window = Tk()
form = Canvas(window,width=360, height=200)
form.pack()

def draw_circle(x, y, x1, y1, alpha, betha, fill_color, line_color):
    form.create_arc(x, y, x1, y1, start=alpha, extent=betha-alpha, fill=fill_color, outline=line_color)

#first blue
colors_1=['blue','white','green','yellow','red','blue','pink','gray']
for x in range(0,7):
    if x != 0:
        draw_circle(20+(20*x), 20, 200, 200-(x*20), 180, 270, str(colors_1[x]), 'white')
        print('X2 = {0}, Y2 = {1}'.format(20*x,100-(x*20)))
    else: 
        draw_circle(0, -120, 320, 200, 180, 270, str(colors_1[x]), 'white')
        print('X2 = {0}, Y2 = {1}'.format(20,100))








mainloop()
#4*80=320+40=360
