import tkinter as tk
from PIL import ImageTk, Image
from model import Model

class ImageGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Generator")

        # Создаем элементы
        self.prompt_label = tk.Label(master, text="Prompt:")
        self.prompt_entry = tk.Entry(master, width=50)
        

        self.negative_prompt_label = tk.Label(master, text="Negative Prompt:")
        self.negative_prompt_entry = tk.Entry(master, width=50)
        

        img = Image.open("res/question.jpg")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel = tk.Label(root, image=img)
        self.panel.image = img

        self.generate_button = tk.Button(master, text="Generate", command=self.generate_image)
        
        # Упаковываем элементы в окне
        self.prompt_label.pack()
        self.prompt_entry.pack()
        self.negative_prompt_label.pack()
        self.negative_prompt_entry.pack()
        self.panel.pack()
        self.generate_button.pack()
       
        
        self.model = Model()

    def generate_image(self):
        prompt = self.prompt_entry.get() + " ." + "No " + self.negative_prompt_entry.get()
        self.model.generate_image(prompt)
        
        img = Image.open("res/generation.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel.image = img
        self.panel.config(image=img)

# Создаем главное окно
root = tk.Tk()
root.geometry("650x400+300+150")
root.resizable(width=True, height=True)

# Запускаем приложение
app = ImageGeneratorApp(root)

# Запускаем цикл обработки событий
root.mainloop()
