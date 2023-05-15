# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.

# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.

from tkinter import *
import tkinter as tk

root = Tk()
root.title("Счетчик количества символов")
root.geometry("420x300")

def button_clicked(event):
    sum_sim = str(entry.get())
    sum = len(sum_sim)
    last_label['text'] = sum

Label(root, text="Введите любые символы", font="Calibri 14").pack()

entry = tk.Entry(root, font="Calibri 14")
entry.pack()

button = Button(root, text='Выполнить', bg="Grey", fg="white", font="Calibri 14", relief="flat", command="button_clicked")
button.pack()

last_label = Label(root, text='', font="Calibri 14")
last_label.pack(fill=BOTH)

button.bind('<Button-1>', button_clicked)
root.mainloop()
