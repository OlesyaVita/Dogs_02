from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb

def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            respone = requests.get(image_url, stream=true)
            respone.raise_for_status()
            img_data = BytesIO(respone.content)
            img = Image.open(img_date)
            img.thumbnail((300, 300))
            lable.config(image=img)
            lable.image = img
        except Exception as e:
            mb.showerror("Ошибка", message=f"Возникла ошибка {e}")


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

lable = Label()
lable.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)
window.mainloop()

