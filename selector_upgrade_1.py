#Import modules
from tkinter import ttk
import bf, kf, ms
from tkinter import *
from tkinter.ttk import *

#Create window
window = Tk()
window.geometry("600x300")
window.title("Fractals")
window.resizable(False, False)
window.configure(bg='black')

# Create Label
label = Label(window, text = "Selected: None")
label.place(
    relx = 0.0,
    rely = 0.0,
    anchor ='nw'
)

#Change label text
def show():
    
    if clicked.get() == "Barnsley fern":
        label.config(text = "Selected: Barnsley fern")
        bf.main()
    elif clicked.get() == "Koch fractal":
        label.config(text = "Selected: Koch fractal")
        kf.main()
    elif clicked.get() == "Mandelbrot set":
        label.config(text = "Selected: Mandelbrot set")
        ms.main()
    else:
        pass

#Reset selection
def reset():
    bf.stop()
    kf.stop()
    ms.stop()

#Options
options = [
    " ",
    "Barnsley fern",
    "Koch fractal",
    "Mandelbrot set"
]

#Datatype of menu text
clicked = StringVar()

#Initial menu text
clicked.set(" ")

# Create Dropdown menu
drop = OptionMenu(window, clicked, *options)
drop.pack()
drop.place (x=200, y=50, width = 200, height=20)

#Button styles
#Show button style
window.style1 = ttk.Style(window)
window.style1.theme_use('alt')
window.style1.configure(
    'show.TButton',
    foreground = 'white',
    background = 'green', 
    font=('Helvetica', 11)
)
window.style1.map('show.TButton', background=[('active','LimeGreen')])
#Reset button style
window.style2 = ttk.Style(window)
window.style2.theme_use('alt')
window.style2.configure(
    'reset.TButton',
    foreground = 'white',
    background = 'blue', 
    font=('Helvetica', 11)
)
window.style2.map('reset.TButton', background=[('active','DeepSkyBlue')])
#Exit button style
window.style3 = ttk.Style(window)
window.style3.theme_use('alt')
window.style3.configure(
    'exit.TButton',
    foreground = 'black',
    background = 'red', 
    font=('Helvetica', 11)
)
window.style3.map('exit.TButton', background=[('active','grey')])

#Buttons
#Show button
btn_show = Button(
    window,
    text = "Show sample",
    style = 'show.TButton',
    command = show
)
btn_show.pack()
btn_show.place (x=50, y=230, width=100, height=40)
#Reset button
btn_reset = Button(
    window, 
    text="Reset",
    style = 'reset.TButton',
    command = reset
)
btn_reset.pack()
btn_reset.place (x=250, y=230, width=100, height=40)
#Exit button
btn_exit = Button(
    window, 
    text="Exit",
    style = 'exit.TButton', 
    command = quit
)
btn_exit.pack()
btn_exit.place (x=450, y=230, width=100, height=40)

# Execute tkinter
window.mainloop()