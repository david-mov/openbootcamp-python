import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title('tkinter app demo')

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.create_widgets()

  def create_widgets(self):
    options = {'padx': 5, 'pady': 5}

    # title label
    self.title_label= ttk.Label(self, text='Select a programming language: ')
    self.title_label.grid(column=0, row=0, sticky=tk.NW, **options)

    # languages list
    langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')

    var = tk.Variable(value=langs)

    self.langs_list = tk.Listbox(
       self,
       listvariable= var,
       height=6,
       selectmode=tk.EXTENDED
    )
    self.langs_list.grid(column=0, row=1, sticky=tk.NW, **options)

if __name__ == '__main__':
  app = App()
  app.mainloop()
