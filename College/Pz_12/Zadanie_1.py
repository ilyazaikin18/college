from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.title("Практическая работа №12")
root.geometry('737x760')
root['bg'] = '#DCDCDC'

Canvas(root, bg="#4682B4", height=50, width=760, highlightbackground="#4682B4").place(x=0, y=0)

Label(
      text='Создайте заказ', width=25, height=1, bg='#4682B4', fg='#ffffff', font=('Time New Roman', "36", BOLD)
).place(x=-10, y=1)

Label(
      text='1. Информация о заказе', width=30, height=1, bg='#DCDCDC', fg='#4682B4', font=('Time New Roman', '18')
).place(x=-75, y=75)

Label(
      text='Номер заказа', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-90, y=115)
Entry(fg='#000000', width=32, font='Calibri 14').place(x=150, y=118)

Label(
      text='Название товара', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-79, y=160)
Entry(fg='#000000', width=32, font='Calibri 14').place(x=150, y=160)

Label(
      text='Количество', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-100, y=200)
Entry(fg='#000000', width=10, font='Calibri 14').place(x=150, y=200)

Label(
      text='2. Контактная информация', width=30, height=1, bg='#DCDCDC', fg='#4682B4', font=('Time New Roman', '18')
).place(x=-59, y=240)

Label(
      text='Ваше имя', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-108, y=280)
Entry(fg='#000000', width=32, font='Calibri 14').place(x=150, y=280)

Label(
      text='Ваш email', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-108, y=320)
Entry(fg='#000000', width=32, font='Calibri 14').place(x=150, y=320)

Label(
      text='Ваш телефон', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-95, y=360)
Entry(textvariable=StringVar(value='+7 ('), fg='#000000', width=18, font='Calibri 14').place(x=150, y=360)

Label(
      text='Формат +7 (999) 999-99-99', width=30, height=1, bg='#DCDCDC', fg='#7D7D7D', font=('Calibri', '12')
).place(x=115, y=390)

Label(
      text='3. Информация о доставке', width=30, height=1, bg='#DCDCDC', fg='#4682B4', font=('Time New Roman', '18')
).place(x=-60, y=415)

Label(
      text='Адрес', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-120, y=450)
text = Text(root, fg='#000000', width=32, height=3, font='Calibri 14').place(x=150, y=450)

Label(
      text='Время доставки', width=30, height=1, bg='#DCDCDC', fg='#000000', font=('Calibri', '14')
).place(x=-82, y=540)
Spinbox(root, from_=0, to=23, width=5).place(x=150, y=545)
Spinbox(root, from_=0, to=59, width=5).place(x=200, y=545)

root.mainloop()
