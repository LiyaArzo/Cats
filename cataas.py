from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO #importoutput

def loade_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # если будет ошибка, тут ее получим, для обработки исключения
        image_data = BytesIO(response.content) # байт символы
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS) # корректировка размеров изображения, чтобы оно умещалось в окно
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_image():
    img = loade_image(url)

    if img:
        label.config(image=img)
        label.image = img  # чтобы сборщик мусора не убрал картинку


def exit():
    window.destroy()


window = Tk()
window.title('Cats')
window.geometry('600x520')

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0) # tearoff меню предопределено, его нельзя менять
mainmenu.add_cascade(label="Файл", menu=filemenu) # название меню
filemenu.add_command(label="Новый котик", command=set_image)
filemenu.add_separator() # разделяющая линия
filemenu.add_command(label="Выход", command=exit)




label = Label()
label.pack()

url = 'https://cataas.com/cat'
set_image()

window.mainloop()
