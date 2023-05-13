import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title('tkinter app demo')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
      # TODO: create widgets
      pass

if __name__ == '__main__':
  app = App()
  app.mainloop()
