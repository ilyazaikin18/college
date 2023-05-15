import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#000000', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="../Pz_16/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить расходы', command=self.open_dialog, bg='#FFFFFF', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="../Pz_16/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать расходы", command=self.open_update_dialog,
                                    bg='#FFFFFF',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="../Pz_16/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить расходы", command=self.delete_records, bg='#FFFFFF',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="../Pz_16/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск расходов", command=self.open_search_dialog, bg='#FFFFFF',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="../Pz_16/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить расходы", command=self.view_records, bg='#FFFFFF',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('data', 'kod', 'name', 'ras', 'sum'), height=15, show='headings')

        self.tree.column('data', width=100, anchor=tk.CENTER)
        self.tree.column('kod', width=180, anchor=tk.CENTER)
        self.tree.column('name', width=155, anchor=tk.CENTER)
        self.tree.column('ras', width=140, anchor=tk.CENTER)
        self.tree.column('sum', width=140, anchor=tk.CENTER)

        self.tree.heading('data', text='Дата')
        self.tree.heading('kod', text='Код продукта')
        self.tree.heading('name', text='Наименование продукта')
        self.tree.heading('ras', text='Расходы')
        self.tree.heading('sum', text='Сумма')

        self.tree.pack()

    def records(self, data, kod, name, ras, sum):
        self.db.insert_data(data, kod, name, ras, sum)
        self.view_records()

    def update_record(self, data, kod, name, ras, sum):
        self.db.cur.execute("""UPDATE users SET data=?, kod=?, name=?, ras=?, sum=? WHERE ras=?""",
                            (data, kod, name, ras, sum, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE kod=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, name):
        name = (name,)
        self.db.cur.execute("""SELECT * FROM users WHERE name>=?""", name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить продукт')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Дата')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=180, y=25)

        label_kod = tk.Label(self, text='Код продукта')
        label_kod.place(x=30, y=50)
        self.entry_kod = ttk.Entry(self)
        self.entry_kod.place(x=180, y=50)

        label_name = tk.Label(self, text='Наименование продукции')
        label_name.place(x=30, y=75)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=180, y=75)

        label_ras = tk.Label(self, text='Расходы')
        label_ras.place(x=50, y=100)
        self.entry_ras = ttk.Entry(self)
        self.entry_ras.place(x=180, y=100)

        label_sum = tk.Label(self, text='Сумма')
        label_sum.place(x=50, y=125)
        self.entry_sum = ttk.Entry(self)
        self.entry_sum.place(x=180, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_kod.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_ras.get(),
                                                                       self.entry_sum.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_kod.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_ras.get(),
                                                                          self.entry_sum.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('../Pz_16/saperpz.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                data TEXT,
                kod TEXT NOT NULL,
                name INTEGER NOT NULL DEFAULT 1,
                ras INTEGER,
                sum INTEGER
                )""")

    def insert_data(self, data, kod, name, ras, sum):
        self.cur.execute("""INSERT INTO users(data, kod, name, ras, sum) VALUES (?, ?, ?, ?, ?)""",
                         (data, kod, name, ras, sum))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Расходы по видам продукции")
    root.geometry("900x750+300+200")
    root.resizable(False, False)
    root.mainloop()
