from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO #importoutput

def load.image(url):


window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load.image(url)

if img:
    label.config(image=img)
    label.image = img #чтобы сборщик мусора не убрал картинку

window.mainloop()
