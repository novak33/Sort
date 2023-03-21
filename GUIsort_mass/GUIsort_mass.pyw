from bingo_sort import bingo
from bose_nelson_sort import bose_nelson
from ins_sort import insertion
from pancake_sort import pancake

import numpy as np
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-100, self.winfo_screenheight()//2-100))
        self.create_widgets()
    
    def bingo_sort(self):
        self.bingo_win = tk.Toplevel()
        self.bingo_win.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-400, self.winfo_screenheight()//2-400))
        self.matrix_output, self.time = bingo(self.matrix[0])
        self.matrix_output = self.matrix_output.reshape(int(self.matrix_N.get()), int(self.matrix_M.get()))
        tk.Label(self.bingo_win, text='Бинго сортировка').grid(row=0)
        tk.Label(self.bingo_win, text=self.matrix_output).grid(row=1)
        tk.Label(self.bingo_win, text='Время работы:'+'%.3f' % self.time + ' s.').grid(row=2)

    def bose_nelson_sort(self):
        self.bose_win = tk.Toplevel()
        self.bose_win.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-400, self.winfo_screenheight()//2-400))
        self.matrix_output, self.time = bose_nelson(self.matrix[0])
        self.matrix_output = self.matrix_output.reshape(int(self.matrix_N.get()), int(self.matrix_M.get()))
        tk.Label(self.bose_win, text='сортировка Боуз-Нельсона').grid(row=0)
        tk.Label(self.bose_win, text=self.matrix_output).grid(row=1)
        tk.Label(self.bose_win, text='Время работы:'+'%.3f' % self.time + ' s.').grid(row=2)

    def insertion_sort(self):
        self.ins_win = tk.Toplevel()
        self.ins_win.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-400, self.winfo_screenheight()//2-400))
        self.matrix_output, self.time = bingo(self.matrix[0])
        self.matrix_output = self.matrix_output.reshape(int(self.matrix_N.get()), int(self.matrix_M.get()))
        tk.Label(self.ins_win, text='сортировка бинарными вставками').grid(row=0)
        tk.Label(self.ins_win, text=self.matrix_output).grid(row=1)
        tk.Label(self.ins_win, text='Время работы:'+'%.3f' % self.time + ' s.').grid(row=2)

    def pancake_sort(self):
        self.pancake_win = tk.Toplevel()
        self.pancake_win.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-400, self.winfo_screenheight()//2-400))
        self.matrix_output, self.time = bingo(self.matrix[0])
        self.matrix_output = self.matrix_output.reshape(int(self.matrix_N.get()), int(self.matrix_M.get()))
        tk.Label(self.pancake_win, text='Блинная сортировка').grid(row=0)
        tk.Label(self.pancake_win, text=self.matrix_output).grid(row=1)
        tk.Label(self.pancake_win, text='Время работы:'+'%.3f' % self.time + ' s.').grid(row=2)

    def get_num(self):
        if self.num.get().isdigit():
            if self.i<=int(self.matrix_N.get())-1 and self.j<=int(self.matrix_M.get())-1:
                self.matrix[self.i][self.j] = int(self.num.get())
                if self.i<int(self.matrix_N.get())-1 and self.j==int(self.matrix_M.get())-1:
                    self.j = 0
                    self.i += 1
                elif self.i==int(self.matrix_N.get())-1 and self.j==int(self.matrix_M.get())-1:
                    self.matrix = self.matrix.reshape(-1, int(self.matrix_N.get())*int(self.matrix_M.get()))
                    self.inmatrx_win.destroy()
                    self.choise_sort_win()
                    return
                else:
                    self.j += 1
                self.name_num['text'] = 'a[' + str(self.i+1) + '][' + str(self.j + 1) + '] ='
        else:
            return

    def new_start(self):
        self.choise_win.destroy()
        self.master.deiconify()

    def create_widgets(self):
        tk.Label(self, text='Введите размерность матрицы').grid(row=0, column=0, columnspan=2)
        self.matrix_N = tk.Entry(self, width=7, justify='center')
        self.matrix_N.grid(row=1, column=0)
        self.matrix_M = tk.Entry(self, width=7, justify='center')
        self.matrix_M.grid(row=1, column=1)
        tk.Button(self, text="NEXT", fg="green", command=self.create_inmatrx_win).grid(row=2, column=0, columnspan=2)
        tk.Button(self, text="QUIT", fg="red", command=self.master.destroy).grid(row=3, column=0, columnspan=2)

    def create_inmatrx_win(self):
        if self.matrix_N.get().isdigit() and self.matrix_M.get().isdigit() and int(self.matrix_N.get()) >= 1 and int(self.matrix_M.get().isdigit()) >= 1:
            self.master.withdraw()
            self.inmatrx_win = tk.Toplevel()
            self.inmatrx_win.geometry('+{}+{}'.format(self.winfo_screenwidth()//2-100, self.winfo_screenheight()//2-100))
            self.matrix = np.zeros((int(self.matrix_N.get()), int(self.matrix_M.get())), dtype=np.int64)
            self.i, self.j = 0, 0
            self.name_num = tk.Label(self.inmatrx_win, text="a[1][1] =")
            self.name_num.grid(row=0, column=0)
            self.num = tk.Entry(self.inmatrx_win)
            self.num.insert(0, 0)
            self.num.grid(row=0, column=1)
            tk.Button(self.inmatrx_win, text='NEXT', fg="green", command=self.get_num).grid(row=1, columnspan=2)
        
    def choise_sort_win(self):
        self.choise_win = tk.Tk()
        self.choise_win.geometry('250x100+{}+{}'.format(self.winfo_screenwidth()//2-150, self.winfo_screenheight()//2-100))
        tk.Button(self.choise_win, text='Бинго', command=self.bingo_sort).grid(row=0, column=0, sticky='nswe', padx=2)
        tk.Button(self.choise_win, text='Боуз-Нельсон', command=self.bose_nelson_sort).grid(row=0, column=1, sticky='nswe', padx=4)
        tk.Button(self.choise_win, text='Бинарные вставки', command=self.insertion_sort).grid(row=1, column=0, sticky='nswe', padx=4)
        tk.Button(self.choise_win, text='Блинная сортировка', command=self.pancake_sort).grid(row=1, column=1, sticky='nswe', padx=4)
        tk.Button(self.choise_win, text="QUIT", fg="red", command=self.new_start).grid(row=2, columnspan=2, sticky='nswe', padx=4)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

