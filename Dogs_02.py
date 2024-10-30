import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb


def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        print(data)
        print((data["message"]))
        print(data["status"])
        return data['message']
    except Exception as e:
        mb.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None

def show_image():
    image_url = get_random_dog_image()

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            # new_window = Toplevel(window)
            # new_window.title("Случайное изображение пёсика")
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f"Картинка № {notebook.index('end') + 1}")
            lb= ttk.Label(tab, image=img)
            lb.pack(padx=10, pady=10)
            lb.image = img

        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


def start_progress():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, lambda: [progress.stop(), show_image()])


window = Tk()
window.title("Случайное изображение")

button = ttk.Button(window, text="Загрузить изображение", command=start_progress)
button.pack(padx=10, pady=10)

progress = ttk.Progressbar(window, mode='determinate', length=300)
progress.pack(padx=10, pady=5)


# Ширина
width_label = ttk.Label(window, text="Ширина:")
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=10, width=10)
width_spinbox.pack(side='left', padx=(0, 10))
width_spinbox.set(300)

# Высота
height_label = ttk.Label(text="Высота:")
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=10, width=10)
height_spinbox.pack(side='left', padx=(10, 10))
height_spinbox.set(300)

top_level_window = Toplevel(window)
top_level_window.title("Изображение собачек")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

window.mainloop()
