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


def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = loade_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img  # чтобы сборщик мусора не убрал картинку


def exit():
    window.destroy()

url = 'https://cataas.com/cat'

window = Tk()
window.title('Cats')
window.geometry('600x520')

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0) # tearoff меню предопределено, его нельзя менять
mainmenu.add_cascade(label="Файл", menu=filemenu) # название меню
filemenu.add_command(label="Новый котик", command=open_new_window)
filemenu.add_separator() # разделяющая линия
filemenu.add_command(label="Выход", command=exit)

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

window.mainloop()
