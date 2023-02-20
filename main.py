import random
from tkinter import *
from tkinter import messagebox
from random import choice

otvety = ('Да', 'Однозначно', '42', 'К бабке не ходи', 'Я бы на это не рассчитывал', 'Подумай еще раз', 'Ты точно хочешь это знать', 'А сам то как думаешь?', 'Нет', 'Возможно', 'Спросите снова', 'Будущее туманно', 'Духи говорят нет', 'Мне кажется да', 'Без сомнения', 'Не дождешься', 'Ыыыыыыы', 'Не судьба!')

def otvet():
    messagebox.showinfo(title='Ответ', message=random.choice(otvety))

root = Tk()
root.title("Магический шар")
root.geometry("150x70")
b = Button(root, text='Встряхнуть', width='10', height='2', command=otvet)
b.pack(anchor="center", expand=1)

root.mainloop()

