import tkinter as tk
from tkinter import ttk


class AngleListener:    # Oberver
    def give_advice(self, event):
        print('Don\'t do it, you might regret it!')


class DevilListener:    # Observer
    def give_advice(self, event):
        print('Ahhh...just do it! Doooo it!')


if __name__ == '__main__':
    window = tk.Tk()
    window.title('TkObservableExample')

    button = ttk.Button(window, text='Should I do it?')         # Observable
    button.pack()
    button.bind('<Button>', AngleListener().give_advice, '+')
    button.bind('<Button>', DevilListener().give_advice, '+')
    button.bind('<Button>', lambda event: print('Meh...Do whatever'), '+')    # lambda function is also an observer

    window.mainloop()
