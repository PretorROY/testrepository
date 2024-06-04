import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Экзамен УБСТ 2102")
root.geometry("1920x1080")

# Указываем путь к изображению
image_path = r"C:\Users\sunri\Desktop\Screenshot_2.png"

# Загружаем изображение и создаем из него объект PhotoImage
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Создаем метку для изображения и размещаем ее в окне
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создаем метку с текстом и настраиваем ее свойства
label = tk.Label(root, text="экзамен убст 2102", fg="red", font=("Helvetica", 24))
label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()